//TODO - Finish notes on OWASP top 10.


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

Domain Name System (DNS) Port 53
- Not inherently secure
- Designed for DNS servers.
- Designed to be usable but not very secure by default

Dynamic Host Configuration Protocol (DHCP) Port 67 and 68
- Automatically assigns IP addresses and network configs to devices
- Port 67 is used by the DHCP server to receive client requests
- Port 68 is used by the client to receive DHCP server requests
- Not inherently secure

Trivial File Transfer Protocol (TFTP) Port 69 (nice)
- Simpler version of FTP
- Used for very small files
- Not secure at all

HyperText Transfer Protocol (HTTP) Port 80
- Not secure or encrypted
- Used for websites to show websites on your computer

Network Time Protocol (NTP) Port 123
- Used to synchronize computer times on networks to ensure accurate time keeping
- Critical for logs and other time sensitive stuff
- Not secure

Simple Network Management Protocol (SNMP) Port 161/162
- Used for monitoring and managing network devices (IE routers and/or switches or servers or more)
- 161 is used by the SNMP manager to send requests to devices
- 162 is used by devices to send alerts to the manager
- Secure but only in V3. All other versions are insecure

Lightweight Directory Access Protocol (LDAP) Port 389
- Not considered secure
- Used for accessing directory information (literally just stuff in folders)
- Sorta acts like a phonebook for different networks where you can manage users/devices and such.

HyperText Transfer Protocol Secured (HTTPS) Port 443
- Secure version of HTTP
- Widely used for transfering data between your browser and a website.
- Address (URL) ensures it gets to the right person (using UDP/TCP transmissions)

Server Message Block (SMB) Port 445
- Not secured by default
- Used for sharing files between devices on 1 network. Allows for files to be accessed as if they are local
- There are technically 5 different SMB versions
- Sorta like a library for your server

Syslog Port 514
- Used by devices for organizing logs for a single centralized log server
- Not secure by default

Simple Mail Transfer Protocol Secure (SMTPS) Port 587/465
- Secure version of SMTP

Lightweight Directory Access Protocol over SSL (LDAPS)
- Used to securely access data in folders securely to protect the data.
- Technically SSL is deprecated. Often the S refers to Secured
- Secured

Structured Query Language (SQL) Port 1433
- Used for making sql queries and edits and such.
- Not inherently safe and requires some configuration to make it secure.

Remote Desktop Protocol (RDP) Port 3389
- Allows for remote control of other people's desktops. Used by the IT guys to help you make your computer work
- Not secure by default but can be pretty easily made secure.

Session Initiation Protocol (SIP) Port 5060/5061
- Used for managing communication stuff over IP networks (IE voice calls or messaging)
- Port 5060 version is not encrypted or secured
- Port 5061 is secured over TLS
- Sorta like a digital event planner for messages/calls

## Web servers and what do they do???!??!?!???!!
- The backend of a website pretty much
- Responds to clients (IE browsers MOSTLY)
- Typically use TCP ports such as 80 or 443 (in other words HTTP and HTTPS protocols)
- Web apps are very high value targets for attacakers because they can provide a very vast attack surface.

## Owasp top 10
- Owasp top 10 is just a list of the 10 most dangerous web server vulnerabilities.
# 1. Broken Access Control
- Access control enforeces policies such that users may not access anything outside their own INTENDED permissions.
- failures typically lead to unauthorized information disclusure, modification, destruction or performing a business function that the user is not supposed to do (IE adding a bajillion dubloons to someones bank account)
- Bypassing access control checks by modifying the URL, (parameter tampering or force browsing), internal application state or the HTML webpage.
- Viewing/accessing someone else's account via it's uique identifier
- accessing APIs using missing access controls (POST PUT and DELETE)
- elevation of privelege. Acting as a user without being logged in for example.
- Metadata manipulation such as tampering with a JSON web token, cookie or hidden field etc.
- CORS misconfiguration can allow for API access from untrusted origins.
- Force browsing (guessing URLs) to authenticate pages as an unauthorized user or to privilege pages as a standard user.

Access control is only effective if it is implemented SERVER side not on the frontend. This is because backend is much harder to modify from the outside generally speaking.

# 2. Security Misconfiguration

# 3. Software Supply Chain Failures

# 4. Cryptographic Failures

# 5. Injections

# 6. Insecure Design

# 7. Authentication Failures

# 8. Software or Data Integrity Failures

# 9. Security Logging and Alerting Failures

# 10. Mishandling of Exceptional Conditions

## Basic Tools
SSH
- A tool used to remotely access computers on the same network or over the internet
- SSH connections are usually much more stable than reverse shell connections
- Really cool stuff highkey
- Can technically be a victim of a man-in-the-middle attack if someone uses your IP you could accidentally connect to it.
- Very secure
- VERIFY THE KEY seriously do this through a secured channel just to be sure.
- Uses public key authentication
- Secure but not anonymous because your public key identifies you.
- Uses public key cryptography

Public key cryptography

Properties
- Creates two mathematically linked keys One private and one public
- Anyone with the public key can encrypt data but not decrypt it. This key is also assumed to be easily seen by anyone who wants to see it
- Anyone with the private key can decrypt data but not encrypt. This key is assumed to never leave the machine.
- Private key can be used to derive the public key but NOT the other way around. (essentially public key is a hash of the private key)

Example
- Imagine Alice and Bob both each have differing public and private keys.
- Alice wants to send Bob a message.
- She does this by ENCRYPTING her message using BOBs public key.
- Then Bob and ONLY Bob can decrypt that message using his private key since no-one else has his private key.
- Same thing when Bob wants to send alice a message.
- Say someone wanted to decrypt the message sent by bob, it would be impossible because he doesn't have Alice's private key
- Same thing goes for the message send by alice.

Symmetric key cryptography

Properties
- One singular key can both ENCRYPT and DECRYPT messages.

Example
- Alice and bob both share a key which they shared and agreed upon a long time ago.
- Say alice wants to send bob a message.
- Alice will encrypt her message using the key.
- Then bob can freely decrypt it because he knows the key Alice used.
- Noone else knows bob's or alice's keys so they cannot read the message.

- The problem with this technique is that it requires for the exchange of these keys beforehand.
- This poses a security concern and is inconvenient.


Netcat
- 










