class Ticket:
    def __init__(self, type, amount_per_ticket, price=0):
        self.__type = type
        self.__amount_per_ticket = amount_per_ticket
        self.__price = price
        self.__is_thai = True
    @property
    def price(self):
        if not (self.__is_thai) and self.__price != 0:
            return self.__price + 200
        else:
            return self.__price

    def update_is_thai(self):
        self.__is_thai = False
    def name(self):
        return "Thai " if self.is_thai else "Foreigner " + self.__type + " Ticket"

class Cabana:
    def __init__(self, id, size, zone):
        self.__id = id
        self.__size = size
        self.__zone = zone
        self.__price = 0
        self.__is_reserve = False

    @property
    def price(self):
        return self.__price
    @property
    def is_reseve(self):
        return self.__is_reserve
    @is_reseve.setter
    def is_reserve(self, reserve: bool):
        self.__is_reserve = reserve
    def name(self):
        return f"Cabana Zone {self.__zone} Size {self.__size}"

class Locker:
    def __init__(self, size, remaining_amount=80):
        self.__size = size
        self.__remaining_amount = remaining_amount
        if size == 'M' :
            self.__price = 149
        elif size == "L" :
            self.__price = 229
    @property
    def price(self):
        return self.__price
    @property
    def size(self):
        return self.__size
    @property
    def remaining_amount(self):
        return self.__remaining_amount
    def name(self):
        return f"Locker Size {self.__size}"

class Towel:
    def __init__(self, remaining_amount=100):
        self.__remaining_amount = remaining_amount
        self.__price = 99
    @property
    def price(self):
        return self.__price
    @property
    def remaining_amount(self):
        return self.__remaining_amount
    def name():
        return "Towel"
    

class OrderDetail:
    def __init__(self, item, amount):
        self.__item = item #instance of Locker, Cabana, Ticket
        self.__amount = amount
        self.__total = 0

    @property
    def item(self):
        return self.__item
    @property
    def amount(self):
        return self.__amount
    @property
    def total(self):
        return self.__total
    def cal_total(self):
        self.__total = self.__item.price * self.__amount
    def order_detail_dict(self):
        return {
            "Item Name": self.__item.name(),
            "Price": self.__item.price,
            "Qty": self.__amount,
            "Subtotal": self.__total
        }
    