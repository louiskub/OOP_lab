from products import Cabana, Locker, Ticket
from stock import Stock, DailyStock, create_daily_stock
from member import Member
from order import Order
from datetime import date

class WaterPark:
    def __init__(self, name):
        self.__name = name
        self.__stock = Stock()
        self.__daily_stock_list = create_daily_stock()
        self.__zone_list = ['Wave Pool', 'Activity and Relax', 'Hill', 'Family']
        self.__customer_list = []
        self.__member_list = []
        self.__promotion_list = []
        self.__payment_list = []
        self.__transaction_list = []
    
    def get_member_list(self):
        return self.__member_list
        
    def add_daily_stock(self, daily):
        self.__daily_stock_list.append(daily)    
        
    def add_member(self, member):
        if isinstance(member, Member):
            self.__member_list.append(member)
        else: return 'Error'     
        
    def search_member_from_id(self, id):
        for member in self.__member_list:
            if id == member.id:
                return member
        return 'Not Found' 
    
    def search_daily_stock_from_date(self, date):
        for daily in self.__daily_stock_list:
            if date == daily.date:
                return daily
        return 'Not Found'  
    
    def get_services_in_stock(self, stock):
        services = {}
        services["Ticket"] = stock.ticket_list
        services["Cabana"] = stock.cabana_list
        services["Locker"] = stock.locker_list
        services["Towel"] = stock.towel
        return services    
        
    def get_all_services(self) : # When press services button
        return self.get_services_in_stock(self.__stock)
        
    def get_services_in_date(self, date): # After selected date
        daily_stock = self.search_daily_stock_from_date(date)
        return self.get_services_in_stock(daily_stock)
    
    def get_zone(self):
        return self.__zone_list
    
    def get_cabana_in_zone(self, date):
        daily_stock = self.search_daily_stock_from_date(date)
        cabana_in_zone = {}
        for zone in self.__zone_list:
            cabana_in_zone[zone] = daily_stock.get_cabana_in_zone(zone)
        return cabana_in_zone
    
    def create_order(self, date):
        return Order(date)
    
    def add_item(self, item, order): # Press (+) button.
        daily_stock = self.search_daily_stock_from_date(order.visit_date)
        if daily_stock.is_available(item, 1):
            order.add_item(item)
        return order
    
    def remove_item(self, item, order): # Press (-) button.
        return order.remove_item(item)
    
    def become_member(self, name, email, phone_number, birthday, password):
        for member in self.__member_list:
            if email == member.email or phone_number == member.phone_number:
                return 'You are already a member.' 
        if Member.check_email(email):
            if Member.check_phone_number(phone_number) and len(phone_number) == 10:
                if Member.check_password(password) and len(password) >= 8:
                    self.add_member(Member(name, email, phone_number, birthday, password))
                    return 'Membership registration completed.'
                return 'Please use a password with at least 8 characters and only the letters 0-9, a-z, A-Z, or (.)'
            return 'Fill the correct phone number.'
        return 'Fill the correct email.'                 

    # def verify_member(self, email, password):
    #     for member in self.__member_list:
    #         member.verify_member(email, password)
    #     return 'Email or password is incorrect.'
    
    def search_member_by_email(self,email):
        for member in self.__member_list:
            if email == member.email:
                return member
            
    def login_member(self, email, password):
        for member in self.__member_list:
            if member.verify_member(email,password) != None:
                    return "Login successful"
            # else:
            #         return "Incorrect password"
        return "Email/Password not found or incorrect"    
    
            
# system = WaterPark('Dkub')
# mem=Member("Nong","123456@gmail.ac.th","0811111111","28/10/47","1111111111")
# mem2=Member("Ki","355@gmail.ac.th","0811234111","8/10/47","125698851")
# system.add_member(mem)
# system.add_member(mem2)


# print(system.search_member_by_email("123456@gmail.ac.th").id)

    # def login_member(self, email, password):
        
    #     for member in self.__member_list:
    #         if member.verify_member(email, password):
    #             return member
    #     return None
    
### Test All Method ###

# dkub = WaterPark('Dkub')
# my_order = dkub.create_order(date(2024, 2, 2))
# daily_stock = dkub.search_daily_stock_from_date(my_order.visit_date)
# towel = daily_stock.towel   
# for locker in daily_stock.locker_list: # choose locker
#     locker_L = locker
# for ticket in daily_stock.ticket_list: # choose ticket
#     my_ticket = ticket
    
# dkub.add_item(towel, my_order)
# dkub.add_item(towel, my_order)
# dkub.add_item(towel, my_order)
# dkub.add_item(locker_L, my_order)
# dkub.add_item(my_ticket, my_order)
# dkub.remove_item(towel, my_order)

# # for detail in my_order.order_detail:
# #     print(detail)
# # print(f"TOTAL: {my_order.total}")
# print(my_order)