# Day 3

## Lab - Building a Custom Ubuntu Docker Image and use it as an Ubuntu Ansible Node
```
cd ~/ansible-march-2024
git pull
cd Day3/CustomDockerImages/ubuntu
ssh-keygen
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ubuntu-ansible-node:latest .
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/a078ac07-f129-4ce2-8d28-9f6c9bbaeaca)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/900fa11f-e17f-4105-bba7-c83c27a2548a)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/57d36e2e-fd73-4e4f-ae4b-7b895ea9e2d1)


## Lab - Building a Custom CentOS Docker Image and use it as a CentOS Ansible Node
```
cd ~/ansible-march-2024
git pull
cd Day3/CustomDockerImages/centos
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/centos-ansible-node:latest .
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/ea5d7a89-04f7-4124-a68e-885f695a77d6)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/40239fe1-2c9b-46fe-be4f-aa9eb1f43a96)


## Lab - Let's create couple of containers using our custom docker image
```
docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ubuntu-ansible-node:latest
docker run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ubuntu-ansible-node:latest

docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/centos-ansible-node:latest
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/centos-ansible-node:latest

docker ps
```
