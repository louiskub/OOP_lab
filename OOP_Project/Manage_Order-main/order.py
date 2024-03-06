from products import Cabana, Locker, Ticket, Towel

class Order:
    def __init__(self, visit_date):
        self.__visit_date = visit_date
        self.__order_detail = []
        self.__total = 0
        self.__promotion = None
    
    def __str__(self):
        return f"{[order for order in self.__order_detail]}\nTOTAL: {self.__total}"
    
    @property
    def visit_date(self):
        return self.__visit_date
    
    @property
    def total(self):
        for items in self.__order_detail:
            self.__total += items.total_price
        return self.__total
    
    @property
    def order_detail(self):
        return self.__order_detail
        
    def add_item(self, item) : # Press the add button
        if isinstance(item, Cabana):
            for items in self.__order_detail:
                if isinstance(items.item, Cabana):
                    return self
        elif isinstance(item, (Locker, Towel, Ticket)):
            for items in self.__order_detail:
                if items.item == item:
                    items + 1
                    return self
        self.__order_detail.append(OrderDetail(item))         
        return self
    
    def remove_item(self, item) : # Press the reduce button
        for items in self.__order_detail:
            if item == items.item:
                items - 1
                if items.amount == 0:
                   self.__order_detail.remove(items)
                return self
        return self

    # def check_still_available(self) -> bool:
    #     for order_detail in self.__order_detail_list:
    #         item = order_detail.item
    #         if isinstance(item, Cabana):
    #             return not item.is_reseve # If reserved = Not available
    #         elif not isinstance(item, Ticket):
    #             return item.remaining_amount >= order_detail.amount
    #     return True
    
    def reserve(self):
        for order_detail in self.__order_detail_list:
            item = order_detail.item
            if isinstance(item, Cabana):
                item.is_reseve = True
            elif not isinstance(self.__item, Ticket):
                item.remaining_amount -= order_detail.amount
        return "Done"
    
    def use_coupon(self, coupon):
        pass
    
class OrderDetail:
    def __init__(self, item, amount = 1):
        self.__item = item  # ใส่เป็น instance 
        self.__amount = amount
        self.__total_price = 0
    
    def __str__(self):
        return f"{self.item} x {self.__amount} = {self.total_price} THB"
    
    def __add__(self, amount):
        if 0 < amount:
            self.__amount += 1
        
    def __sub__(self, amount):
        if 0 < amount <= self.__amount:
            self.__amount -= amount 
        
    @property
    def item(self):
        return self.__item
    
    @property 
    def amount(self):
        return self.__amount
    
    @property
    def total_price(self):
        return self.__item.price * self.__amount