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

## Public key cryptography

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

## Symmetric key cryptography

Properties
- One singular key can both ENCRYPT and DECRYPT messages.

Example
- Alice and bob both share a key which they shared and agreed upon a long time ago.
- Say alice wants to send bob a message.
- Alice will encrypt her message using the key.
- Then bob can freely decrypt it because he knows the key Alice used.
- Noone else knows bob's or alice's keys so they cannot read the message.

- The problem with this technique is that it requires for the exchange of these keys beforehand.
- This poses a security concern and is inconvenient compared to public key cryptography


# Netcat
- Netcat is a network utility for interacting with TCP and UDP ports. It can be used for many things during a pentest.
- Mainly useful for connecting to shells. 
- Can be used to connect to any LISTENING port and interact with the service that's running on the port.
- SSH for example is programmed to handle connections over port 22 to send data and keys.

# Tmux
- Pretty much a tiling window manager but inside of a single terminal
- Manages multiple terminals in 1 terminal. Kinda neat.
- Get used to using Tmux. Seriously its useful


## Service Scanning
- A service is an application that runs on a computer and does something for other computers. 
- Specialized machines for services are just servers.
- As cybersec people, what we're interested in is if we can coerce these services act differently than as they are intended. (this would be a vulnerability possibly)
- Port 1 to 1023 out of the 1 to 65535 ports are reserved for specialized functions.
- Port 0 is reserved for TCP/IP networking and is not used by TCP or UDP messaging. 
- If anything attempts to bind to port 0, it will instead bind to the next available port above port 1024 because port 0 is treated as a "wildcard" port.
- Instead of having to examine all 65535 ports manually, tools such as Nmap have been designed to make this easier.

## NMap
- performs many different types of scans on ports of a given IP adress. Very useful tool.
- The STATE heading will show a couple of main options
# Open
- to mean you can freely attempt to connect
# Filtered
- Usually means there's some kind of firewall on this port only allowing some IPs to attempt to connect.

# SERVICE

- Usually specifies the service that is TYPICALLY associated with the port number. 
- The default scan does NOT tell you the actual service running on the port
- nmap by default does a TCP scan and not a UDP scan.
- The default scan will will assume the service running on the port is the standard service as per the port conventions.

