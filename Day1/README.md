# Day 1

## Kindly complete the pre-test and let me now

## On Premise Server
- Servers owned by your organization

## Public Cloud
- AWS, GCP, Azure, Digital Ocean, etc
- Servers that you can rent from Amazon, Google, Microsoft online

## What is Static IP?
- it won't change even if the machine rebooted

## What is Dynamic IP?
- it will chnage everytime the machine is rebooted

## What is Private IP?
- the IP Address is accessible only within that machine/same network

## What is Public IP?
- the IP address is accessible from Internet

## Linux Distributions
- Ubuntu
- Fedora
- CentOS
- Red Hat Enterprise Linux (RHEL)
- Kali

## What is Package Manager?
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

## What is a subnet?
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


## Connecting to the ec2 instance from your lab machine using ssh
```
cd ~/Downloads
chmod 400 ./jegan-new.pem
ssh -i ./jegan-new.pem ubuntu@ec2-52-12-170-75.us-west-2.compute.amazonaws.com
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8e53e395-96c4-4478-a93e-cefd7fe7316c)
