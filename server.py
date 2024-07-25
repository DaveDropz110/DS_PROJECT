from flask import Flask, jsonify
import os

app = Flask(__name__)

SERVER_ID = os.environ.get('SERVER_ID', 'Unknown')
# Get server ID from environment

@app.route('/home')
def home():
    # Respond with a hello message
    return jsonify({
        "message": f"Hello from Server: {SERVER_ID}",
        "status": "successful"
    }), 200

@app.route('/heartbeat')
def heartbeat():
    # Just a heartbeat
    return "", 200

if __name__ == '__main__':
    # Start the server
    app.run(host='0.0.0.0', port=5000)
