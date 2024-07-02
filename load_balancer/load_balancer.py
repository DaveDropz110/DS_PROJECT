import subprocess

import time
import logging
from flask import Flask, jsonify, request
from consistent_hash import ConsistentHash

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
ch = ConsistentHash()

def run_docker_command(command):
    # Run some docker command
    logger.debug(f"Running docker command: {command}")
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        logger.error(f"Docker command failed: {result.stderr}")
        raise Exception(f"Docker command failed: {result.stderr}")
    logger.debug(f"Docker command output: {result.stdout.strip()}")
    return result.stdout.strip()

def remove_all_servers():
    # Remove all the servers
    logger.info("Removing all existing servers")
    try:
        servers = run_docker_command("docker ps -a --format '{{.Names}}' --filter 'name=server_'").split('\n')
        for server in servers:
            if server:
                run_docker_command(f"docker stop {server} && docker rm {server}")
        logger.info(f"Removed {len(servers)} servers")
    except Exception as e:
        logger.error(f"Error removing servers: {str(e)}")

def ensure_server(server_name):
    # Make sure a server is running
    logger.info(f"Ensuring server: {server_name}")
    try:
        run_docker_command(
            f"docker run -d --name {server_name} --network load_balancer_network -e SERVER_ID={server_name} server-image")
        ch.add_server(server_name)
        logger.info(f"Server {server_name} created and added to consistent hash")
        # Wait for the server to be ready
        time.sleep(2)
    except Exception as e:
        logger.error(f"Error ensuring server {server_name}: {str(e)}")

# Remove all existing servers and initialize with 3 new servers
logger.info("Initializing servers")
remove_all_servers()
for i in range(1, 4):
    server_name = f"server_{i}"
    ensure_server(server_name)

logger.info("Server initialization complete")
logger.info(f"Consistent hash ring state: {ch.hash_ring}")

@app.route('/rep', methods=['GET'])
def get_replicas():
    # Get the replicas
    logger.info("Getting replicas")
    output = run_docker_command("docker ps --format '{{.Names}}' --filter 'name=server_'")
    replicas = output.split('\n') if output else []
    logger.info(f"Found {len(replicas)} replicas: {replicas}")
    logger.info(f"Consistent hash ring state: {ch.hash_ring}")
    return jsonify({
        "message": {
            "N": len(replicas),
            "replicas": replicas
        },
        "status": "successful"
    }), 200

@app.route('/add', methods=['POST'])
def add_servers():
    # Add servers
    logger.info(f"Consistent hash ring state after adding servers: {ch.hash_ring}")

@app.route('/rm', methods=['DELETE'])
def remove_servers():
    # Remove servers
    logger.info(f"Consistent hash ring state after removing servers: {ch.hash_ring}")

@app.route('/<path>', methods=['GET'])
def route_request(path):
    # Route the request
    logger.info(f"Routing request for path: {path}")
    logger.info(f"Current consistent hash ring state: {ch.hash_ring}")
    server = ch.get_server(hash(request.url))
    if not server:
        logger.error("No servers available")
        return jsonify({
            "message": "No servers available",
            "status": "failure"
        }), 500

    logger.info(f"Selected server: {server}")
    try:
        result = run_docker_command(f"docker exec {server} curl -s http://localhost:5000/{path}")
        logger.info(f"Response from server: {result}")
        return result, 200
    except Exception as e:
        logger.error(f"Error communicating with server: {str(e)}")
        return jsonify({
            "message": f"Error communicating with server: {str(e)}",
            "status": "failure"
        }), 500

@app.route('/debug', methods=['GET'])
def debug_info():
    # Get debug info
    logger.info("Getting debug info")
    docker_ps = run_docker_command("docker ps")
    docker_network = run_docker_command("docker network inspect load_balancer_network")
    return jsonify({
        "docker_ps": docker_ps,
        "docker_network": docker_network,
        "consistent_hash_ring": ch.hash_ring
    }), 200

if __name__ == '__main__':
    # Start the load balancer
    logger.info("Starting load balancer")
    app.run(host='0.0.0.0', port=5000)
