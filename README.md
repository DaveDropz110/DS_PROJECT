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
    sudo mkdir /mnt/server_project_share
    ```

2. Mount the shared folder to the directory you just created:
    ```sh
    sudo mount -t vboxsf server_project /mnt/server_project_share
    ```

### Building Docker Images

Navigate to the project directory (either the mounted directory or your project directory) and build the Docker images.

1. Build the load balancer image:
    ```sh
    docker build -t loadbalancer-image -f Dockerfile-loadbalancer .
    ```

2. Build the server image:
    ```sh
    docker build -t server-image -f Dockerfile-server .
    ```

## Running the Containers

Use Docker Compose to run the containers defined in the `docker-compose.yml` file.

1. Start the containers:
    ```sh
    docker-compose up
    ```

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


