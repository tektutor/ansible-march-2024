# Day 1

## On Premise Server
- Servers owned by your organization
- also referred as On-Prem servers

## Data Center
- a physical facility that organizations uses to host their critcal applications and data
- key components of a data center design include routers, switches, firewalls, storage systems, servers
  
## Public Cloud
- AWS, GCP, Azure, Digital Ocean, etc
- Servers that you can rent from Amazon, Google, Microsoft online

## What is Static IP?
- it won't change even if the machine is rebooted
- it could be private/public

## What is Dynamic IP?
- it will change everytime the machine is rebooted
- it could be private/public

## What is Private IP?
- the IP Address is accessible only within that machine/same network

## What is Public IP?
- the IP address is accessible from Internet
- this could be static/dynamic
  
## Linux Distributions
- Ubuntu
- Fedora
- CentOS
- Red Hat Enterprise Linux (RHEL)
- Kali

## What is a Package Manager?
Examples
- apt/apt-get, yum, rpm, dnf, nuget, chocolatey
- it is software utility that is used to install/uninstall/update/upgrade softwares
- every Linux Distributions supports one or two types of package managers
- For example
  - Ubuntu - apt/apt-get is the package manager
  - CentOS - yum or rpm or dnf
  - RHEL - yum or rpm or dnf
  - Kali - apt

## What is Hypervisor?
- is a software that helps you run multiple OS on the same laptop/desktop/workstation/server
- multiple OS can be actively running side by side
- it is a combination of hardware + software technology
- AMD Processors Virtualization feature - AMD-V
- Intel Processors Virtualization feature - VT-X
- two types
  - Type 1 - used in servers/workstations ( doesn't require a Host OS )
  - Type 2 - used in laptops/desktops/workstations ( requires a Host OS - can be Windows/Mac/Linux )

## What is VPC?
- Virtual Private Cloud
- it is a big network usually that could support 65536 IP addresses
  
## What is a subnet?
- logical network, VPC is divided into many logical networks called Subnet
- Subnets allows System administrators to apply different security policies for different Subnets
- there could be a Subnet for accounts departmnet, HR dept, COO office(CEO, CTO & CFO), Software, IT, etc with different permissions and network policies
- it is a range of IP address
- in other words IP block
- small network
- IPV4 or IPV6
- 192.168.49.0/24
- 24 (CIDR)

- 192.168.0.0/16 - how many IPs are there?
- a.b.c.d ( 32 bits - 4 bytes )
- a(8 bits - Octet)
- b(8 bits - Octet)
- c(8 bits - Octet)
- d(8 bits - Octet)

192.168.49.0
192.168.49.1
...
192.168.49.255

192.168.49.108
192.168.49.105

## What is Key pair?
- for an unix/linux user, instead of typing password to login an unix/linux/mac machine, we could create a key pair
- key pair contains a private key and a public key
- the private key will be kept on the same machine where it was created, usually in the home directory /home/jegan/.ssh/id_rsa
- the public key will be distributed to the trusted machines usually these keys are appended to a file called authorized_keys in the trusted machine /home/some-user/.ssh/authorized_keys
- when you login from your machine to a remote machine that has your public key, the remote machine gives the public key of yours which will be validated against the private key stored in your home directory, if it matches you will be allowed to login the remote machine without password
- this is an alternate way to login to unix/linux/mac machines without typing password
- this is considered more security compared to typing password 

## Lab - Login to AWS Web Console with your login credentials shared to you
Once you login, your AWS web console would look like this
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/229e7409-3c1b-48e9-8bdf-60acd8f46033)


## Connecting to the ec2 instance from your lab machine using ssh
```
cd ~/Downloads
chmod 400 ./jegan-new.pem
ssh -i ./jegan-new.pem ubuntu@ec2-52-12-170-75.us-west-2.compute.amazonaws.com
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8e53e395-96c4-4478-a93e-cefd7fe7316c)

## Lab - Creating an application Load Balancer

We need to create 2 ec2 instances with Ubuntu 22.04 OS

Once the ec2 instances starts running, connect to the ec2 instance
```
ssh -i "jegan-new.pem" ubuntu@ec2-54-213-192-149.us-west-2.compute.amazonaws.com
```

From the ec2 instance, install nginx web server
```
sudo apt update
sudo apt install -y nginx
```

Repeat this in the second ec2 instance as well
```
ssh -i "jegan-new.pem" ubuntu@ec2-34-218-232-228.us-west-2.compute.amazonaws.com
sudo apt update
sudo apt install -y nginx
```

