# Day 1

## Info - On Premise Server
- Servers owned by your organization
- also referred as On-Prem servers

## Info - Data Center
- a physical facility that organizations uses to host their critcal applications and data
- key components of a data center design include routers, switches, firewalls, storage systems, servers
  
## Info - Public Cloud
- AWS, GCP, Azure, Digital Ocean, etc
- Servers that you can rent from Amazon, Google, Microsoft online

## Info - What is Static IP?
- it won't change even if the machine is rebooted
- it could be private/public

## Info - What is Dynamic IP?
- it will change everytime the machine is rebooted
- it could be private/public

## Info - What is Private IP?
- the IP Address is accessible only within that machine/same network

## Info - What is Public IP?
- the IP address is accessible from Internet
- this could be static/dynamic
  
## Info - Linux Distributions
- Ubuntu
- Fedora
- CentOS
- Red Hat Enterprise Linux (RHEL)
- Kali

## Info - What is a Package Manager?
Examples
- apt/apt-get, yum, rpm, dnf, nuget, chocolatey
- it is software utility that is used to install/uninstall/update/upgrade softwares
- every Linux Distributions supports one or two types of package managers
- For example
  - Ubuntu - apt/apt-get is the package manager
  - CentOS - yum or rpm or dnf
  - RHEL - yum or rpm or dnf
  - Kali - apt

## Info - What is Hypervisor?
- is a software that helps you run multiple OS on the same laptop/desktop/workstation/server
- multiple OS can be actively running side by side
- it is a combination of hardware + software technology
- AMD Processors Virtualization feature - AMD-V
- Intel Processors Virtualization feature - VT-X
- two types
  - Type 1 - used in servers/workstations ( doesn't require a Host OS )
  - Type 2 - used in laptops/desktops/workstations ( requires a Host OS - can be Windows/Mac/Linux )

## Info - What is VPC?
- Virtual Private Cloud
- it is a big network usually that could support 65536 IP addresses
  
## Info - What is a subnet?
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

## Info - What is Key pair?
- for an unix/linux user, instead of typing password to login an unix/linux/mac machine, we could create a key pair
- key pair contains a private key and a public key
- the private key will be kept on the same machine where it was created, usually in the home directory /home/jegan/.ssh/id_rsa
- the public key will be distributed to the trusted machines usually these keys are appended to a file called authorized_keys in the trusted machine /home/some-user/.ssh/authorized_keys
- when you login from your machine to a remote machine that has your public key, the remote machine gives the public key of yours which will be validated against the private key stored in your home directory, if it matches you will be allowed to login the remote machine without password
- this is an alternate way to login to unix/linux/mac machines without typing password
- this is considered more security compared to typing password 

## Info - Services offered by Public Cloud Vendors
- renting just the hardware - which is called Infrastructure as a Service ( IaaS)
- renting hardware + OS - which is called Platform as a Service ( PaaS )
- renting hardware + OS + Software - which is referred as Software as a Service ( SaaS)
![3 models](iaas.jpeg)

## Info - What is an ec2 instance?
- it is a virtual machine we can create in the public AWS cloud
- virtual machines could be created on our laptops/desktops/workstation/on-prem servers
- virtual machines could also be created on AWS/Azure/GCP/Digital Ocean public cloud portals
- is an Infrastructure as a Service (IaaS)
- in this model, Amazon takes care of networking, storage, servers and managing virtualization
- We need to take care of Operating System, application and data

## Lab - Login to AWS Web Console with your login credentials shared to you ( You need to perform all the lab exercies in the lab machine browser not on your office laptop web browser )

Once you login, your AWS web console would look like this
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/229e7409-3c1b-48e9-8bdf-60acd8f46033)

## Lab - Creating an ec2 instance with Ubuntu 22.04 Linux
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/094d7851-6ca5-448e-b5f2-6d2f7aec8d31)

Click on the Launch instances that show up in the top right corner (orange color)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/c0ce2d06-94b4-4f62-9112-1ab704604dc2)

Under the name and tags, type yourname-ubuntu-ec2
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/b0b32c6d-06cb-446f-a9ab-70e95ba7e0e2)

Under the Application and OS Images, select Ubuntu
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/360a107c-47ec-4935-9021-6bea8546cf14)

Under the Instance type, select t2-micro
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/266bc2ba-5984-4939-a13c-11c7f69bdd33)

Under key-pair, select 'create new key pair' to generate new key-pair and download the same onto your lab machine.
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/76737535-3184-4523-a131-08ac5ed22cde)

Under Network settings, select existing security group, in my case I chose launch-wizard-1
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/6cad4011-1b0f-482d-b4df-df851ebc225a)

Under Configure storage, accept the default size
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/a66684f9-e1dc-4288-82a1-4af167a20948)

Click on launch instance at the bottom right corner ( orange color button )
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/c0a4f083-64a7-42d7-9829-2309e3037cd3)

Click on the ec2 instance link that appears in green color
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/130830a2-c59d-42a7-98d8-419a048f8d9b)


## Connecting to the ec2 instance from your lab machine using ssh
Now select the check box that appears on the left side of your ec2 instance that is running
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/4049a509-c981-40ea-bd51-01ff215e8f94)

Click on "connect" button that appears in the top
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/4948a0e6-ec48-43d7-8278-dccee6b9269b)

Copy the command that show near Example
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/b4f9fe7b-b261-487c-8d56-a78e08b8e5a1)


```
cd ~/Downloads
chmod 400 ./jegan-new.pem
ssh -i "jegan-new.pem" ubuntu@ec2-54-245-204-120.us-west-2.compute.amazonaws.com
```

