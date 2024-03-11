from datetime import datetime, date, time, timedelta

class WaterPark:
    def __init__(self, name):
        self.__name = name
        self.__stock_list = None
        self.__daily_stock = None
        self.__customer_list = []
        self.__member_list = []
        self.__pormotion_list = []
        self.__booking_list = []
        self.__reward_list = []
        
    def show_services() : 
        pass
    def show_services_from_date( date ):
        pass 
    def show_selection():
        pass
    def search_coupon_from_code():
        pass 
    def cal_price():
        pass 
    def create_member():
        pass
    def create_customer():
        pass
    def create_booking(): # choice/coupon 
        pass 
    def show_confirm_booking():
        pass
    def show_payment_options():
        pass 
    def show_paid():
        pass 
    def send_finished_booking(): # add reward
        pass
    def update_status():
        pass
    def cancel_booking(booking):
        pass
    def search_booking_from_user():
        pass 
    def selected_item():
        pass
    def add_item( item, amount ) : # return self
        pass
    def remove_item( item, amount ) : # return self
        pass
    def to_dict( item_list ) : # return dict
        pass
    def fill_information(name, email, phone_no):
        pass
    
class Stock:
    def __init__(self):
        self.__cabana_list = []
        self.__medium_locker_amount = 80
        self.__large_locker_amount = 20
        self.__towel_amount = 5000
        self.__towel_price = 99
    
    def show_cabana(self):
        return self.__cabana_list
    def show_medium_locker_amount(self):
        pass   
    def show_large_locker_amount(self):
        pass
    def show_towel_amount(self):
        pass    
    def show_all(self):
        pass 
    
class DailyStock(Stock):
    def __init__(self, date):
        super().__init__()
        self.__date = date
        self.__medium_locker_reserved = 0
        self.__large_locker_reserved = 0
        self.__towel_reserved = 0
        #self.__booking_list = []
        
    # def add_booking(self, booking):
    #     if isinstance(booking, Booking):
    #         self.__booking_list.append(booking)
    #     else: return 'Error'
        
class Cabana:
    def __init__(self, id, size, zone):
        self.__id = id
        self.__size = size
        self.__zone = zone
        self.__price = 0
        self.__is_reserve = False
        
    @property    
    def price(self):
        # standard_price = 899
        # medium_price = 1499
        # large_price = 2499
        cabana_price = {'S':899, 'M':1499, 'L':2499}
        
        for size, price in cabana_price.items():
            if self.__size == size:
                return price
        return 'Error' 
 
class Locker:
    def __init__(self, size):
        self.__size = size
        self.__price = 0
        self.__is_reserve = False
        
    @property
    def price(self):
        # locker_medium_price = 149
	    # locker_large_price = 229
        locker_price = {'M':149, 'L':229}
        
        for size, price in locker_price.items():
            if self.__size == size:
                return price
        return 'Error'
    
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

class Coupon:
    def __init__(self, discount, start_date, end_date, min_purchase):
        self.__discount = discount
        self.__start_date = start_date
        self.__end_date = end_date    
        self.__min_purchase = min_purchase    
    
    def get_available_date(self):
        date_list = [self.__start_date + timedelta(days = x) for x in range((self.__end_date - self.__start_date).days + 1)]
        return date_list

class Customer:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__booking_list = []
        
class Member(Customer):
    def __init__(self, name, email, phone_number, birthday, nationality):
        super().__init__(name, email, phone_number)
        self.__birthday = birthday
        self.__nationality = nationality
        self.__point = 0
        self.__password = None
        self.__points_history_list = []
        self.__reward_history_list = []
        
    def __add__(self, amounts):
        if amounts > 0:
            self.__point += amounts
            return 'Success'
        else: 
            return 'Invalid Amounts'
        
    def __sub__(self, amounts):
        if self.__point >= amounts > 0:
            self.__point -= amounts
            return 'Success'
        else: 
            return 'Not enough points'
    
    def check_password(self, password):
        for char in password:
            if char.isnumeric() or char.isalpha() or char == '.':
                continue
            return False
        
    def add_password(self, password):
        if len(password) >= 8 and self.check_password(password) != False:
            self.__password = password
            return 'Success'
        elif len(password) < 8:
            return 'Please use a password with at least 8 characters.'
        elif self.check_password(password) == False:
            return 'Please use passwords that contain only the letters 0-9, a-z, A-Z, or (.)'
        else: 
            return 'Please use a password with at least 8 characters and only the letters 0-9, a-z, A-Z, or (.)' 
        
    def add_points_history(self, history):
        if isinstance(history, PointsHistory):
            self.__points_history_list.append(history)
        else: return 'Error'
    
class PointsHistory:
    def __init__(self, amounts, point_after, datetime):
        self.__amounts = amounts
        self.__point_after = point_after
        self.__datetime = datetime
        self.__reward = None # Only 1 reward can be redeemed at a time
        
    def add_reward(self, reward):
        if isinstance(reward, Reward):
            self.__reward = reward
        else: return 'Error'
            
        
        
