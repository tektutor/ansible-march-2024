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

## Docker High Level Architecture
![Docker Architecture](DockerHighLevelArchitecture.png)

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

## Lab - Creating your first docker container
```
docker run hello-world:latest
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/d5d7a519-7a05-49f0-a251-7f36c313ce0d)

## Lab - Renaming a container
```
docker ps -a
docker rename wonderful_pasteur hello-container
docker ps -a
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/ebfe1609-277c-48b3-bc53-9de63c9d890f)

## Lab - Listing network types docker supports
```
docker network ls
docker network inspect bridge
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/ee8e1250-eb50-4995-a20e-74dcdd54f0e2)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/2dc2f6a3-86c0-4ccf-bff5-651047482f5c)

## Lab - Deleting a container 
```
docker ps -a
docker rm hello-container
docker ps -a
docker rm ubuntu1
docker stop ubuntu1
docker rm ubuntu1
docker ps -a
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/b335d08c-4cfb-4d93-82e2-0c1bedf378b5)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/a6e87c3b-f58c-4f1d-ac2a-535770817264)


## Lab - Port fowarding - Setup a load balancer with nginx

Delete any container that might conflict
```
docker rm -f $(docker ps -aq)
```

Let's create 3 web server containers
```
docker run -d --name nginx1 --hostname nginx1 nginx:latest
docker run -d --name nginx2 --hostname nginx2 nginx:latest
docker run -d --name nginx3 --hostname nginx3 nginx:latest
docker ps
```

Let's create the lb container with port-forwarding
```
docker run -d --name lb --hostname lb -p 80:80 nginx:latest
docker ps
```

Let's create the nginx.conf with the below content on your local machine
```
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    upstream servers {
        server 172.17.0.2:80; 
        server 172.17.0.3:80;
        server 172.17.0.4:80;
    }
    
    server {
        location / {
            proxy_pass http://servers;
        }
    }
}
```

Let's copy the nginx.conf from your local machine to the lb container
```
docker cp nginx.conf lb:/etc/nginx/nginx.conf
```

We need to restart the lb container to apply the config changes
```
docker restart lb
```

Let's check if the lb container is running
```
docker ps
```

Let's update the index.html on nginx1, nginx2 and nginx3 containers
```
echo "Web Server 1" > index.html
docker cp index.html nginx1:/usr/share/nginx/html/index.html

echo "Web Server 2" > index.html
docker cp index.html nginx2:/usr/share/nginx/html/index.html

echo "Web Server 3" > index.html
docker cp index.html nginx3:/usr/share/nginx/html/index.html
```

We can now test if the lb container is able to load balance the requests. On your ubuntu lab machine type the below url

```
http://localhost
```

Each time you refresh the output should come from nginx1, nginx2 and nginx3 containers in a round-robin fashion.

## Lab - Creating a mysql db server container
```
docker run -d --name mysql --hostname mysql -e MYSQL_ROOT_PASSWORD=root mysql:latest
docker ps
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/73c224d0-4cee-40cb-84fb-e0cbc80e1e7b)

Let's open a shell inside the mysql container, when it prompts for password, type root
```
docker exec -it mysql /bin/sh
mysql -u root -p
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/3fcc02a8-53c1-4f3a-abac-7b94c4fa73fc)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/98e4e943-c0c8-4a6e-b081-847518cde5da)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/0046ae5e-0227-476e-9928-16ecb055a27c)

Now, let's use external volume to store the database

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8863b01f-7df1-4a61-9501-b9821ebb3823)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/9b477f60-9feb-45f7-b714-4d412ad36890)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/78195856-0373-41cb-baa5-32ac0e2af2e2)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/3a171f1a-6c1f-4c72-8216-93b47a64ea81)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/4561310f-79ac-4bab-942f-e9164013e366)

# Ansible

## Info - What is a Configuration Management Tool?
- used by System Administrator to automate software installation/uninstallation/update/upgrade
- Examples
  - Puppet
  - Chef
  - Salt/Salt Stack
  - Ansible

## Info - Puppet 
- this is the oldest configuration management tool
- this came around year 2008
- it uses Puppet Language as DSL(Domain Specific Langauage)
- DSL - nothing but language used to automate
- it follows client/server architecture
- installation of Puppet is bit tedious
- learning Puppet requires mastering Puppet language

## Info - Chef
- this came after Puppet
- this uses Ruby as the DSL
- it follow client/server architecture
- installation is tedious
- learning chef requires mastering Ruby scripting language

## Info - Ansible
- this is one of the more latest configuration management tool
- this is developed in Python by Micheal Deehan
- Michael Deehan was former employee of Red Hat
- Yaml is the DSL used by Ansible
- YAML - superset of JSON
- Ansible comes in 2 flavours
  - Ansible core - opensource and command-line only
  - AWX - opensource variant of Ansible Tower ( supports Web Interface )
   - developed on top of Ansible core
  - Ansible Tower - Red Hat enterprise product - Web console (GUI)
    - developed on top of AWX

## Lab - Finding ansible version
```
ansible --version
```

Expected output
<pre>
root@tektutor.org:~# ansible --version
ansible 2.10.8
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
</pre>
