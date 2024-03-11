from datetime import date
from order import Order
from products import Cabana, Locker, Ticket
from products import create_cabana, create_locker, create_ticket

class Stock:
    def __init__(self):
        self.__cabana_list = create_cabana
        self.__locker_list = create_locker
        self.__ticket_list = create_ticket
        self.__medium_locker_amount = 80
        self.__large_locker_amount = 20
        self.__towel_amount = 5000
        self.__towel_price = 99
    
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
    def medium_locker_amount(self):
        return self.__medium_locker_amount
    
    @property
    def large_locker_amount(self):
        return self.__large_locker_amount
    
    @property
    def towel_amount(self):
        return self.__towel_amount
    
    @property
    def towel_price(self):
        return self.__towel_price
    
    def add_cabana(self, cabana):
        if isinstance(cabana, Cabana):
            self.__cabana_list.append(cabana)
        else: return 'Error'
            
    def add_locker(self, locker):
        if isinstance(locker, Locker):
            self.__locker_list.append(locker)
        else: return 'Error'
            
    def add_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.__ticket_list.append(ticket)
        else: return 'Error'
    
    def show_all(self):
        pass 
    
class DailyStock(Stock):
    def __init__(self, date):
        super().__init__()
        self.__date = date
        self.__medium_locker_reserved = 0
        self.__large_locker_reserved = 0
        self.__towel_reserved = 0
        self.__booking_list = []
    
    @property
    def date(self):
        return self.__date
    
    def get_remaining_large_locker(self):
        return self.large_locker_amount - self.__large_locker_reserved
    
    def get_remaining_medium_locker(self):
        return self.medium_locker_amount - self.__medium_locker_reserved
    
    def get_remaining_towel(self):
        return self.towel_amount - self.__towel_reserved
    
    def get_available_cabana(self):
        cabana_list = []
        for cabana in self.cabana_list:
            if cabana.is_reserve == False:
                cabana_list.append(cabana)
        return cabana_list
    
    def get_cabana_from_zone(self, zone):
        cabana_list = []
        for cabana in self.get_available_cabana():
            if zone == cabana.zone:
                cabana_list.append(cabana)
        return cabana_list
                 
                
    def check_still_available(self, order):
        #[[Ticket(Type),10],["Towel",1],["Cabana",Cabana],[Locker(Med),10],[Locker(Large),20]]
        if not isinstance(order, Order):
            return None
        order_detail = order.selected_item_list
        for each_order in order_detail:
            if each_order[0] == "Cabana":
                if each_order[1] not in self.get_available_cabana():
                    return False
            elif each_order[0] == "Towel":
                if each_order[1] > self.get_remaining_towel():
                    return False
            elif isinstance(each_order[0], Locker):
                if each_order[0].size == 'M' and each_order[1] > self.get_remaining_medium_locker():
                    return False
                elif each_order[0].size == 'L' and each_order[1] > self.get_remaining_large_locker():
                    return False
            else:
                return False
        return True
       
    # def add_booking(self, booking):
    #     if isinstance(booking, Booking):
    #         self.__booking_list.append(booking)
    #     else: return 'Error'

def create_daily_stock():
    daily_list = []
    daily_list.append(DailyStock(date(2024, 2, 1)))
    daily_list.append(DailyStock(date(2024, 2, 2)))
    daily_list.append(DailyStock(date(2024, 2, 3)))
    daily_list.append(DailyStock(date(2024, 2, 4)))
    daily_list.append(DailyStock(date(2024, 2, 5)))
    daily_list.append(DailyStock(date(2024, 2, 6)))
    daily_list.append(DailyStock(date(2024, 2, 7)))
    daily_list.append(DailyStock(date(2024, 2, 8)))
    daily_list.append(DailyStock(date(2024, 2, 9)))
    daily_list.append(DailyStock(date(2024, 2, 10)))
    
    return daily_list