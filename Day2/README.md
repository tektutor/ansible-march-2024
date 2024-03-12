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

## Lab - Finding the version of Docker you are using
```
docker --version
```

Expected output
<pre>
root@tektutor.org:~# docker --version
Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1  
</pre>

```
docker info
```
Expected output
<pre>
root@tektutor.org:~# docker info
Client:
 Version:    24.0.5
 Context:    default
 Debug Mode: false

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 24.0.5
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 
 runc version: 
 init version: 
 Security Options:
  apparmor
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.5.0-21-generic
 Operating System: Ubuntu 22.04.4 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 24
 Total Memory: 62.48GiB
 Name: tektutor.org
 ID: 30abfe9c-99b6-4e45-80b9-4868b207da52
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false  
</pre>

## Lab - Listing docker images from Local Docker Registry
```
docker images
```

Expected output
<pre>
root@tektutor.org:~# docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE  
</pre>

## Lab - Download docker images from Docker Hub Remote Registry to your Docker Local Registry
```
docker pull ubuntu:latest
docker images
docker pull centos:7.9.2009
docker images
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/f4d8d5e8-9895-426d-a58d-34543ca2e4b8)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/7a08db1a-51e9-4851-a065-892386d8fccb)

## Lab - Deleting a docker image from your Docker local registry
```
docker pull hello-world:latest
docker images
docker rmi hello-world:latest
docker images
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/4cae123e-9429-4c15-9b2e-020c30df4ec1)
