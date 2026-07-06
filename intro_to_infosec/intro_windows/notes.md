# a bit of history.
- windows was first introduced on november 20th in 1985.
- windows was originally designed to be a graphical OS shell for MS-DOS and later versions of windows introduced file manager, program manager and print manager programs.
- Windows 95 was the first full integration of windows and DOS. It also offered built-in internet support for the first time.
- Windows also has server versions (windows server XXXX)
- Windows Server 2008 and 2012 are at the end of their lifecycle and no longer receive security updates since anuary 14 2020.
- Only server 2012 and 2008 are in support but microsoft has released patches for earlier versions of windows within the past few years due to the discovery of the Eternal Blue (SMBv1) security vulnerability.

- Many windows versions are deemed "legacy" and are no longer supported however many organizations often find themselves still running them. 
- This is to keep critical systems online or due to monetary concerns.

- A pentester needs to understand the differences between versions and the various misconfigurations and vulnerabilities inherent to each.

## Windows versions and their numbers

- Windows XP has a version unmber of 5.1
- Windows Vista server has a version number of 6.0

For a more expansive list see non-tool cheatsheets.

- 'Get-WmiObject' cmdlet can give you more information on the specifics of the windows machine. More specifically the win32_OperatingSystem class.

# Local Access to windows
- usually done through peripherals but you knew this lol
# Remote Acces to windows
- Entire industries are built around remote access (Think MSP and MSSP)
The most common remote access technologies include the following.
- VPN (Virtual Private Network)
- SSH (Secure SHell)
- FTP (File Transfer Protocol)
- VNC (Virtual Network Computing)
- WinRM (Powershell Remoting/Windows Remote Management) (WinRM)
- RDP (Remote Desktop Protocol)

# RDP protocol
- Uses client-server architecture 
- Client side app is used to specify a target IP address over a network on which RDP is enabled.
- The target computer (on which RDP is enabled) is considered the server
- Runs on port 3389.
- See "getting_started" for more info.
- The app for creating RDP connections is mstc.exe. Remote access however must already be allowed for this to work.

As a pentester, you may benefit from looking for .rdp files. (Files that save an RDP connection profile for specific users. Its quite nice.

# xfreerdp
- From a linux attack host we may benefit from the xfreerdp tool which can help you remotely access windows targets.

# OS Structure
- Root folder of windows of a given drive is usually <Drive_Letter>:\<Drive_(usually_CDrive>
- Other drives are assigned other letters both virtual and non-virtual.
- Other folders look as follows.

Perflogs 
- Can hold windows performance logs but is empty by default.

Program Files
- On 32-bit systems, all 16-bit and 32-bit programs are installed here.
- On 64-bit systems, only 64 bit programs are installed here.
Program Files (x86)
- 32 and 16 bit programs are installed here on 64 bit editions of windows.
ProgramData
- Hidden folder that is essential for specific programs to run. This data is accessible by the program no matter which user is running it.
Users
- This folder contains user profiles that logs onto the system. Contains the default and public folders.
Default
- This contains the default user porile template for all created users. Whenever a new user is added, their profile is based on this profile.

Public
- This folder is intended for computer users to share files and is accessible to all users by default.

AppData
- Per user application data and settings are stored in a hidden subfolder of this folder (IE cliff.more/AppData). 
- Each of these folders contains 3 subfolders. 
- Roaming folder contains machine independant data that should be according to the users profile such as custom directories and such.
- Local folder is specific to the computer itself and is never synchronized across the network.
- LocalLow is similar to the local folder but has a lower data integrity level.
- It can therefore be used by web browsers to set protected and safe modes for example.

Windows
- Contains the majority of files required for windows OS are stored here.

System, System32 and SysWOW64
- Contains all the DLLs required for the core features of windows and the Windows API.
- The OS searches these folders any time a program asks to load a DLL without specifying an absolute path.

WinSxS
- The Windows Component Store contains a copy of all windows components, updates and service packs.

# Exploring directories using the CLI.
- We do this using the 'dir' command.
- or the 'tree' command.

# File Systems.
there are 5 main types of windows file systems. FAT12, FAT16, FAT32, NTFS and exFAT.
# FAT32 
- Is compatible with a lot of different devices (tablets, cameras, consoles etc).
- Compatible with all windows OS's starting windows 95. Also supported on linux and macos.
- Can only be used with files less than 4GB.
- No built in data compression or protection features.
- Must use 3rd party tools for encryption.
# NTFS
- Very reliable and can restore the consistency of files in its system in case of a system failure or power loss.
- Lets you set very granular permissions on files.
- Supports large partitions.
- Has journaling built-in meaning that file modifications are logged.
- Most mobile devices dont support NTFS natively.
- Older devices such as TVs and digital cameras dont offer support for NTFS storage devices.

# Permissions of NTFS file systems.
- Full Control
Reading, writing, changing and deleting of files and folders
- Modify
Reading, writing, deleting files and folders
- List folder contents
Viewing, listing folders and subfolders, executing files. 
Files and subfolders inherit the permission
- Read and execute
Viewing, listing files and subfolders, executing files.
files and subfolders inherit the permission
- Write
Allows for adding files to a folder and subfolders, and writing to a file.
- Read
Allows for viewing and listing
- Traverse Folder
Allows or denies ability to move through folders to reach other files or folders. j

# Integrity Control Access Control List (ICACLS)
Permissions can be managed through file explorer security tab.
The icacls utility can be used to have more granular control over ntfs files.