stock = Stock()
daily = DailyStock(datetime(2024, 2, 15, 16, 30))

def create_cabana_and_locker():
    w01 = Cabana('W01', 'S', 'Wave Pool') # Wave Pool Zone
    w02 = Cabana('W02', 'S', 'Wave Pool')
    w03 = Cabana('W03', 'M', 'Wave Pool')
    w04 = Cabana('W04', 'M', 'Wave Pool')
    w05 = Cabana('W05', 'M', 'Wave Pool')
    w06 = Cabana('W06', 'M', 'Wave Pool')
    w07 = Cabana('W07', 'M', 'Wave Pool')
    w08 = Cabana('W08', 'M', 'Wave Pool')
    w09 = Cabana('W09', 'M', 'Wave Pool')
    w10 = Cabana('W10', 'S', 'Wave Pool')
    w11 = Cabana('W11', 'S', 'Wave Pool')
    w12 = Cabana('W12', 'S', 'Wave Pool')
    w13 = Cabana('W13', 'L', 'Wave Pool')
    w14 = Cabana('W14', 'S', 'Wave Pool')
    w15 = Cabana('W15', 'M', 'Wave Pool')
    w16 = Cabana('W16', 'M', 'Wave Pool')
    w17 = Cabana('W14', 'S', 'Wave Pool')
    w18 = Cabana('W14', 'S', 'Wave Pool')
    w19 = Cabana('W14', 'S', 'Wave Pool')
    p05 = Cabana('P05', 'S', 'Wave Pool')
    p06 = Cabana('P06', 'S', 'Wave Pool')
    
    p01 = Cabana('P01', 'S', 'Activity and Relax') # Activity and Relax Zone
    p02 = Cabana('P02', 'S', 'Activity and Relax')
    p03 = Cabana('P03', 'M', 'Activity and Relax')
    p04 = Cabana('P04', 'M', 'Activity and Relax')
    
    h01 = Cabana('H01', 'S', 'Activity and Relax') # Hill Zone
    h02 = Cabana('H02', 'S', 'Activity and Relax')
    h03 = Cabana('H03', 'S', 'Activity and Relax')
    h04 = Cabana('H04', 'M', 'Activity and Relax')
    h05 = Cabana('H05', 'M', 'Activity and Relax')
    
    f01 = Cabana('F01', 'M', 'Family') # Family Zone
    f02 = Cabana('F02', 'S', 'Family')
    f03 = Cabana('F03', 'L', 'Family')
    f04 = Cabana('F04', 'S', 'Family')
    f05 = Cabana('F05', 'M', 'Family')
    f06 = Cabana('F06', 'M', 'Family')
    k05 = Cabana('K05', 'M', 'Family')
    k06 = Cabana('K06', 'M', 'Family')
    k07 = Cabana('K07', 'S', 'Family')
    
    locker_m = Locker('M') # Locker
    locker_l = Locker('L')

def create_ticket():
    full_day_ticket = Ticket('Full Day', 1, 699)
    senior_with_slides = Ticket('Senior', 1, 599) # >= 60 y.o. and want to play slides
    free_child_ticket = Ticket('Child', 1)
    senior_pools_only = Ticket('SPD', 1) # including pregnant and disabled 
    group_for_4 = Ticket('Group', 4, 2599)
    group_for_6 = Ticket('Group', 6, 3779)
    group_for_8 = Ticket('Group', 8, 4879)
    group_for_10 = Ticket('Group', 10, 5999)

def create_customer_and_member():
    # Member
    # prae = Member('Prae', 'sirima26@gmail.com', '0912345678', date(2005, 3, 26), 'Thai')
    # louis = Member('Louis', 'manatsavin@gmail.com', '0923456789', date(2005, 4, 23), 'Thai')
    # beam = Member('Beam', 'ananthachai@gmail.com', '0934567890', date(2004, 9, 20), 'Thai')
    # som = Member('Som', 'ariya28@gmail.com', '0945678901', date(2004, 10, 28), 'Thai')
    
    # Customer
    james = Customer('James', 'james123@gmail.com', '0812345678')
    yuji = Customer('Yuji', 'yuji1234@gmail.com', '0823456789')
    irene = Customer('Irene', 'irene123@gmail.com', '0834567890')
    charlotte = Customer('Charlotte', 'charlotte@gmail.com', '0845678901')
    sharon = Customer('Sharon', 'sharon12@gmail.com', '0856789012')
    rose = Customer('Rose', 'rose1234@gmail.com', '0867890123')
    lucian = Customer('Lucian', 'lucian123@gmail.com', '0878901234')
    zeno = Customer('Zeno', 'zeno1234@gmail.com', '0889012345')
    apollo = Customer('Apollo', 'apollo12@gmail.com', '0890123456')
    lucian = Customer('Lucian', 'lucian123@gmail.com', '0801234567')
    dion = Customer('Dion', 'dion1234@gmail.com', '0898765432')
 
w01 = Cabana('W01', 'S', 'Wave Pool')
     
create_cabana_and_locker() 
create_ticket()
create_customer_and_member()
print(w01.price)
#print(daily.show_cabana())