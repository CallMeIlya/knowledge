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




