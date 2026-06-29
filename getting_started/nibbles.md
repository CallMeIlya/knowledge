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

