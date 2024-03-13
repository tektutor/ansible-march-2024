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


## Lab - Building a Custom CentOS Docker Image and use it as a CentOS Ansible Node
```
cd ~/ansible-march-2024
git pull
cd Day3/CustomDockerImages/centos
ssh-keygen
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/centos-ansible-node:latest .
```
