from datetime import date
from order import Order, OrderDetail
from products import Cabana, Locker, Ticket, Towel
from products import create_cabana, create_locker, create_ticket

class Stock:
    def __init__(self):
        self.__cabana_list = create_cabana()
        self.__locker_list = create_locker()
        self.__ticket_list = create_ticket()
        self.__towel = Towel()
    
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
    
    @property
    def towel_price(self):
        return self.__towel
    
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
    
    def get_cabana_in_zone(self, cabana_zone):
        for zone in range (len(self.__cabana_list)):
            for cabana in range (len(self.__cabana_list[zone])):
                if cabana_zone == self.__cabana_list[zone][cabana].zone:
                    return self.__cabana_list[zone]
                cabana_zone += 1        
        return None
    
class DailyStock(Stock):
    def __init__(self, date):
        super().__init__()
        self.__date = date
        self.__booking_list = []
    
    @property
    def date(self):
        return self.__date
    
    def is_available(self, item, amount):
        if isinstance(item, Cabana):
            return not item.is_reseve # If reserved = Not available
        elif not isinstance(item, Ticket):
            return item.remaining_amount >= amount
        return True
                  

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