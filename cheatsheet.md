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

## Get command
- lets you download files from remotely accessed devices.

## SNMP
- 'snmpwalk <version> <public/private> <ip>'
- Lets you gather some information about a network management device.

# onesixtyone
- 'onesixtyone -c <dictionary> <ip>' lets you brute force community strings for networks.
