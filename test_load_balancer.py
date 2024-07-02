import pytest
import requests

def test_home():
    response = requests.get('http://localhost:5000/home')
    assert response.status_code == 200
    assert "Hello from Server" in response.json()['message']

def test_heartbeat():
    response = requests.get('http://localhost:5000/heartbeat')
    assert response.status_code == 200
    assert response.text == ""

def test_add_remove_server():
    # This is a placeholder test case to show structure
    assert True
