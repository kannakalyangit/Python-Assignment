# import necessary libraries, RE is used for regex
import re

def check_password_strength(pwd):
    # Checking the length of the password
    if len(pwd) < 8:
        return False
    # Check if there are uppercase letters
    if not re.search(r"[A-Z]", pwd):
        return False
    # Check if there are lowercase letters
    if not re.search(r"[a-z]", pwd):
        return False
    # Check if there are digits
    if not re.search(r"[0-9]", pwd):
        return False
    # Check if there are special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        return False
    return True

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    if check_password_strength(pwd):
        print("Strong password.")
    else:
        print("Weak password. Please include uppercase, lowercase, digit, special character, and minimum 8 characters.")