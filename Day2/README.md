# Day 2
## My medium blogs
https://medium.com/tektutor/container-engine-vs-container-runtime-667a99042f3
https://medium.com/@jegan_50867/docker-overview-be840f727b3
https://medium.com/@jegan_50867/docker-commands-ba19387383b4

## YouTube Channel
https://www.youtube.com/@JeganathanSwaminathan

## Docker Overview
- It is developed in Google Go programming language by an organization called Docker Inc
- comes in 2 flavours
  - Community Edition - Docker CE
  - Enterprise Edition - Docker EE
- it follows Client/Server Architecture
- Docker Server is referred as Docker Application Container Engine
- Docker Client is docker
- Docker Registry
  - is a server with a collection of many Docker Images
  - there are 3 types of Docker Registries
    - Local Docker Registry
    - Private Docker Registry ( Optionally you setup Nexus/Artifactory Server )
    - Remote Docker Registry ( Docker Hub Website )

- Docker Image
  - is a specification/blueprint of a Docker container
  - it has atleast one application with all its dependent libraries
  - We can create any number of Docker container instances using a single Docker Image
  - Docker container is an instance of a Docker Image
 
- Docker Container
  - each container is an application process not a OS
  - each container gets it own IP address
  - has its own network stack
  - every container get its own software defined network card
  - every container container has its own file system ( files and folders )
  - usually one container represents one application which is also the best practice

## What is Container Engine?
- Docker is a Container Engine
- Docker depends on containerd for managing images and containers
- Containerd depends on runC container runtime to manage containers
- offers user-friendly commands to create and manage containers without the need to know any Kernel low-level technical details
  Examples
  - Docker depends on runC container Runtime
  - Podman depends on CRI-O Container Runtime
    
## What is Container Runtime?
- they are low-level softwares which are generally not used by end-users like us
- these are used by Container Engines
- Examples
  - runC
  - CRI-O
