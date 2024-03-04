from booking import Order, Booking
from service import Cabana, Locker

class Stock:
    def __init__(self):
        self.__cabana_list = []
        self.__medium_locker_amount = 80
        self.__large_locker_amount = 20
        self.__towel_amount = 5000

    # @property
    # def medium_locker_amount(self):
    #     return self.__medium_locker_amount
    @property
    def large_locker_amount(self):
        return self.__large_locker_amount
    @property
    def towel_amount(self):
        return self.__towel_amount

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
        Stock.__init__(self)
        self.__date = date
        self.__medium_locker_reserved = 0
        self.__large_locker_reserved = 0
        self.__towel_reserved = 0
    
    @property
    def date(self):
        return self.__date
    
    def get_remaining_large_locker(self):
        return self.large_locker_amount - self.__large_locker_reserved
    
    def get_remaining_medium_locker(self):
        return self._Stock__medium_locker_amount - self.__medium_locker_reserved
    
    def get_remaining_towel(self):
        return self.__towel_amount - self.__towel_reserved
    
    def get_available_cabana(self):
        cabana_list = []
        for cabana in self.cabana_list:
            if cabana.is_reserve == False:
                cabana_list.append(cabana)
        return cabana_list

    def check_still_available(self, order):
        #[[Ticket(Type),10],["Towel",1],["Cabana",Cabana],[Locker(Med),10],[Locker(Large),20]]
        if not isinstance(order, Order):
            return None
        order_detail = order.selected_item_list
        for each_order in order_detail:
            if each_order[0] == Locker('M'):
                if each_order[1].is_reserve == True:
                    return False
            elif each_order[0] == "Towel":
                if each_order[1] > self.get_remaining_towel():
                    return False
            elif isinstance(each_order[0], Locker) :
                if each_order[0].size == 'M' and each_order[1] > self.get_remaining_medium_locker():
                    return False
                elif each_order[0].size == 'L' and each_order[1] > self.get_remaining_large_locker():
                    return False
        return True

    def reserve(self, order: Order):
        if not isinstance(order, Order):
            return None
        order_detail = order.selected_item_list
        for each_order in order_detail:
            if each_order[0] == "Cabana":
                if each_order[1].is_reserve == False:
                    each_order[1].is_reserve = True
            elif each_order[0] == "Towel":
                if each_order[1] <= self.get_remaining_towel():
                    self.__towel_reserved += each_order[1]
            elif isinstance(each_order[0], Locker) :
                if each_order[0].size == 'M' and each_order[1] <= self.get_remaining_medium_locker():
                    self.__medium_locker_reserved += each_order[1]
                elif each_order[0].size == 'L' and each_order[1] <= self.get_remaining_large_locker():
                    self.__towel_reserved += each_order[1]
        return "Done"
    
    