# Password Cracker Tool

## Description
The **Password Cracker** is a Python-based tool designed to test the strength of passwords by performing dictionary-based or brute-force attacks. The tool supports various protocols such as SSH, FTP, HTTP Basic Authentication, and SMTP, making it ideal for penetration testing and security auditing purposes.

> **Disclaimer**: This tool is intended for educational purposes and authorized security testing only. Unauthorized use may violate laws and regulations.

---

## Features
- **Configurable Dictionaries**: Use custom wordlists for password testing.
- **Brute Force Support**: Generate passwords dynamically for exhaustive testing.
- **Multi-Protocol Support**:
  - SSH (via `paramiko`)
  - FTP (via `ftplib`)
  - HTTP Basic Authentication (via `requests`)
  - SMTP (via `smtplib`)
- **Interactive Menu**: User-friendly interface to select protocols and attack methods.
- **Modular Design**: Extendable to add more protocols or attack types.

---

## Requirements
- Python 3.8 or higher
- Install the required Python dependencies:
  ```bash
  pip install paramiko requests
  ```

---

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/diegomessiah/password-cracker-tool.git
   cd password-cracker
   ```

2. Run the tool:
   ```bash
   python password_cracker_extended.py
   ```

3. Follow the interactive menu:
   - Select the protocol (e.g., SSH, FTP, HTTP, SMTP).
   - Choose between dictionary-based or brute-force attacks.
   - Provide the necessary information (e.g., hostname, username, dictionary path).

---

## Examples
### SSH Dictionary Attack
```plaintext
Enter hostname or IP address: 192.168.1.10
Enter SSH username: admin
Enter path to dictionary file: passwords.txt
```

### FTP Brute Force Attack
```plaintext
Enter hostname or IP address: 192.168.1.20
Enter FTP username: anonymous
Enter maximum password length: 4
```

---

## Customization
- **Adding Protocols**: Extend the tool by implementing new methods for unsupported protocols.
- **Custom Wordlists**: Use your own `.txt` files containing passwords for dictionary-based attacks.

---

## Warning
This tool should only be used with explicit permission from the owner of the system being tested. Unauthorized usage is illegal and unethical. Always ensure you have proper authorization before running this tool.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue for improvements or bug fixes.

---

## Author
**Diego Messiah**
- GitHub: [diegomessiah](https://github.com/diegomessiah)
