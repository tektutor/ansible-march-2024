# Day 2

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
