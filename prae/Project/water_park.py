from datetime import datetime

class WaterPark:
    def __init__(self, name):
        self.__name = name
        self.__customer_list = []
        self.__member_list = []
        self.__booking_list = []
        self.__promotion_list = []
        self.__daily_stock = []
    
    @property
    def booking_list(self):
        return self.__booking_list
        
    def add_booking(self, booking):
        if isinstance(booking, booking) and booking.status == True:
            self.__booking_list.append(booking)
        else: return "Error"
        
    def add_promotion(self, promotion):
        if isinstance(promotion, Promotion):
            self.__promotion_list.append(promotion)
        else: return "Error"
        
    def add_shop(self, shop):
        if isinstance(shop, Shop):
            self.__shop = shop
        else: return "Error"
        
    def search_customer_from_email(self, customer_email):
        for booking in self.__booking_list:
            if customer_email == booking.transaction.customer.email:
                return booking.transaction.customer
            
    def search_booking_from_date(self, target_date):
        booking_list = []
        for booking in self.__booking_list:
            if booking.order_date.date() == target_date:
                booking_list.append(booking)
        return booking_list

class WaterParkAccount:
    pass

class Ticket:
    def __init__(self, is_thai, main_type, sub_type, price):
        self.__is_thai = is_thai
        self.__main_type = main_type # solo or group
        self.__sub_type = sub_type # sub in main type
        self.__price = price
        self.__feature = None
    
    @property    
    def price(self):
        pass
        
class Customer:
    def __init__(self, name, email, phone_number, visit_date):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__visit_date = visit_date
        
    @property
    def email(self):
        return self.__email

class Member(Customer): 
    
    __discount = 0.05
    
    def __init__(self, name, email, phone_number, birthday_date, nationality, isinThailand = False):
        Customer.__init__(self, name, email, phone_number) 
        self.__bithday_date = birthday_date
        self.__nationality = nationality
        self.__isinThailand = isinThailand
        self.__transaction_list = []
           
class Shop:
    def __init__(self):
        self.__ticket_list = []
        self.__cabana_list = []
        self.__locker_list = []
        self.__amount_of_locker = [50, 10]
        self.__amount_of_towel = 5000
    
    def add_cabana(self, cabana):
        if isinstance(cabana, Cabana):
            self.__cabana_list.append(cabana)
        else: return 'Error'    
        
    def add_locker(self, locker):
        if isinstance(locker, Locker):
            self.__locker_list.append(locker)
        else: return 'Error'  
        
    def show_ticket(self, water_park, target_date):
        pass
    
    def show_cabana(self, water_park, target_date): # show available cabana
        cabana_list = self.__cabana_list
        booking_list = water_park.search_booking_from_date(target_date)
        for booking in booking_list:
            if booking.transaction.cabana in cabana_list:
                cabana_list.remove(booking.transaction.cabana)
        return cabana_list        
    
    def show_locker(self, water_park, target_date):
        locker_list = self.__locker_list
        booking_list = water_park.search_booking_from_date(target_date) 
    
    def show_towel(self, water_park, target_date):
        pass        
       
    def choose_product(self, water_park, target_date, customer): # create transaction
        product_list = []
        #trans = Transaction(customer, 0, target_date)
        available_cabana = self.show_cabana(water_park, target_date)
        selected_cabana = available_cabana[0]
        #trans.add_cabana(selected_cabana)
        product_list.append(selected_cabana)
        return product_list
    
    def cal_total(self, product_list):
        total = 0
        for product in product_list:
            total += product.price
        return total        
    
    def create_transaction(self, product_list, customer, target_date):
        trans = Transaction(customer, self.cal_total(product_list), target_date)
        for product in product_list:
            if isinstance(product, Cabana):
                trans.add_cabana(product)
        return trans
                       
class Cabana:
    def __init__(self, id, size, zone):
        self.__id = id
        self.__size = size # normal(N), medium(M), large(L)
        self.__zone = zone
        self.__price = 0
    
    @property    
    def price(self):
        # normal_price = 899
        # medium_price = 1499
        # large_price = 2499
        cabana_price = [899, 1499, 2499]
        cabana_size = ['N', 'M', 'L']
        
        for i in range(3):
            if self.__size == cabana_size[i]:
                return cabana_price[i]
        return 'Error'        
 
