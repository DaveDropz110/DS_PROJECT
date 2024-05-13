from flask import Flask
import hashlib

app = Flask(__name__)

# Number of virtual servers (simulated by positions on the hash ring)
NUM_VIRTUAL_SERVERS = 20

@app.route('/home', methods=['GET'])
def home():
    request_id = 123  # Example request ID
    virtual_server_id = consistent_hash(request_id)
    server_id = map_virtual_server_to_server(virtual_server_id)
    return f'Hello from Server: {server_id}\n'

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return '', 200

def consistent_hash(request_id):
    # Calculate hash value of the request ID
    hash_value = hashlib.sha256(str(request_id).encode()).hexdigest()
    # Map hash value to a virtual server on the hash ring
    virtual_server_id = int(hash_value, 16) % NUM_VIRTUAL_SERVERS
    return virtual_server_id

def map_virtual_server_to_server(virtual_server_id):
    # Map virtual server ID to a server container ID
    # In a real-world scenario, this would involve a lookup table or configuration
    return 1  # Single server ID for simplicity

if __name__ == '__main__':
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port)
