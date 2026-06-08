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


## SSH
- Use 'ssh user@host' to safely remotely access a computer. Very useful utility
## Netcat
- Allows you to grab the banner of a given service running on a port
- 'nc <host> <port>'
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
- 'nmap <flag> <ip>'
the -sC parameter of nmap lets you specify which script should be used to gain more detailed information.

-sV parameer instructs nmap to perform a version scan which lets nmap fingerprint the services on the traget system and identify their protocols, application names and version number. Version scan uses a massive databse of over 1000 service signatures, 

-p- tells nmap that you want to scan EVERY single port out of all 65535 ports.

-sV and -sC parameters increase how long the scan takes because it has to perform a ton more checks instead of performing only a TCP handshake

- The -sC parameter runs a ton of useful default scripts against the ports to gain more information about them.

version scans can also reveal which OS you are scanning if the version of the protocol mentions it.

The sV parameter will fingerprint the services on the target system and will acquire the protocol, the application name and the version.
It is very informative.

# Gobuster
'gobuster <dir/dns> <command options>
- the dir flag lets you switch between directory enum mode and dns enum mode.
- 'dir -u' lets you specify a url that you want to connect to.
- 'dir -w' lets you specify a wordlist for a dictionary attack.
- Theres many more flags that you can lookup by looking at the 'man' page.