class ShowCabana(Cabana):
    
    __normal_size_price = 899
    __medium_size_price = 1499
    __large_size_price = 2499
    
    def __init__(self, id, size, zone, price = 0):
        Cabana.__init__(self, id, size, zone)
        self.__price = price
        self.__is_reserve = False
        
class Locker:
    def __init__(self, size):
        self.__size = size
        self.__price = 0
        
    @property
    def price(self):
        # locker_medium_price = 149
	    # locker_large_price = 229
        locker_price = [149, 229]
        locker_size = ['M', 'L']
        
        for i in range(2):
            if self.__size == locker_size[i]:
                return locker_price[i]
        return 'Error'    
 
class ShowLocker(Locker):
    
    __medium_size_price = 149
    __large_size_price = 229
    
    def __init__(self, id, size, price = 0):
        Locker.__init__(self, id, size)
        self.__price = price
        self.__is_reserve = False
        
class Promotion:
    def __init__(self, start_date, end_date, discount):
        self.__start_date = start_date
        self.__end_date = end_date
        self.__discount = discount
        
    def add_feature(self):
        pass

class Transaction:
    def __init__(self, customer, total, coupon = None):
        self.__customer = customer
        #self.__detail = detail # detail = [[cabana, 1], [locker, 2]]
        self.__total = total
        self.__coupon = coupon
        self.__cabana = None # instance of cabana
        self.__locker_amount_list = [] # index 0 = medium, 1 = large
        self.__ticket_amount_list = [] 
        self.__towel_amount = 0
        
    @property
    def customer(self):
        return self.__customer
    
    @property
    def cabana(self):
        return self.__cabana
    
    @property
    def ticket_amount_list(self):
        return self.__ticket_amount_list
    
    @property
    def locker_amount_list(self):
        return self.__locker_amount_list
    
    @property
    def towel_amount(self):
        return self.__towel_amount
    
    @property
    def total(self):
        return self.__total    
    
    def add_cabana(self, cabana):
        if isinstance(cabana, Cabana):
            self.__cabana = cabana
        else:
            return 'Error'
    
    
class Booking:
    def __init__(self, id, transaction, order_date):
        self.__id = id
        self.__transaction = transaction
        self.__order_date = order_date
        self.__qrcode = None
        self.__status = False
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        if status == True or status == False:
            self.__status = status
        else: return 'Error'
        
    @property
    def id(self):
        return self.__id
    
    @property
    def transaction(self):
        return self.__transaction
    
    @property
    def order_date(self):
        return self.__order_date
        
    def generate_qrcode(self):
        pass          
    
class Payment:
    def generate_payment(self, water_park, transaction, alternative):
        ispaid = False
        count = 1000
        booking = booking(f"{count}", transaction, datetime.now())
        ### Do something ###
        ispaid = True
        if ispaid == True:
            booking.status = True
            water_park.add_booking(booking)   
            count += 1
            return 'Success'
        else: return 'Error'         
    
    def paid(self, amounts):
        pass       
    
# class Slides:
#     def __init__(self, type, feature):
#         pass
    
dkub = WaterPark('Dkub')
dkub_shop = Shop()
payment = Payment()
K_mam = Customer('Mam', 'mam@gmail.com', '09311234567', datetime.now().date())
K_malee = Customer('Malee', 'malee@gmail.com', '0849876543', datetime.now().date())

n14 = Cabana('N14', 'N', 'Family')
m15 = Cabana('M15', 'M', 'Isus')
l16 = Cabana('L16', 'L', 'Westpool')
medium_locker = Locker('M')
large_locker = Locker('L')

dkub_shop.add_cabana(n14)
dkub_shop.add_cabana(m15)
dkub_shop.add_cabana(l16)
dkub_shop.add_locker(medium_locker)
dkub_shop.add_locker(large_locker)

# product_list = dkub_shop.choose_product(dkub, datetime.now().date(), K_mam)
# trans = dkub_shop.create_transaction(product_list, K_mam, datetime.now().date())
# print(payment.generate_payment(dkub, trans, 'promptpay'))
# for booking in dkub.booking_list:
#     print(booking.id, booking.transaction.total)