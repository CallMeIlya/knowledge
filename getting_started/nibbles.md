## Notes on testing
# Black Box
you are given little to no information on a target. Just a company name. These tests are intended to act as an intruder but are far from comprehensive as vulnerabilities can be left undiscovered by the attacker. Thorough enumeration required from the attacker's POV.

# Grey Box
pentesters are given some information about the target. This could be a list of in-scope IP addresses/ranges or low level nework diagrams. This type of test can simulate what a malicious insider could do with low-level access. Less time is spent on enumeration and more time on exploitation.

# White Box
testers are given full access. A tester is provided with root-access, access to source code, build diagrams etc to look for logic vulnerabilities. and other flaws tha t are hard to see. This is a highly comprehensive test.

# Notes
IP: 10.129.200.170 
Ubuntu version: 4ubuntu2.2
# NMAP
Notable ports: 
- open port 22 running ssh openssh 7.2.p2
- open port 80 running apache httd 2.4.18
Notable directory enumeration

# common.txt
# error 403
- /.hta /.htapsswd /.htaccess /.server-statsu

# web-extensions.txt
/.php3 4 5 7 /.phps /.phptml /.htm /.html /.pht

Most likely an apache a php server.

A curl of the main page revealed a /nibbleblog page whcih returned a 200 on adnim, admin.php, content, plugins and README and index.php

# Plugins used
Readme revealed the following
PHP module DOM
PHP module SimpleXML
PHP moduke GD

Readme also revealed that setup of the server involved uploading files via FTP, perhaps I could upload a webshell into the apache webroot.

Notes end here. It is a bit incomplete because I got lost in the sauce a little bit.

# high-level summary of approaches and reflection
The manual approach involved firstly getting the username and password for the admin.php login page. (which was "addmin" "nibbles")

Getting admin meant enumerating /nibbleblog/content/private/user or something along those lines and the password was just a guess for nibbles. Bit silly but ok. Normal critical thinking deduction.

Once the admin panel is accessed, enumerating you may find that the "my-image" plugin has an upload section intended for images. You can upload a php reverse shell script through here and then run it by curling my_image in the content section (I think this is not exact).

After this, you're in.

Now your job is to find a way to gain root as the default user is nibbler. A quick sudo -l reveals that nibbler has the permission to run a script as root in their home directories personal/stuff/monitor.sh folder which you unzip.

Now this is useful because turns out monitor.sh is writable. You can add a reverse shell script into this monitor.sh and then run it as sudo to have root access. Now getting the flags is as simple as running cat in the home directory of nibbler and root.

The metasploit path for this exploit is almost the same except you create the payload using msfvenom. This payload is then uploaded using the same my_image upload prompt as before. Then you are dropped into a shell with the user nibbler. privelege escalation is the exact same as the previous path.

# Reflection
I needed a lot of help from the walkthrough. This was mainly because I did not enumerate carefully enough and kept missing details. I missed the admin username in the config file, I missed the nibbles password. I need to learn to stay focused during these boxes. There's always a way to exploit, you just havent found it yet. Which is okay.

From now on, try to enumerate VERY thoroughly and write down theories about the info you find all the time. 




