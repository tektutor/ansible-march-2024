# Day 3

## Info - Ansible inventory types
<pre>
1. Static inventory
2. Dynamic inventory ( usually a python script )
</pre>

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

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/863529be-e976-4f03-a843-772e54b1a247)

## Lab - Let's test these containers if we can ssh into them without typing password

Let's try to connect to ubuntu1 container via ssh as shown below
```
ssh -p 2001 root@localhost 
```
Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8af1bdcb-1999-478a-8642-09ca3c1fe0a0)

## Lab - Ping the ansible nodes
```
cd ~/ansible-march-2024
git pull
cd Day3/ansible
ansible -i inventory all -m ping
ansible -i inventory ubuntu -m ping
ansible -i inventory centos -m ping
ansible -i inventory centos1 -m ping
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/23e462a6-5fad-4b7d-9dfa-3ab9b7cbaf6c)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/e8dc54be-8522-4300-a6ff-fa12f4921b5e)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/fc65425c-effa-470b-bfa2-dab9fe315693)

## Lab - Stopping nginx service using ansible ad-hoc command
```
cd ~/ansible-march-2024
git pull
cd Day3/ansible
ansible -i inventory ubuntu -m shell -a "service nginx stop"
```

## Lab - Running ansible playbook
```
cd ~/ansible-march-2024
git pull
cd Day3/ansible/playbooks
ansible-playbook -i inventory install-nginx-playbook.yml
```
Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8e02da83-7a18-433d-8ece-3b7eefe70d33)

Let's see if we can access the web page from ubuntu1 and ubuntu2 ansible nodes
```
curl http://localhost:8001
curl http://localhost:8002
```

![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/eb49350b-e0b8-4be1-a21b-e8be4f6320be)


Accessing the web page from ubuntu1 and ubuntu2 ansible nodes
```
curl http://localhost:8001
curl http://localhost:8002
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/0739b094-f1a7-4065-b57f-57c66ea6f7f0)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/eb7af250-deb3-4874-928d-82b14df08b3c)

## Lab - Running the updated install nginx playbook
```
cd ~/ansible-march-2024
git pull
cd Day3/ansible/playbooks
ansible-playbook -i inventory install-nginx-playbook.yml
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/67ec8811-7658-4d9a-9495-abd663b5abbe)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/756760d7-ddbd-4115-bf30-82e29838e491)

Accessing the web page from ubuntu1 and ubuntu2 ansible nodes
```
curl http://localhost:8001
curl http://localhost:8002
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/f2f71fb8-4ab9-422f-9b58-1646f6047f14)

## Lab - Dry running playbook without actually making any changes in the ansible nodes
```
cd ~/ansible-march-2024
git pull
cd Day3/ansible/playbooks
ansible-playbook -i inventory -C install-nginx-playbook.yml
```
Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/415ba120-f391-4ace-bff4-c08b5666abd3)
