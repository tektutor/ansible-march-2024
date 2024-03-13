# Day 3

## Lab - Building a Custom Ubuntu Docker Image and use it as an Ubuntu Ansible Node
```
cd ~/ansible-march-2024
git pull
cd Day3/CustomDockerImages/ubuntu
ssh-keygen
cp ~/.ssh/id_rsa.pub authorized_keys
docker built -t tektutor/ubuntu-ansible-node:latest .
```

## Lab - Building a Custom CentOS Docker Image and use it as a CentOS Ansible Node
```
cd ~/ansible-march-2024
git pull
cd Day3/CustomDockerImages/centos
ssh-keygen
cp ~/.ssh/id_rsa.pub authorized_keys
docker built -t tektutor/centos-ansible-node:latest .
```
