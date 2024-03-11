from products import Cabana, Locker, Ticket
from stock import Stock

class Order:
    def __init__(self, visit_date):
        self.__visit_date = visit_date
        self.__selected_item_list = []
        self.__total = 0
        self.__coupon = None
    
    @property
    def visit_date(self):
        return self.__visit_date
    
    @property
    def total(self):
        return self.__total
    
    @property
    def selected_item_list(self):
        return self.__selected_item_list
    
    def add_coupon(self):
        pass
        
    def add_item(self, item) : # Press the add button
        for each_item in self.__selected_item_list:
            if isinstance(item, (Locker, Ticket)) or item == 'Towel':
                if item == each_item[0]:
                    each_item[1] += 1
                    return self
                self.__selected_item_list.extend([item, 1])
            elif isinstance(item, Cabana):
                self.__selected_item_list.extend(['Cabana', item])
        self.cal_total()
        return self
    
    def remove_item(self, item) : # Press the reduce button
        for each_item in self.__selected_item_list:
            if item == each_item[0]:
                each_item[1] -= 1
                if each_item[1] == 0:
                   self.__selected_item_list.remove(each_item)
            elif item == each_item[1] and isinstance(item, Cabana):
                self.__selected_item_list.remove(each_item)
        self.cal_total()
        return self
    
    def cal_total(self):
        for each_item in self.__selected_item_list:
            if isinstance(each_item[0], (Locker, Ticket)):
                self.__total += each_item[0].price * each_item[1]
            elif isinstance(each_item[1], Cabana):
                self.__total += each_item[1].price
            elif each_item[0] == 'Towel':
                self.__total += Stock.towel_price * each_item[1]
        return self.__total
    
    def use_coupon(self, coupon):
        pass
