import re

def validate_password(password):
    if len(password) < 6:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[$#@]", password):
        return False

    return True

# Check password validity
username = input("Enter username: ")
password = input("Enter password: ")

if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")