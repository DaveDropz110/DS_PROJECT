# Load Balancer Implementation

This project implements a load balancer using Flask and Docker. The load balancer distributes requests to multiple servers running in Docker containers.

## Prerequisites

- Docker
- Docker Compose
- VirtualBox (if running on a virtual machine)

## Setting Up the Environment

### Mounting the Shared Directory (for VirtualBox Users)

If you are using VirtualBox to run a Linux virtual machine, you need to mount the shared directory from your host Windows system.

1. Create a directory where you'll mount the shared folder:
    ```sh
    sudo mkdir /home/server
    ```

2. Mount the shared folder to the directory you just created:
    ```sh
    sudo mount -t vboxsf load_balancer /home/server
    ```
![image](https://github.com/user-attachments/assets/f6940613-88b3-48f1-94f7-c5992722f636)

### Building Docker Images

Navigate to the project directory (either the mounted directory or your project directory) and build the Docker images.

1. Build the load balancer image:
    ```sh
    docker build -t loadbalancer-image -f Dockerfile-loadbalancer .
    ```


![image](https://github.com/user-attachments/assets/12e2d823-5aef-4e68-84bc-b1f81b1e1f13)




2. Build the server image:
    ```sh
    docker build -t server-image -f Dockerfile-server .
    ```
![image](https://github.com/user-attachments/assets/bbe3fc20-64fc-4d11-a1dc-014678608f6c)

## Running the Containers

Use Docker Compose to run the containers defined in the `docker-compose.yml` file.

1. Start the containers:
    ```sh
    docker-compose up
    ```
![image](https://github.com/user-attachments/assets/74f19a97-462c-4d00-a7f2-8cbb506594ba)
![image](https://github.com/user-attachments/assets/e597ee7b-2c70-4815-9cfe-0b16c259d98a)


This command will start the load balancer and server containers as defined in the `docker-compose.yml` file.

## File Descriptions

### Dockerfile-loadbalancer

Builds the Docker image for the load balancer. Installs necessary dependencies, sets up the environment, and runs the load balancer application.

### Dockerfile-server

Builds the Docker image for the server. Installs necessary dependencies, sets up the environment, and runs the server application.

### docker-compose.yml

Defines the services for the load balancer and server containers, including network configurations and ports.

### `load_balancer.py`

The main application file for the load balancer. Manages the consistent hashing, adding and removing servers, and routing requests.

### `consistent_hash.py`

Implements the consistent hashing algorithm used by the load balancer to distribute requests across multiple servers.

### `server.py`

The server application file. Defines endpoints for the home and heartbeat routes.

## Additional Information

- The load balancer listens on port `5000`.
- The server containers are part of a Docker network called `load_balancer_network`.
- The `SERVER_ID` environment variable is used to identify each server.


