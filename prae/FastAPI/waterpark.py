from products import Cabana, Locker, Ticket, Towel
from stock import Stock, DailyStock, create_daily_stock 
from member import Member
from order import Order
from datetime import date

class WaterPark:
    def __init__(self, name):
        self.__name = name
        self.__stock = Stock()
        self.__daily_stock_list = create_daily_stock
        self.__customer_list = []
        self.__member_list = []
        self.__coupon_list = []
        self.__booking_list = []
        self.__reward_list = []
    
    @property
    def member_list(self):
        return self.__member_list
    
    def add_stock(self, stock):
        self.__stock = stock
        
    def add_daily_stock(self, daily):
        self.__daily_stock_list.append(daily)    
        
    def add_member(self, member):
        if isinstance(member, Member):
            self.__member_list.append(member)
        else: return 'Error'        
    
    def search_daily_stock_from_date(self, date):
        for daily in self.__daily_stock_list:
            if date == daily.date:
                return daily
        return 'Not Found'
    
    def search_member_from_id(self, id):
        for member in self.__member_list:
            if id == member.id:
                return member
        return 'Not Found'
        
    def get_all_services(self) : 
        services = {}
        # services["Ticket"] = self.__stock.ticket_list
        # services["Cabana"] = self.__stock.cabana_list
        # services["Locker"] = self.__stock.locker_list
        services["Ticket"] = {}
        services["Cabana"] = {}
        services["Locker"] = {}
        for ticket in self.__stock.ticket_list:
            services["Ticket"][ticket.type] = ticket.price
        for cabana in self.__stock.cabana_list:
            services["Cabana"][cabana.id] = cabana.price
        for locker in self.__stock.locker_list:
            services["Locker"][locker.size] = locker.price 
        services["Towel"] = self.__stock.towel_price  
            
        return services
        
    def get_services_in_date(self, date):
        daily_stock = self.search_daily_stock_from_date(date)
        services = self.get_all_services()
        del services["Cabana"]
        services["Cabana"] = {}
        available_cabana_list = daily_stock.get_available_cabana()
        if available_cabana_list != []:
            for cabana in available_cabana_list:
                services["Cabana"][cabana.id] = cabana.price
        else : services["Cabana"] = []
        return services
    
    def create_order(self, date):
        return Order(date)
    
    def add_item(self, item, order):
        daily_stock = self.search_daily_stock_from_date(order.visit_date)
        if daily_stock.check_still_available(order):
            order.add_item(item)
        return order
    
    def remove_item(self, item, order):
        pass
        return order
        
    
    def become_member(self, name, email, phone_number, birthday, password):
        for member in self.__member_list:
            if email == member.email or phone_number == member.phone_number:
                return 'You are already a member.' 
        if Member.check_email(email):
            if Member.check_phone_number(phone_number) and len(phone_number) == 10:
                if Member.check_password(password) and len(password) >= 8:
                    self.add_member(Member(name, email, phone_number, birthday, password))
                    return 'Membership registration completed.'
                return 'Choose your password again.'
            return 'Fill the correct phone number.'
        return 'Fill the correct email.'                 

    def search_coupon_from_code():
        pass 
    def create_booking():
        pass 
    def show_confirm_booking():
        pass
    def show_payment_options():
        pass 
    def send_finished_booking(): 
        pass
    def update_status():
        pass
    def cancel_booking(booking):
        pass
    def search_booking_from_user():
        pass 

dkub = WaterPark('Dkub')
# print(dkub.become_member('siirma', 'siirma@gmail.com', '0123456789', date(2005, 3, 26), 'srm12345._'))
# print(dkub.become_member('siirma', 'siirma@gmail.com', '0123456789', date(2005, 3, 26), 'srm12345._'))
# for member in dkub.member_list:
#     print(member.id, member.name)

order1 = Order(date(2024, 3, 2))
order1
