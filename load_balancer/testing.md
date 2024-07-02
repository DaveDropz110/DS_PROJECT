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


### Running Tests with Docker

1.Build the test image:
    
    docker build -t loadbalancer-test -f Dockerfile-test .
    
2. Run the test container:

    ```sh
    docker run --network=host loadbalancer-test
    ```


### This provides instructions on how to add and run test cases within a Docker container.