Many ports are commonly associated with windows or linux (for example port 3389 is the default port for Remote Desktop Services and is a sign that you are connecting to a windows machine.

Port 22 being available indicates that you are on a linux/unix machine.

the -sC parameter of nmap lets you specify which script should be used to gain more detailed information.

-sV parameer instructs nmap to perform a version scan which lets nmap fingerprint the services on the traget system and identify their protocols, application names and version number. Version scan uses a massive databse of over 1000 service signatures, 

-p- tells nmap that you want to scan EVERY single port out of all 65535 ports.

-sV and -sC parameters increase how long the scan takes because it has to perform a ton more checks instead of performing only a TCP handshake

- The -sC parameter runs a ton of useful default scripts against the ports to gain more information about them.

version scans can also reveal which OS you are scanning if the version of the protocol mentions it.

The sV parameter will fingerprint the services on the target system and will acquire the protocol, the application name and the version.
It is very informative.


# nmap scripts
- -sC will run a bunch of default scripts but will also allow you to specify a script.
- you can specify a script by running nmap '--script <script name> -p<port> <host>'
# Attacking Network Services - nmap also has functionality that allows you to grab the banner of a given host.
- It looks as follows 'nmap -sV --script=banner <target>'
- 

# FTP (File Transfer Protocol)
- Ports that run the FTP protocol often contain very useful information
- You can connect to FTP services/ports using the 'ftp' command line utility

# SMB (Server Message Block)
- Prevalant protocol on Windows machines
- Moves data around (very sensitive data IE credentials)
- Some SMB versions are vulnerable to RCE exploits such as EternalBlue.
- nmap has tools for enumerating SMB (IE smb-os-discovery.nse which extracts the operating system version).

# Shares
- SMB also allows for users and admins to share folders so that they become accessible remotely by eachother. These tend to contain sensitive info
- A tool that allows you to enumerate and access these shares is the smbclient tool.

# SNMP
- Access to routers is controlled using literal plaintext strings. 
- The default configuration for SNMP protocol is "public" which means you only have read access to the data
- "private" means read and write access.
- Vulnerable to IP spoofing attacks.

- A tool called snmpwalk lets you interact with snmp protocoled devices.


## Web Enumeration

- Sometimes you may run into webservers on port 80 or 443. Webservers host webapps (sometimes more than 1)
- Webapps are a JUIIICY attack service. Very high value target for a pen-test.
- Proper web enumeration is CRITICAL especially when organizations are not exposing too many services 
- Or if they are patched appropriately.

# Gobuster
- tools like fuff or GoBuster lets you uncover hidden files and perform directory enumerations
- This can find hidden files and pages.
- has functionality that allows DNS, vhost and directory brute forcing
- Can even perform remote code execution

# Directory/File Enumeration using gobuster
- 'gobuster dir' mode lets you enumerate directories of web servers.
- a couple example dictionaries you could use would be 'common.txt'
- code 200 means you are allowed to access the dir.
- code 403 means you are not allowed to access the directory.
- code 301 means you are being redirected.
- there's many more status codes.
- Wordpress is an enormous attack potential attack surface.
# DNS subdomain enumeration with gobuster
- Subdomains of websites can also provide an attack surface (IE admin panels or applications with additional functionality which could be exploited)
- https://github.com/danielmiessler/SecLists has some useful lists and such for DNS and DIR enumeration.
- remember to add a dns to your /etc/resolv.conf before doing any DNS enumeration to specify a DNS.

# Banner Grabbing / Web Server Headers on websites
- The banner of a webserver is a very revealing piece of info.
- It can tell you if the server has been misconfigured or is missing crucial security options
- It can tell you exactly whats running on the server (mainly which web framework is in use)
- cURL can be used to retrieve the banner of a webserver.

# whatweb
- Tool used for the extraction of versions of webservers that use frameworks.
- 'whatweb <ip>'

# Certificates
- SSL/TSL certrificates are also a potentially valueble source of info if HTTPS is in use.
- The reason for this is because the certificate can reveal the country, state,organization, emails, name of issuer, and a bunch of other personal info aswell.

# robots.txt
- robots.txt files are files that specify rules for webcrawlers to follow. It can contain webpages that you can sometimes access.

# source code
- Can be worth checking for any new webpages you come across. Hit CTRL + U to bring up the source code.

# Public Exploits
- When we identify a service using nmap, one of the first steps is to check if the service has any public exploits. (public exploits are known exploits that have been found on the web that haven't yet or can't be fixed.
- Literall just google '<application> exploit>.
- A well known tool for this is searchsploit but there are also others. (exploit DB, rapid7 DB, Vulnerability Lab).

# Metasploit Primer
- MetaSploit primer (MSF) is a tool for pentesters that has built-in exploits and public vulnerabilities. It povides an automated way to use these exploits against vulnerable targets.
- It has features like 
- recon scripts which let you enumerate the target and remote hosts
- verification scrips to test the existence of a vulnerability without compromising the target
- meterpeter which is a tool that lets you remotely connect to shells on compromised targets.
- post-exploitation and pivoting tools
- RHOST means the target host's IP (can also be a list of IPs)
- RPORT represents the port of the target
- LHOST represents the IP of the attacking machine.
- LPORT is the local port you're listening on
- Dont overrely on Metasploit primer. It will sometimes fail which means you'll have to switch to manual methods. 
- Good pentesters know when to switch between automatic and manual methods.
- Different exploits on metasploit do different things (some open a shell some just extract a file or whatever).

# Retired Boxes
- There are a shit ton of retired boxes you can try metasploit exploits on. If you want. It's highly recommended.
- List of retired boxes
Granny/Grandpa
Jerry
Blue
Lame
Optimum
Legacy
Devel

## Types of Shells
- One way to connect to a compromised system is to use SSH or WinRM but this only works AFTER we're able to execute commands on the system first.
- Other method of accessing compromised systems is through shells. This is more reliable.
- The reason we even need to setup a shell is so we dont have to repeat the exploit every time we want to type a command on the compromised machine.

# Reverse Shell
- Quickest and easiest method of acquiring control over a compromised host. Once a vulnerability is identified, you can start a NetCat listener on your machine that listens to a specific port on your machine.
- With this listener in place, you can execute a reverse shell command that connects the remote host to our netcat listener.
- When the netcat listener realizes you've connected, it will open a shell.
- Needs you to setup a listening port using netcat.
<<<<<<< HEAD

=======
# Bind Shell
- 
>>>>>>> b604d769b35ac7a84c4f4f903077d720b3be7d1d
# Listening ports
- You can set netcat to listen to a specific port. For more info see cheatsheet.

# Connect Back IP
- To send a reverse connection we need our system's IP and port.
- Certain shell commands are more reliable than othgers.
- We can use the exploit we have over a remote host to execute one of these commands. (IE through python or a metasploit module) to get a reverse connection

<<<<<<< HEAD
# Reverse Shell Command
- The executed commands depend on what OS the compromised host runs on. A website called "Payload All The Things" has a comprehensive list of reverse shell commands which can be very useful.
- Once we do we should receive a connection through our netcat listener.
- A reverse shbell is very fragile. Once the reverse shell command is interrupted for any reason, we lose connection and you'd have to repeat the exploit.
- We can use the exploit over a remote host to execute reverse shell commands (IE through python or a metasploit module) to open the shell

# Bind Shell
- Another type of shell is a bind shell. This shell requires the host to connect to our listening port.
- Once a bind shell command is executed, the remote host will connect to you and youll be able to send it commands.
- You have to setup a listening port BEFORE executing the bind shell command.
- Make sure you specify the IP and port number you want the shell to connect to when executing the bind shell command.
- The shell will be waiting on that port for input from you.
=======
# Bind Shell
- A type of shell connection that is sent from the defender to the attacker.
- Requires a listening port to be setup on your machine before it can be performed.

# Upgrading TTY
- Once we connect a bind shell to us, or conenct to a reverse shell, some terminal features may not be available. (IE viewing command history by scrolling up or editing our commands w left and right arrows.)
- This is why we upgrade the TTY. This can be done by mapping the shell TTY to our own terminal's TTY.
- One way to do this is to use the python/stty method. 
- In our NC shell, type "python -c 'import pty; pty.spawn("/bin/bash")'". This will upgrade our TTY (keep in mind this is specific to bind shells)
- After this run CTRL+Z to get back to the local terminal and type this.

- 'stty raw -echo' stty is just a tool that lets you set the terminal configuration.
- The raw setting lets you set the terminal to NOT do any text processing.
- The -echo tells the terminal to output every character typed.
- 'fg' this is a built-in shell command that executes within the shell's process. All this command will do is put us back into the netcat session.

# Web Shells
- Typically a web scripting (usually PHP or ASPX) that accepts commands through HTTP request parameters such as GET or POST requests.
- This executes our command and prints the output back on our webpage.

# Writing a web Shell
- Typically a web shell is a one liner that can be memorized easily.
- a couple of examples

PHP: "<?php system($_REQUEST["cmd"]); ?>"
JSP: "<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>"
ASP: "<% eval request("cmd") %>"

- Once we have our web shell, we need to place it into the remote host's directory (Ideally webroot)
- This is usually done through a vulnerability in an upload feature which would allow us to write one of our shells to a file and then access the file to execute commands.
- If we have remote command excution already through an exploit, then we can write our shell directly into the webroot to access it over the internet.
- First you need to identify which webroot is used.
- Some default webroots for specific types of webservers.
Apache:	"/var/www/html/"
Nginx: "/usr/local/nginx/html/"
IIS: "c:\inetpub\wwwroot\"
XAMPP:	"C:\xampp\htdocs\"

we can use "echo '<script>' > <webroot_path>" to write the shell script into the webroot. The > essentially tells bash to write the script into the file of the path.

EX with an apache linux host.
"echo '<?php system($_REQUEST["cmd"]); ?>' > /var/www/html/shell.php"

# Accessing the web shell
- After creating the webscript we can access it through a browser by using CURL. For an apache php example we can visit the shell.php webpage

"curl http://SERVER_IP:PORT/shell.php?cmd=id".
This lets you execute the "id" command.

- The great thing about web shells is it bypasses any and all firewall restrictions.
- This is because it does not create any new port connections but just runs on web port 80 or 443.
- Its also great that if the compromised host is rebooted, then the web shell would still be in place and can still be freely accessed without having to exploit the remote host again(once the host is booted again.).
- Unfortunately web shells are not as interactive as reverse and bind shells since you have to re-request different URLs to execute commands. Still, in rare cases you can create a python script to automate this process and make the web shell a bit more interactive.

# Privelege Escalation
- Once we gain access to a box, we want to scout (enumerate) the box first to see if there's any internal vulnerabilities to achieve higher privelege level. (IE root or admin).

# PrivEsc Checklists.
- There are a ton of checklists and cheatsheets online for checks that can be ran for privesc enumeration.
- One example is HackTricks. Useful for both linux and windows local privEsc.
- Another one is PayloadAllTheThings on github for linux and windows.

# Enumeration Scripts.
- Many of the commands in PrivEsc checklists can be automatically ran with a script which will report any weaknesses.
- You can check a lot of things, which version of sudo used, outdated kernel, wether the folder you're in has write permissions and a bunch of other stuff.
- A couple example scripts for linux include LinEnum and linuxprevchecker on github.Seatbelt and JAWS are for windows.
- Another useful repository is SUITE PEASS.

## Keep in mind that running such scrips can easily trigger anti-virus software or other alarm bells. Manual enumeration may be preferable in many cases in the name of stealth.

# Kernel Exploits.
- Whenever we encounter an old server, the first thing we should look at is possible kernel vulnerabilities that may exist. If the server is poorly maintained without recent patches or updates, it is probably vulnerable to kernel exploits.
- Keep in mind that kernel exlpoits can cause serious instabilities so be very careful when running them on production systems. Only run them in a pen-testing scenario with explicit permission and coordination with the client (unless you wish to do a little trolling hehehehehe).

# Vulnerable Software.
- Use the command dpkg -l on linux or look at C:\Program Files on windows for any vulnerable (usually older) software. These can contain unpatched vulnerabilities.

# User priveleges
- We may not always be able to run the commands that we want as our default user. For that, we may want to escalate our user priveleges by gaining access to another user or by accessing root/system users. 
- The 3 most common methods for this are sudo, suid and Windows token privileges.

sudo is a program that lets you execute commands as a different user. It is used to allow lowever privelege users to execute commands without giving them root user access.

sudo -l gives you a list of priveleges.

sudo su lets you switch to another user.

sudo -u [user] lets you specify which user you want to run the command as.

GTFOBins is a list of unix-like executables that can be used to bypass local restrictions in misconfigured systems.
LOLBAS has a similar list of stuff but for windows.

# Scheduled Tasks
- In both linux and windows, we can run scripts at specific intervals (IE antivirus scan every 30 minutes or a backup script every 6 hours)
You can usually take advantage of these scheduled tasks (windows) or cron jobs (linux) in two main ways.
- Add a new scheduled task/cron job.
- Trick them into executing malicious software.
- The easiest way is to check if we are allowed to add a new scheduled task.
- There are a couple of files you could look at if you have write permissions.
/etc/crontab
/etc/cron.d
/var/spool/cron/crontabs/root

if we can write to such a directory called by a cronjob then we can write a bash script with a reverse shell command which will send us the shell.

# Exposed Credentials
- next we can look for files we can read to see if there's exposed credentials in them.
- This is common with configuration files or log files or history files. (bash_history in linux and PSReadLine in Windows).
- The enumeration scripts we discussed earlier usually looks for potential passwords in these spots and gives them to us.
- Also make sure to check for password reuse. Seriously.
- You can also use another person's SSH credentials.

# SSH Keys
- Usally SSH keys are in the .ssh directory. We may read their private ssh key in the /home/user/.ssh/id_rsa or /root/.ssh/id_rsa files.
- This can be used to log into servers. We can copy it to our machine and use the -i flag to login with it.
- Note that in the example, "chmod 600" is used after copying the file because if the ssh keys have lax permissions, then the server can prevent them from working.

- If we find that we may have write access to the ssh directory, then it can become possible to place your public key in there.
- This can allow you to ssh into the users machine whenever you want but this only really works if you already have full control over the machine since ssh will not accept keys written by other users.
- First create a new keypair with ssh-keygen and -f to specify output file.

- key.pub is the public key and key with no file extension is the private key. key.pub will need to be copied into the .ssh folder.
- The remote server should then allow you to login as that user.

## Transferring files 
During any pentesting exercise youll probably need to transfer files to the remote server. Stiff like enumeration scripts, exploits, or transfering data back to our attack host. Tools like metasploit agive you a metarpreter shell which lets you use the "Upload" command to upload a file, methods for transferring files into a reverse or ssh shell are very important still.

# using wget
wget is a tool for downloading stuff from the internet.

- One way to download/upload files is to run a python http server on our machine and then using wget and cURL to download file on the remote host.
- First we go to the directory with the file and startup an http server.
- Then we can run wget on our local host machine and select the file as the page in the domain/url.

# using SCP
SCP is a tool tat can let you download files over an ssh connection.
'scp <localfile> user@remotehost:/path/<localfile>'

# using base64
Some cases we are unable to transfer files. (IE remote host may have a firewall or smt)
In this type of situation we can use a trick to base64 encode the file. You can then paste the string on the remote server and decode it.

# hashing functions
Hash functions are very simple, file as input, and a unique string of text/number as output.
Options exist like md5sum or sha256sum. Both are good for this purpose but md5 is a bit outdated for cryptography.

# Starting out
Make sure to mix between exploratory and guided learning style. HTB academy follows guided and HTB main platform follows the exploratory style. Seriously. Do this.

# Resources.
# vulnerable machines/applications outside of HTB.
OWASP Juice Shop. 
- This is a modern vulnerable web app written in nodejs, express and angular
- It showcases the entirety of OWASP top ten vulnerabilities along with other security flaws.
- Probably slightly outdated.

Metasploitable 2
- A purposefelly vulnerable ubuntu linux mint VM that can be used to practice enumeration, automated and manual exploitation.

Metasploitable 3
- a template for building vulnerable windows VMs configured with a wide range of vulnerabilities.

DVWA
- Vulnerable php/mysql web app showcasing many comming web app vulnerabilities to varying degrees of difficulty.

# Youtube channels
Ippsec
- Provides in-depth walkthroughs of all retired HTB boxes chockfull of insight.

VbScrub 
- Provides HTB videos as well as videos on techniques. Focuses mainly on Active Directory Exploitation.

STOK
- Provides videos on various infosec related opics. focuses on bug bounteis and web application pen-testing.

LiveOverflow
- Provides videos on wide variety of technical infosec topics.


# Blogs
0xdf hacks stuff
- a great blog with tons of retired HTB box walkthroughs.
- Also has a "beyond root" section which covers some more unique aspects of the box that the author noticed.
- Also posts tons of techniques malware analysis and writeups from old CTF events.

# Beginner friendly HTB machines
- Lame
- Blue
- Nibbles
- Shocker
- Jerry

# Dante Prolab
- Dante prolab is an enterprise-style network geared towards players with some more experience. Check it out sometime.

