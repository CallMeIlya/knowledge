## Structure of InfoSec

# Areas of Informational Security
- The three key aspects that security specialist must insure is the:
- These are very general assets but still important.
Security of data
Availability of data
Integrity of data

The actual umbrella of infosec threats is much more extensive but some example threats are as follows.

Network Security
Application Security
Operational Security
Disaster Recovery and Business Continuity
Cloud Security
Physical Security
Mobile Security
Internet of Things (IoT) Security

- It all essentially comes down to risk management 
Measuring the severity of a threat by looking at how much damage the event would do and how likely it is to happen (usually). 
- Risk is a bit broader that encapsulates both threats and vulnerabilities and involves identifying and applying measures for mitigation.

- A threat is a potential cause of harm to the system or organization. (IE person, hacker group or natural event such as a fire)

- Vulnerability is a wekaness in a system that could be exploited by a threat. (Bugs, misconfigs weak passwords etc). The presence of a vulnerability does not necessarily mean the system is compromised. A credible threat must also exist in combination that can exploit the vulnerability.

## Roles in InfoSec.
- Chief Infosec officer.
oversees entire informational security program. Sets the overall strat that pentesters will evaluate.
- Security Architect
designs secure systems and networks. Creates systems the pentesters will try to breach.
- Pen-tester
Finds vulnerabilities through simulated attacks. Actively looks for exploits and vulnerabilities (legally and ethically).
- Incident Response Specialist.
Manages and responds to security incidents. Works with pen-testers by responding to their attacks and collaborating with them afterwards.
- Security Analyst
Monitors systems for threats and analyzes security data. Sometimes uses pentest results to improve monitoring.
- Compliance Specialist
Makes sure people adhere to the security standards and regulations. Pen test reports often support complicance efforts.

# Principles of InfoSec
- Confidentiality, data protected against unauthorized viewing
Impletented through encryption and access control.
- Integrity, data protected against unauthorized changes
Implemented through hashes and digital signatures.
- Availability, data protected against disruption of access
Implemented through disaster recovery plans and redundancy.
- Non-repudiation, Ensures party cannot DENY that the data belongs to them (IE, signature)
Implemented through digital signatures and audit logs.
- Authentication, verifies identity of user or device
Implemented through passwords, biomatrics MFA etc.
- Privacy, Focused on proper handling of personal information
Implemented through data minization and consent management.

# Processes of InfoSec
- Risk Assessment
Evaluates potential threats and vulnerabilities.
- Security Planning
Develops strategies to identify risks.
- Implementation of Security controls
Involves deploying technical solutions and enforcing policies.
- Monitoring and Detection
Watches for security events and anomalies (uses tools like SIEM systems and intrusion detection systems).
- Incident Response
Reacts to detected incidents. Follows procedures to mitigate threats.
- Disaster Recovery
Focuses on restoring systems and data post-incident.
- Continous Improvement
Reviews and learns from past incidents and/or near misses.

# Tools in InfoSec
- Firewalls
Control incoming network traffic. Acts as a barrier between internal networks and untrusted external networks based on pre-determined rules.
- Intrusion Detection/Prevention Systems (IDS/IPS)
Monitor and block sus activity (amoogus). Takes automated actions based off of suspicious activities detected on the network.
- VPNs
Provides secure connections over public networks ensuring integrity and privacy during transmission.
- Security Information and Event Management (SIEM) Systems
Collect and analyze security event data
- Vulnerability scanners
IDentify weaknesses in systems and apps.
- Pen testing tools
Simulate attacks to find vulnerabilities (Metasploit, Burp Suite)
- Encryption Tools
Protect data integrity and confidentiality. Protects sensitive data in transit and at rest. Renders it unreadable to unathorized parties.
- Access Control Systems
Manage user permissions and authentication. Inclues measures for authentication protocols and tries to make sure only legitimate users can access the network.
- Security awareness training platforms
Educate users about best security practices.

# Network Security
Security of networks lol. (As in the communication lines between specific computers.

# Application Security
The purpose of application security is to makes sure that apps are developed taking into account the CIA Triad
## CIA Triad.
The CIA Triad (Confidentiality, Integrity, Availability).

Application security continues through the ENTIRE lifecycle of an app.
Developers play a huge role in Application Security in the sense that they need to make sure they write code that is not vulnerable to common vulnerabilities. IE XSS (cross site scripting), SQL Injection and Buffer Overflows.

## Metaphor time!!
1. Building the house.

- Locks on doors and windows (Authentication)
When you create an app, you need to make sure only the right people can get in (authentication), like how a house needs good locks to keep strangers out.
- Strong walls and materials (Vulnerabilities)
The app's code should be solid and free from weaknesses that hackers could exploit, just like you would build a house with strong materials to prevent it from collapsing.
- Waterproof roof (Encryption)
Encrypting data means protecting sensitive information, like making sure your house’s roof doesn’t leak during rain. This ensures no one can read or steal your data while it's being transferred.

2. Inspect the house
- Test if locks are working
This is like testing an app to see if hackers can break in by trying different methods (penetration testing).
- Look for cracks in walls 
Just as you’d inspect a house for any cracks, developers need to check their app’s code for bugs or weak spots that could be used by attackers.
- Test roof with water
After you’ve built the app, you need to make sure sensitive data stays protected, just like testing a roof to ensure it doesn't leak during a storm.

3. Keep the House Safe Over Time (Ongoing Security Monitoring)
- Install security cameras
Even after building and testing your app, you must monitor it regularly to catch any new threats or problems, just like using security cameras to watch for intruders.
- Fix cracks and replace broken locks
Apps need regular updates to fix vulnerabilities or bugs, just like how you would repair cracks or replace broken locks to keep a house safe.

- A security test or check goes wrong if a specialist skips cehcking a lock, wether due to incompetence or complacency.

## Security by Design
- This means that security isn't something you think about later, it is kept in mind from start to finish.
- Security Does not stop at an apps code but also literally everything else (IE social engineering, ecosystem, hardware)

## Threat Modelling
Imagining how people could possibly break into your house. Threatmodelling helps developers figure out risks and vulnerabilities early on.
## Secure Code Reviews
After writing code devs check and probe it for weakspots.
## Servers and Databases
These are important lol. If these arent secure you're basically fucked.

# Application Security Responsibility
- Application Developers (Write secure code and implementing features)
- Security Architects (Design a structure for the app that's secure)
- IT Operations (These teams are responsible for maintaining security of the production environment).

