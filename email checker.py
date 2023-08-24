import re

email_address = input('Enter your email address: ')

if re.search(r'^.*@(.\w*)\.(.\w*)', email_address) == None:
    print("INVALID")
else:
    print("OK")