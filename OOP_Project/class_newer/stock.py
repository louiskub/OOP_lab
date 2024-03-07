from booking import Booking
from order import Order
from service import Cabana, Locker, Ticket, Towel
from datetime import date, timedelta

class Stock:
    def __init__(self):
        self.__cabana_list = Stock.create_cabana()
        self.__locker_list = Stock.create_locker()
        self.__ticket_list = Stock.create_ticket()
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
    
    def show_cabana(self):
        return self.__cabana_list
    def create_locker():
        locker_list = []
        locker_list.append(Locker('M', 80)) # Locker
        locker_list.append(Locker('L', 20))
        return locker_list
    def create_cabana():
        wave_pool_zone = []
        wave_pool_zone.append(Cabana('W01', 'S', 'Wave Pool')) # Wave Pool Zone
        wave_pool_zone.append(Cabana('W02', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W03', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W04', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W05', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W06', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W07', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W08', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W09', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W10', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W11', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W12', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W13', 'L', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W14', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W15', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W16', 'M', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W14', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W14', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('W14', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('P05', 'S', 'Wave Pool'))
        wave_pool_zone.append(Cabana('P06', 'S', 'Wave Pool'))

        activity_relax_zone = []
        activity_relax_zone.append(Cabana('P01', 'S', 'Activity and Relax')) # Activity and Relax Zone
        activity_relax_zone.append(Cabana('P02', 'S', 'Activity and Relax'))
        activity_relax_zone.append(Cabana('P03', 'M', 'Activity and Relax'))
        activity_relax_zone.append(Cabana('P04', 'M', 'Activity and Relax'))

        hill_zone = []
        hill_zone.append(Cabana('H01', 'S', 'Activity and Relax')) # Hill Zone
        hill_zone.append(Cabana('H02', 'S', 'Activity and Relax'))
        hill_zone.append(Cabana('H03', 'S', 'Activity and Relax'))
        hill_zone.append(Cabana('H04', 'M', 'Activity and Relax'))
        hill_zone.append(Cabana('H05', 'M', 'Activity and Relax'))

        family_zone = []
        family_zone.append(Cabana('F01', 'M', 'Family')) # Family Zone
        family_zone.append(Cabana('F02', 'S', 'Family'))
        family_zone.append(Cabana('F03', 'L', 'Family'))
        family_zone.append(Cabana('F04', 'S', 'Family'))
        family_zone.append(Cabana('F05', 'M', 'Family'))
        family_zone.append(Cabana('F06', 'M', 'Family'))
        family_zone.append(Cabana('K05', 'M', 'Family'))
        family_zone.append(Cabana('K06', 'M', 'Family'))
        family_zone.append(Cabana('K07', 'S', 'Family'))
        
        cabana_list = []
        cabana_list.extend([wave_pool_zone, activity_relax_zone, hill_zone, family_zone])
        return cabana_list
    def create_ticket():
        ticket_list = []
        
        # Solo Ticket
        ticket_list.append(Ticket('Full Day', 1, 699))
        ticket_list.append(Ticket('Senior', 1, 599)) # >= 60 y.o. and want to play slides
        ticket_list.append(Ticket('Child', 1, 0))
        ticket_list.append(Ticket('SPD', 1, 0)) # including pregnant and disabled 

        # Group Ticket
        ticket_list.append(Ticket('Group for 4', 4, 2599))
        ticket_list.append(Ticket('Group for 6', 6, 3779))
        ticket_list.append(Ticket('Group for 8', 8, 4879))
        ticket_list.append(Ticket('Group for 10', 10, 5999))
        return ticket_list

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
        Stock.__init__(self)
        self.__date = date
        self.__booking_list = []
    
    @property
    def date(self):
        return self.__date
    
        cabana_list = []
        for cabana in self.cabana_list:
            if cabana.is_reserve == False:
                cabana_list.append(cabana)
        return cabana_list
    # def reserve(self, order: Order):
    #     if not isinstance(order, Order):
    #         return None
    #     order_detail = order.selected_item_list
    #     for each_order in order_detail:
    #         if each_order[0] == "Cabana":
    #             if each_order[1].is_reserve == False:
    #                 each_order[1].is_reserve = True
    #         elif each_order[0] == "Towel":
    #             if each_order[1] <= self.get_remaining_towel():
    #                 self.__towel_reserved += each_order[1]
    #         elif isinstance(each_order[0], Locker) :
    #             if each_order[0].size == 'M' and each_order[1] <= self.get_remaining_medium_locker():
    #                 self.__medium_locker_reserved += each_order[1]
    #             elif each_order[0].size == 'L' and each_order[1] <= self.get_remaining_large_locker():
    #                 self.__towel_reserved += each_order[1]
    #     return "Done"
    
    def update_item(self, item, amount):
        if isinstance(item, Cabana):
            item.update_status('R')
        elif not isinstance(item, Ticket):
            item.update_status('R', amount)
    def is_available(self, item, amount):
        if isinstance(item, Cabana):
            return not item.is_reserve # If reserved = Not available
        elif not isinstance(item, Ticket):
            return item.remaining_amount >= amount
        return True
    
def create_daily_stock():
    daily_list = []
    for i in range(60):
        daily_list.append(DailyStock(date.today + timedelta(days=i)))
    return daily_list