section 4

## VPNs
- Client-based VPN
Must be donwloaded on the computer and can also be configured to allow access to specific domains and software and such.
Works mostly as if you where connected to the companies network.
Can be configured to give users less or more permissions on the company network.
- SSL VPN
uses a web browser as the VPN client.
Can be configured to only allow access to specific domains (IE gmail or something) or only intranet sites.
Accessed through a webbrowser based gateway.
Does not require for you to install anything.

## Why use a VPN?
- It will anonimize your public IP
- Chances are the company who's VPN you are connecting to is logging your IP and data.
- The VPN could also not be very secure itself as the companmy sucks at security.
- Does not guarantee privacy but can help bypass firewall and regional restrictions on a hostile network.

## When connecting to an HTB VPN (or any hacking focused lab)
- Treat the network as if it where hostile.
Which means
- Disallow password auth if SSH is enabled on your VM.
- do not leave any sensitive data on our attack VM.


## Shell
- literally just a program on linux that takes input and passes commands back to the OS.
- Others exist IE cmd.exe or powershell.
- Python shell, awk, php java etc also exist
## Shell types
- Reverse shell # Creates a connection with a "listener" on our attack box
- Bind shell # "binds" to a specific port on the target host and waits for a connection from the attack box
- Web shell # Runs OS system commands through a web browser. Can only be used to run single commands. (IE uploading a php script or to levarage file vulnerability).


## What is a port?
- Ports are virtual points of connection for networks. It is the place where connections begin and end.
- Can be thought of as a window or a door on a house and can be used to access the machine.
- Types of ports are generally associated with a specific process or service and allow for computers to tell the difference between different traffic types (IE ssh traffic flows through a different port than web requests to a website even though they go through the same network.

- Each port is assigned a number and is standardized amongst ALL network connected devices. You can configure a device to run a non-standard port. This is just a convention and can be broken.
- Ex, HTTP messages generally go through port 80 while HTTPS messages go through port 443 unless configured otherwise.
- Port numbers allow us to access specific services or applications running on target devices.
- Ports help computers how to understand different types of data sent to them.

## Two main categories of ports.
- Transmission Control Protocol (TCP)
TCP is connection-oriented, so a connection between the client and the server has to be established before data can be exchanged.
Server must be awaiting connections from the client.
Usually lossless and more stable.
Useful for integrity-based applications (IE sneding a text file or an exe)
TCP may sometimes require retransmission which can cause it to be faster.
- User Datagram Protocol (UDP)
Utilizes a connectionless comms model. There is no handshake. this introduces some level of unreliability.
Has no guarantee of data delivery.
Useful for time-sensitive applications (IE streaming video or sound)
Dropping packets is FASTER than waiting for delayed packets due to retransmission.

There are different 65,535 TCP ports and 65,535 different UDP ports. All of them are denoted by a number.

List of well known ports and their protocols

PORT NUM       PROTOCOL
20/21 (TCP)    FTP
22 (TCP)       SSH
23 (TCP)       TELNET
25 (TCP)       SMTP
80 (TCP)       HTTP
161 (TCP/UDP)  SNMP
389 (TCP/UDP)  LDAP
443 (TCP)      SSL/TLS (HTTPS)
445 (TCP)      SMB
3389 (TCP)     RDP

## More detailed info on ports and their respective protocols
File Transfer Protocol 20/21
- Used for transfering files (port 20 handles the data and port 21 handles the control commands)
- considered insecure

Secure Shell (SSH) port 22
- Very secure protocol
- Used for remote login and CLI execution
- Can be used over an unsecured network cuz its encrypted

Secure File Transfer Protocol (SFTP) port 22
- Uses ssh to transfer files over securely.
- is encrypted

Telnet port 23
- Its very insecure
- Outdated version of SSH

Simple Mail Transfer Protocol (SMTP) Port 25
- SMTP is by default not secured by default.
- Used mainly for emails and such






