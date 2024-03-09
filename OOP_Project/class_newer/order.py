from service import Cabana, Ticket, Locker, Towel
from promotion import AmountCoupon
class Order:
    def __init__(self, visit_date):
        self.__visit_date = visit_date
        self.__order_detail = []
        self.__total = 0
        self.__promotion = None
    
    # def __str__(self):
    #     return f"{[order for order in self.__order_detail]}\nTOTAL: {self.__total} THB"

    @property
    def visit_date(self):
        return self.__visit_date

    @property
    def order_detail(self):
        return self.__order_detail
    
    @property
    def total(self):
        return self.__total
        
    @property
    def promotion(self):
        return self.__promotion
    
    @promotion.setter
    def promotion(self, promotion):
        self.__promotion = promotion

    # Calculate the purchase amount before discount.
    def cal_purchase_amount(self):
        total = 0
        for items in self.__order_detail:
            total += items.total_price
        return total
    
    # Calculate the discount received.
    def cal_discount(self):
        if self.promotion == None: 
            return 0
        total = self.cal_purchase_amount()
        if self.promotion.is_expired():
            self.promotion = None
            return 0
        if isinstance(self.promotion, AmountCoupon):
            if self.promotion.min_purchase > total :
                self.promotion = None
                return 0
        return self.promotion.get_discount(total)
    
    # Calculate total purchase after discount.
    def cal_total(self):
        self.__total = self.cal_purchase_amount() - self.cal_discount()
        return self.__total
    
    # Add item to order.
    def add_item(self, item) : # Press the add button
        if isinstance(item, Cabana):
            for items in self.__order_detail:
                if isinstance(items.item, Cabana):
                    return self.to_dict()
        elif isinstance(item, (Locker, Towel, Ticket)):
            for items in self.__order_detail:
                if items.item == item:
                    items + 1
                    self.cal_total()
                    return self.to_dict()
        self.__order_detail.append(OrderDetail(item)) 
        self.cal_total()  
        return self.to_dict()
    
    # Reduce item from order.
    def reduce_item(self, item) : # Press the reduce button
        for items in self.__order_detail:
            if item == items.item:
                items - 1
                if items.amount == 0:
                    self.__order_detail.remove(items)
                self.cal_total()
                return self.to_dict()
        return self.to_dict()

    def order_amount(self, item):
        for items in self.__order_detail:
            if items.item == item :
                return items.amount
        return 0

    def show_order_detail(self):
        return [detail.order_detail_dict() for detail in self.__order_detail]
    
    def to_pdf(self):
        return [detail.to_pdf() for detail in self.__order_detail]

    def to_dict(self):
        self.cal_total()
        return {
            "visit_date": self.__visit_date,
            "order_detail": [detail.to_dict() for detail in self.__order_detail],
            "total": self.__total,
            "discount": self.cal_discount()
        }
    
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

class OrderDetail:
    def __init__(self, item):
        self.__item = item # instance of Locker, Cabana, Ticket, Towel
        self.__amount = 1
        self.__total_price = self.__item.price

    @property
    def item(self):
        return self.__item
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def total_price(self):
        return self.__total_price
    
    # def __str__(self):
    #     return f"{self.item} x {self.__amount} = {self.total_price} THB"
    
    def __add__(self, amount = 1):
        if 0 < amount:
            self.__amount += amount
            self.cal_total_price()
        
    def __sub__(self, amount = 1):
        if 0 < amount <= self.__amount:
            self.__amount -= amount
            self.cal_total_price()
        
    def cal_total_price(self):
        self.__total_price = self.__item.price * self.__amount    

    def to_dict(self):
        return {
            "item": self.item.to_dict(),
            "amount": self.__amount,
            "total_price": self.__total_price
        }
    
    def to_pdf(self):
        return {
                "Item Name": self.__item.name(),
                "Price": self.__item.price,
                "Qty": self.__amount,
                "Subtotal": self.__total_price
        }
    