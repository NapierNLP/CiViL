# CiViL Project

The dockerized version of the project facilitates the process of installing the system on your local machine.

## Base system requirements

* Docker, Docker-Compose

## Installation

The following installation instructions are taken from the websites below. Check them out for more details.
* https://docs.docker.com/install/linux/docker-ce/ubuntu/
* https://docs.docker.com/install/linux/linux-postinstall/
* https://docs.docker.com/compose/install/

### Set up the repository

1. Update the `apt` package index:
```bash
sudo apt update
```
2. Install packages to allow `apt` to use a repository over HTTPS:
```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```
3. Add Docker’s official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint:
```bash
sudo apt-key fingerprint 0EBFCD88
```
The output should look as follows:
```bash
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]
```
4. Use the following command to set up the stable repository:
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

### Install Docker Engine - Community

1. Update the `apt` package index:
```bash
sudo apt update
```
2. Install the latest version of Docker Engine - Community:
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
3. Verify that Docker Engine - Community is installed correctly by running the hello-world image:
```bash
sudo docker run hello-world
```
This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.

### Post-installation steps

Docker Engine - Community is installed and running. The docker group is created but no users are added to it. You need to use `sudo` to run docker commands. Fulfilling the following steps will let you run docker commands without `sudo`.
1. Create the docker group:
```bash
sudo groupadd docker
```
2. Add your user to the docker group:
```bash
sudo usermod -aG docker $USER
```
3. Run the following command to activate the changes to groups:
```bash
newgrp docker
```
4. Verify that you can run docker commands without `sudo`:
```bash
docker run hello-world
```

### Install Docker Compose

1. Run this command to download the current stable release of Docker Compose:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
2. Check if your ip address matches the address in the docker-compose.yml file. Type the following command and look for "docker0":
```bash
ip addr show
```
If your ip address is different, change it in the docker-compose.yml file.


## Usage

### Testing CiViL project

First, you need to build docker containers:
```bash
docker-compose up --build --no-cache
```
Note: You may want to start the system in detached mode by adding -d to the docker-compose command, the console output can then be accessed using docker-compose logs -f *service_name*.


### Re-building containers after you've made changes to the project

When you make changes to the project (e.g. to some CiViL bots), you will need to rebuild the containers.

To take the system down and remove the virtual network run:

```bash
docker-compose down
```

To remove all unused images:
```bash
docker image prune -a
```

To remove all building cache:
```bash
docker builder prune -a
```

If you just wish to re-build the images that have been changed and restart the necessary containers without downtime run:

```bash
docker-compose up --build  --no-cache

```
Only containers with changes will be rebuilt, the others will be skipped.

### Viewing system logs

Use the following command if you wish to view system logs:
```bash
docker-compose logs -f
```
Use the following command if you wish to view the output of a particular system service such as the directions_bot:
```bash
docker-compose logs -f directions_bot
```
To exit the preview, press `Ctrl+C`. You can also use `docker attach directions_bot` to view the logs, but this directly attaches the terminal so when you press `Ctrl+C`, it'll stop the service.
