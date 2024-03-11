from email_validator import validate_email, EmailNotValidError
import re

class Customer:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__booking_list = []
        
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @property
    def booking_list(self):
        return self.__booking_list
    
    def check_email(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False
        
    def check_phone_number(phone_number): 
        pattern = re.compile(r'^0\d*$')  # Starts with '0' and followed by any number of digits
        is_valid_phone_no = bool(pattern.match(phone_number))
        return is_valid_phone_no                  
        
class Member(Customer):
    __ID = 1
    def __init__(self, name, email, phone_number, birthday, password):
        super().__init__(name, email, phone_number)
        self.__id = Member.__ID
        self.__birthday = birthday
        self.__point = 0
        self.__password = password
        self.__points_history_list = []
        self.__reward_history_list = []
        Member.__ID += 1
    
    @property
    def id(self):
        return self.__id
    
    def check_password(password):
        for char in password:
            if char.isnumeric() or char.isalpha() or char == '.' or char == '_':
                continue
            return False
        return True
    
email = 'sirima@090.com'
phone = '01234890'
password = '57637'
# print(Member.check_email(email))
# print(Member.check_phone_number(phone))
# print(Member.check_password(password))