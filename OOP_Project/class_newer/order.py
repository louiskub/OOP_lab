from service import Cabana, Ticket, Locker, Towel

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
    def order_detail(self):
        return self.__order_detail
    @property
    def total(self):
        total = 0
        for items in self.__order_detail:
            total += items.total_price
        self.__total = total
        return self.__total
    
    def to_dict(self):
        return {
            "visit_date": self.__visit_date,
            "order_detail": [detail.to_dict() for detail in self.__order_detail],
            "total": self.total,
            "promotion": self.__promotion,
        }
    
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
    #     for order_detail in self.__order_detail:
    #         item = order_detail.item
    #         if isinstance(item, Cabana):
    #             return not item.is_reseve  # ถ้าจองแล้ว = ไม่ว่าง
    #         elif not isinstance(item, Ticket):
    #             return item.remaining_amount >= order_detail.amount
    #     return True

    # def reserve(self):
    #     for order_detail in self.__order_detail:
    #         item = order_detail.item
    #         if isinstance(item, Cabana):
    #             item.is_reseve = True
    #         elif not isinstance(self.__item, Ticket):
    #             item.remaining_amount -= order_detail.amount
    #     return "Done"
    
    # def cancel_reseve(self):
    #     for order_detail in self.__order_detail:
    #         item = order_detail.item
    #         if isinstance(item, Cabana):
    #             item.is_reseve = False
    #         elif not isinstance(self.__item, Ticket):
    #             item.remaining_amount += order_detail.amount
    #     return "Done"

    def show_order_detail(self):
        return [detail.order_detail_dict() for detail in self.__order_detail]

class OrderDetail:
    def __init__(self, item):
        self.__item = item #instance of Locker, Cabana, Ticket
        self.__amount = 1
        self.__total_price = 0

    @property
    def item(self):
        return self.__item
    @property
    def amount(self):
        return self.__amount
    @property
    def total_price(self):
        return self.__item.price * self.__amount
    def __str__(self):
        return f"{self.item} x {self.__amount} = {self.total_price} THB"
    
    def __add__(self, amount):
        if 0 < amount:
            self.__amount += 1
        
    def __sub__(self, amount):
        if 0 < amount <= self.__amount:
            self.__amount -= amount 
        

    def to_dict(self):
        return {
            "Item Name": self.item.name(),
            "Price": self.item.price,
            "Qty": self.amount,
            "Subtotal": self.total_price
        }


def create_locker():
    locker_list = []
    locker_list.append(Locker('M', 149, 80)) # Locker
    locker_list.append(Locker('L', 229, 20))
    
    return locker_list
    
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