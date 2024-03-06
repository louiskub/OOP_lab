from booking import Booking
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import re

class Customer:
    def __init__(self, name, email, phone_no):
        self.__name = name
        self.__email = email
        self.__phone_no = phone_no
        self.__booking_list = []
    
    @property
    def name(self):
        return self.__name
    @property
    def email(self):
        return self.__email
    @property
    def phone_no(self):
        return self.__email
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
    def __init__(self, name, email, phone_number, birthday, password):
        super().__init__(name, email, phone_number)
        self.__id = 0
        self.__birthday = birthday
        self.__point = 0
        self.__password = password
    @property
    def id(self):
        return self.__id
    
    def add_booking(self, booking: Booking):
        if not isinstance(booking, Booking):
            return None
        self.__booking_list.append(booking)
        return "Done"
    def remove_booking(self, booking: Booking):
        if not isinstance(booking, Booking):
            return None
        self.__booking_list.remove(booking)
        return "Done"
    
    def check_password(password):
        for char in password:
            if char.isnumeric() or char.isalpha() or char == '.' or char == '_':
                continue
            return False
        return True
    
    def verify_member(self, email, password):
        if email == self.email and password == self.__password:
            return self
