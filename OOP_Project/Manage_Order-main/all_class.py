from datetime import datetime, date, timedelta

class WaterPark:
    def __init__(self, name):
        self.__name = name
        self.__stock = None
        self.__daily_stock = None
        self.__customer_list = []
        self.__member_list = []
        self.__promotion_list = []
        self.__payment_list = []
    
class Stock:
    def __init__(self):
        self.__cabana_list = []
        self.__locker_list = []
        self.__ticket_list = []
        self.__towel = None
        
    @property
    def cabana_list(self):
        return self.__cabana_list
    
    @property
    def locker_list(self):
        return self.__locker_list
    
    @property
    def ticket_list(self):
        return self.__ticket_list
    
    @property
    def towel(self):
        return self.__towel
    
class DailyStock(Stock):
    def __init__(self, date : date):
        super().__init__()
        self.__date = date
    
    @property
    def date(self):
        return self.__date
        
class Cabana:
    def __init__(self, id, size, zone, price = 0):
        self.__id = id
        self.__size = size
        self.__zone = zone
        self.__price = price
        self.__is_reserve = False
        
    @property
    def id(self):
        return self.__id
    
    @property
    def zone(self):
        return self.__zone
    
    @property
    def is_reserve(self):
        return self.__is_reserve
        
    @property    
    def price(self):
        cabana_price = {'S':899, 'M':1499, 'L':2499}
        
        for size, price in cabana_price.items():
            if self.__size == size:
                return price
        return 'Error' 
 
class Locker:
    def __init__(self, size, price, remaining_amount):
        self.__size = size
        self.__price = price
        self.__remaining_amount = remaining_amount
    
    @property
    def size(self):
        return self.__size
        
    @property
    def price(self):
        return self.__price
    
    @property
    def remaining_amount(self):
        return self.__remaining_amount
      
class Ticket:
    def __init__(self, type, amount_per_ticket, price = 0):
        self.__type = type
        self.__amount_per_ticket = amount_per_ticket
        self.__price = price
        self.__is_thai = True
    
    @property
    def price(self):
        if not(self.__is_thai) and self.__price != 0:
            return self.__price + 200                       
        else:
            return self.__price
        
    def update_is_thai(self):
        self.__is_thai = False

class Towel:
    def __init__(self):
        self.__price = 99
        self.__remaining_amount = 5000
        
    @property
    def price(self):
        return self.__price
    
    @property
    def remaining_amount(self):
        return self.__remaining_amount
        
class Promotion:
    def __init__(self, start_date: date, end_date: date):
        self.__start_date = start_date
        self.__end_date = end_date       
    
    def get_available_date(self):
        date_list = [self.__start_date + timedelta(days = x) for x in range((self.__end_date - self.__start_date).days + 1)]
        return date_list
    
class Coupon(Promotion):
    def __init__(self, code, discount, min_purchase, start_date, end_date):
        super().__init__(start_date, end_date)
        self.__code = code
        self.__discount = discount
        self.__min_purchase = min_purchase  # ยอดซื้อขั้นต่ำ
    
    @property
    def code(self):
        return self.__code
    
    @property
    def discount(self):
        return self.__discount
    
    @property
    def min_purchase(self):
        return self.__min_purchase    
    
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
        return self.__phone_no
    
    @property
    def booking_list(self):
        return self.__booking_list
        
class Member(Customer):
    def __init__(self, name, email, phone_number, birthday):
        super().__init__(name, email, phone_number)
        self.__birthday = birthday
        self.__password = None
        
    @property
    def password(self):
        return self.__password    
    
class Order:
    def __init__(self, visit_date: date):
        self.__visit_date = visit_date
        self.__order_detail = []
        self.__total = 0  
        self.__promotion = None
        
    @property
    def visit_date(self):
        return self.__visit_date
    
    @property
    def order_detail(self):
        return self.__order_detail
    
    @property
    def promotion(self):
        return self.__promotion
    
    @property
    def total(self):
        for item in self.__order_detail:
            self.__total += item.total_price
        return self.__total
    
class OrderDetail:
    def __init__(self, item, amount = 1):
        self.__item = item  # ใส่เป็น instance 
        self.__amount = amount
        self.__total_price = 0
        
    @property
    def item(self):
        return self.__item
    
    @property 
    def amount(self):
        return self.__amount
    
    @property
    def total_price(self):
        return self.__item.price * self.__amount 
    
class Booking:
    __ID = 1
    
    def __init__(self, customer, order, booking_date: date):
        self.__id = Booking.__ID
        self.__customer = customer
        self.__order = order
        self.__booking_date = booking_date
        self.__status = 'Unpaid'
        Booking.__ID += 1
        
    @property
    def id(self):
        return self.__id
    
    @property
    def customer(self):
        return self.__customer
    
    @property
    def order(self):
        return self.__order
    
    @property
    def booking_date(self):
        return self.__booking_date
    
    @property
    def status(self):
        return self.__status
    
    def update_status(self):
        pass
           
class Payment:
    def pay(self):
        return True
    
    def request_info():
        return None
    
class BankPayment(Payment):
    def __init__(self):
        self.__account_no = None   

class CardPayment(Payment) :
    def __init__(self):
        self.__card_no = None
        self.__card_pin = None 

class PaymentTransaction:
    ID = 1
    
    def __init__(self, booking, amount, payment_method: Payment, datetime : datetime): #
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method
        self.__create_datetime = datetime
        self.__transaction_id = PaymentTransaction.__ID
        self.__status = False
        PaymentTransaction.ID += 1