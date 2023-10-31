
#online passcode checker

import re

def check_password_validity(password):
    if (6 <= len(password) <= 12 and
        re.search("[a-z]", password) and
        re.search("[0-9]", password) and
        re.search("[A-Z]", password) and
        re.search("[$#@_&%]", password)):
        return True
    else:
        return False


password = input("Enter your password: ")
if check_password_validity(password):
    print("Valid password!")
else:
    print("Invalid password!")
