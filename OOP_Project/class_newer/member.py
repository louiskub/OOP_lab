from booking import Booking
from order import Order
from email_validator import validate_email, EmailNotValidError
import re

# class Customer:
#     def __init__(self, name, email, phone_no):
#         self.__name = name
#         self.__email = email
#         self.__phone_no = phone_no
#         self.__booking_list = []
    
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def email(self):
#         return self.__email
#     @property
#     def phone_no(self):
#         return self.__phone_no
#     @property
#     def booking_list(self):
#         return self.__booking_list
    
#     def check_email(email):
#         try:
#             validate_email(email)
#             return True
#         except EmailNotValidError:
#             return False
        
#     def check_phone_number(phone_number): 
#         pattern = re.compile(r'^0\d*$')  # Starts with '0' and followed by any number of digits
#         is_valid_phone_no = bool(pattern.match(phone_number))
#         return is_valid_phone_no            

class Member:

    __ID = 100000

    def __init__(self, name, email, phone_no: str, birthday, password):
        self.__name = name
        self.__email = email
        self.__id = Member.__ID
        self.__birthday = birthday
        self.__password = password
        self.__phone_no = phone_no
        self.__order = None
        self.__booking_temp = None
        self.__booking_list = []
        Member.__ID += 1

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def phone_no(self):
        return self.__phone_no
    
    @property
    def booking_list(self):
        return self.__booking_list  

    @property
    def order(self):
        return self.__order 
    
    @property
    def booking_temp(self):
        return self.__booking_temp

    @order.setter
    def order(self, order):
        self.__order = order
    
    @booking_temp.setter
    def booking_temp(self, booking: Booking):
        self.__booking_temp = booking

    # Check member info before become member.
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
    
    def check_password(password):
        for char in password:
            if char.isnumeric() or char.isalpha() or char == '.' or char == '_':
                continue
            return False
        return True
    
    # Verify member identity when login.
    def verify_member(self, email, password):
        if email == self.email and password == self.__password:
            return self  
    
    def get_order_from_visit_date(self, date):
        if self.__order != None and date == self.__order.visit_date:
            return self.__order
        order = Order(date)
        self.__order = order
        return order

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
    
    def to_dict(self):
        return {
            "id": self.__id,
            "name": self.__name,
            "email": self.__email,
            "birthday": self.__birthday, 
            "phone_no": self.__phone_no,
            "booking_list": [ booking.to_dict() for booking in self.__booking_list ]
        }