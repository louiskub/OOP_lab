import requests
import json
from datetime import datetime, date, time
from products import Cabana, Locker, Ticket
from products import create_cabana


# a = requests.get("http://127.0.0.1:8000/services")
# print(a.json())

# date1 = date(2024, 2, 1)
# b = requests.get("http://127.0.0.1:8000/services/{date1}", data = json.dumps(str(date1)))
# print(b.json())

# detail = {'Email':'sirima@gmail.com', 'Phone number':'0918242283', 'Birthday':str(date(2005, 3, 26)), 'Password':'sirima123456'}
# r = requests.post("http://127.0.0.1:8000/subscription", data = json.dumps('sirima', detail))
# print(r.json())
# print(detail['Email'])


from email_validator import validate_email, EmailNotValidError

email = "example@23.com"

def check(email):
    is_valid = bool(validate_email(email))
    return is_valid
    
print(check(email))
       

    
# from email_validator import validate_email, EmailNotValidError

# email = "example@example.com" # อีเมล

# try:
#     v = validate_email(email) # validate and get info
#     email = v["email"] # replace with normalized form
# except EmailNotValidError as e:
#     # email is not valid, exception message is human-readable
#     print(str(e))

# import re

# def is_valid_phone_number(phone_number):
#     # Define the expected format using a regex pattern
#     pattern = re.compile(r'^0\d*$')  # Starts with '0' and followed by any number of digits

#     # Check if the phone number matches the pattern
#     is_valid = bool(pattern.match(phone_number))

#     return is_valid

# # Example usage
# phone_number_to_check = "918242283"
# result = is_valid_phone_number(phone_number_to_check)

# if result:
#     print(f"The phone number {phone_number_to_check} is in the correct format.")
# else:
#     print(f"The phone number {phone_number_to_check} is not in the correct format.")