Expected output
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/e67ed0de-a60f-4c53-9ea4-319957334860)

Find the hostname and ip address of your ec2 instance
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8b524c80-a07c-491b-99ad-07976b0adf01)

You need to install net-tools before you could run ifconfig command
```
sudo apt install -y net-tools
```
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/1717db22-3798-4070-90e2-d32fc1bddbc5)

Now try to find the ip address
```
ifconfig
```
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/c9bee850-2b7b-4d3f-9e73-18d7fd493695)

You may exit the ssh connection
```
exit
```
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/3834fc00-cfd4-4264-ae48-e6552198d6a2)

Terminate the ec2 instance
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8df64cf5-8b1f-44c6-a251-4185a0fd97c0)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/78e7c64d-a2e6-423f-b5c5-123a8efb4e22)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/5d678024-1a88-4f42-878d-a52656ed615e)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/999b59e6-7cb4-485c-802a-1cf5f34db967)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/962e7b37-8bbc-42b7-9b10-c7ca42536ef3)

## Lab - Creating a windows ec2 instance
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/c6b3df64-dd65-4649-85b2-c2bce31370a0)

In the the top right corner, you will find "Launch Instance" in orange color, click on it
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/b531d780-7811-4869-94c9-0642b09be9f6)

Under Name and Tags, type yourname-windows-ec2
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/ef2432e7-1467-4b1f-ba3b-71175c30c28c)

Application and OS Images, select Windows
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8f8d48dd-41fc-4664-ba82-33ceddaca781)

Instance type, select "t2 micro"
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/74ef2774-c49d-474b-a67d-17da0f7b79f1)

Under key-pair, select the key-pair you created while creating your ubuntu ec2 instance
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/96887dd7-dd40-4584-92ba-9a242c315890)

Under Network Settings, select existing security group
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/d59f309f-b420-4cd0-814f-a68736cb0382)

Configure storage, accept the default storage
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/6af83acd-902e-4aef-89f0-3b2208eb63ff)

Click on "Launch instance" orange button
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8dbfee20-3b76-400c-a69a-bf1d988d8d17)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/54bc115d-73f4-429f-8e87-da6f78173dc6)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/58879b16-37b4-47c1-8cec-565616ac67ff)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/edc06e76-f783-465c-8b51-a5e818833524)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/b7133c81-f4c3-4904-a3b0-81e954b388f3)

Select the checkbox that appears in front of the ec2 instance name and click on "Connect" that appeas in the top 
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/db7ac652-57c1-4cd5-b22d-30310f262475)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/bdb9afdb-3164-4ab1-91ad-e0de9e06d94a)

Click on the "Download remote desktop file" to your lab machine.
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8db5dded-033f-47c8-a5b8-869f4e691f11)

Open Remina (Windows Remote Desktop client software on your Ubuntu Lab machine )
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/8e1ef222-acc4-4d4c-a316-e87341afe05a)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/6d7d875a-3e3d-4427-986a-dae5b0245bfe)

Click on "Add a new connection profile"
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/382f9346-7167-45ea-b513-91e8fccf0709)

Copy the "Public DNS"
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/0af31613-412a-4051-9bde-773b91819c3a)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/635881bb-ad88-4feb-ad9e-296dd0dca8ae)

Click on the "Get password"
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/0731d691-b77e-4518-8f07-47ee81cc208d)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/2b6b82bd-d52b-474f-bf3d-d655b5f5e540)

Click on the "Upload private key file" button
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/7e811a3c-0ffd-4052-8d21-9fa16e4834ee)

Click on "Decrypt password" button
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/b660d784-4d7f-4e4b-8aa6-cefbbb764591)

Copy the password and paste it in Remina
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/3f625a42-4ac9-473f-8e7b-450bc7b40890)

Click on "Save and Connect" button in Remina
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/3f625a42-4ac9-473f-8e7b-450bc7b40890)

Click on "Yes" to accept certificate
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/bc790b04-1892-4592-8ffa-651f152912aa)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/1c4409ed-838e-46f5-ba6f-6798361ab832)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/b696e2b8-a8a2-489e-9aa6-2823c927b789)

Make sure, your terminate the Windows ec2 instance once you have completed this lab exercise
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/fdb273b5-ff7c-42a5-b8cc-b601035999c5)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/304e5c8c-9c21-40dc-a50f-3a1a032e2212)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/fa1e0653-0644-43d0-ac96-0724d91df261)
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/aa0a288b-bc66-4fb6-9bb9-3afbf78901e6)


## Info - What is a Load Balancer?
- distributes traffic to servers or applications
- AWS supports 4 types of load balancers
- Classic Load Balancer
- Applicaiton Load Balancer (ALB)
- Network Load Balancer (NLB)
- Gateway Load Balancer (GLB)

## Info - What is an AWS Classic Load Balancer?
- can distribute incoming traffic to EC2 instances, containers, IP addresses in one or more Availability zones
- monitors the health of targets and only routes to healthy targets
- supports scaling either manually or automatically
- 

## Lab - Creating an application Load Balancer

We need to create 2 ec2 instances with Ubuntu 22.04 OS

Once the ec2 instances starts running, connect to the ec2 instance
```
ssh -i "jegan-new.pem" ubuntu@ec2-54-245-204-120.us-west-2.compute.amazonaws.com
```
![image](https://github.com/tektutor/ansible-march-2024/assets/12674043/e67ed0de-a60f-4c53-9ea4-319957334860)


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

