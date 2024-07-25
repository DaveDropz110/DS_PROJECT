## Testing

### Adding Test Cases

Ensure you have test cases that cover the key functionalities of the project. Add your test cases to the `tests` directory.

### Running the Tests

1. Ensure the services are up and running:
    ```sh
    docker-compose up -d
    ```

![image](https://github.com/user-attachments/assets/b6091a5b-e944-47c7-afad-64b6c3b53163)



### Running Tests with Docker

1.Build the test image:
    ```sh
    docker build -t loadbalancer-test -f Dockerfile-test .
    ```
    ![image](https://github.com/user-attachments/assets/f79431ee-7999-4bd6-baea-f18d651ad113)

    
2. Run the test container:

    ```sh
    docker run --network=host loadbalancer-test
    ```


### This provides instructions on how to add and run test cases within a Docker container.

