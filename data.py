catalog = [
    {
        "id": 1,
        "name": "SQL Injection",
        "category": "Web/Application Vulnerability",
        "description": "Attackers insert malicious SQL query requests through an input field to manipulate a database query.",
        "mitigation": "Use parameterized queries / prepared statements instead of string concatenation.",
        "objective": "2.3",
        "Simulation": True
    },
    {
        "id": 2,
        "name": "XSS",
        "category": "Web Vulnerability",
        "description": "Attackers inject malicious scripts into a trusted website to exploit vulnerabilities in the user's browser.",
        "mitigation": "Sanitize user inputs and escape output.",
        "objective": "2.3",
        "Simulation": True
    },
    {
        "id": 3,
        "name": "Race Condition",
        "category": "Application Vulnerability",
        "description": "A flaw in the timing of a program's execution that produces unexpected results, often leading to security vulnerabilities.",
        "mitigation": "Implement proper synchronization mechanisms and avoid shared mutable state.",
        "objective": "2.3"
    },
    {
        "id": 4,
        "name": "Buffer Overflow",
        "category": "Application Vulnerability",
        "description": "Occurs when a program writes more data to a buffer of memory that it can hold, leading to adjacent memory being overwritten.",
        "mitigation": "Use safe string handling functions and implement bounds checking.",
        "objective": "2.3"
    },
    {
        "id": 5,
        "name": "Weak Encryption",
        "category": "Cryptography Vulnerability",
        "description": "Using outdated or weak encryption algorithms that can be easily broken by attackers.",
        "mitigation": "Use strong, modern encryption algorithms and regularly update cryptographic libraries.",
        "objective": "2.3"
    },
    {
        "id": 6,
        "name": "Ransomware",
        "category": "Malware",
        "description": "A type of malicious software that encrypts a victim's files and demands payment for the decryption key.",
        "mitigation": "Regularly back up data, keep software updated, and educate users about phishing attacks.",
        "objective": "2.4",
        "Simulation": True
    },
    {
        "id": 7,
        "name": "Spyware/Keylogger",
        "category": "Malware",
        "description": "Malware that secretly monitors and records user activity, often capturing sensitive information like passwords.",
        "mitigation": "Use reputable antivirus software, keep systems updated, and avoid downloading software from untrusted sources.",
        "objective": "2.4"
    },
    {
        "id": 8,
        "name": "Logic Bomb",
        "category": "Malware",
        "description": "A malicious piece of code that is triggered by specific conditions or events, causing harm to the system.",
        "mitigation": "Implement code reviews, monitor system behavior, and use intrusion detection systems.",
        "objective": "2.4"
    },
    {
        "id": 9,
        "name": "Watering Hole Attack",
        "category": "Social Engineering",
        "description": "Attackers compromise a website that is frequently visited by the target group, infecting it with malware to gain access to their systems.",
        "mitigation": "Keep software updated, use web filtering, and educate users about the risks of visiting untrusted websites.",
        "objective": "2.2"
    }, 
    {
        "id": 10,
        "name": "Phishing",
        "category": "Social Engineering",
        "description": "Attackers impersonate a trusted entity to trick victims into revealing sensitive information, such as login credentials or financial information.",
        "mitigation": "Educate users about phishing tactics, implement email filtering, and use multi-factor authentication.",
        "objective": "2.2"
    },
    {
        "id": 11,
        "name": " Denial of Service (DoS)",
        "category": "Network Vulnerability",
        "description": "An attack that overwhelms a system, network, or service with excessive traffic, rendering it unavailable to legitimate users.",
        "mitigation": "Implement rate limiting, use firewalls and intrusion detection systems, and have a response plan in place.",
        "objective": "2.4"
    },
    {
        "id": 12,
        "name": "Replay Attack",
        "category": "Network Vulnerability",
        "description": "An attack where valid data transmission is maliciously or fraudulently repeated or delayed, often to gain unauthorized access.",
        "mitigation": "Use timestamps, nonces, and secure session management to prevent replay attacks.",
        "objective": "2.4"
    },
    {
        "id": 13,
        "name": "Man-in-the-Middle (MitM) Attack",
        "category": "Network Vulnerability",
        "description": "An attack where an attacker intercepts communication between two parties, allowing them to eavesdrop or modify the data being transmitted.",
        "mitigation": "Use encryption, implement certificate validation, and employ secure communication protocols.",
        "objective": "2.4"
    },
    {
        "id": 14,
        "name": "Unsecured Networks",
        "category": "Network Vulnerability",
        "description": "Using networks that lack proper security measures, making it easier for attackers to intercept data or gain unauthorized access.",
        "mitigation": "Use secure Wi-Fi networks, implement VPNs, and avoid using public networks for sensitive transactions.",
        "objective": "2.2"
    },
    {
        "id": 15,
        "name": "Default Credentials",
        "category": "Configuration Vulnerability",  
        "description": "Using default usernames and passwords that come with software or hardware, which are often publicly known and easily exploitable.",
        "mitigation": "Change default usernames and passwords immediately upon installation, and enforce strong password policies.",
        "objective": "2.2",
        "Simulation": True
    }
]