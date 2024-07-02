## Testing

### Adding Test Cases

Ensure you have test cases that cover the key functionalities of the project. Add your test cases to the `tests` directory.

### Running the Tests

1. Ensure the services are up and running:
    ```sh
    docker-compose up -d
    ```

2. Run the tests using `pytest`:
    ```sh
    pytest tests/
    ```

### Sample Test Case (test_load_balancer.py)

Create a `tests` directory and add a file named `test_load_balancer.py` with the following content:

```python
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

```
### Running Tests with Docker

1.Build the test image:
    
    docker build -t loadbalancer-test -f Dockerfile-test .
    
2. Run the test container:

    ```sh
    docker run --network=host loadbalancer-test
    ```


### This provides instructions on how to add and run test cases within a Docker container.

