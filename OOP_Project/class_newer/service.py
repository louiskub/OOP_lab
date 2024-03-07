class Ticket:
    def __init__(self, type, amount_per_ticket, price=0):
        self.__type = type
        self.__amount_per_ticket = amount_per_ticket
        self.__price = price
        self.__is_thai = True
    @property
    def type(self):
        return self.__type
    @property
    def amount(self):
        return self.__amount
    @property
    def is_thai(self):
        return self.__is_thai
    @property
    def price(self):
        if not(self.__is_thai) and self.__price != 0:
            if self.__amount_per_ticket == 1:
                return self.__price + 200                       
            else :
                return self.__price + 150 * self.__amount_per_ticket
        else:
            return self.__price
    def update_is_thai(self, type): # F = Foreign, T = Thai
        if type == 'T':
            self.__is_thai = True
        elif type == 'F':
            self.__is_thai = False
    def name(self):
        return str("Thai " if self.is_thai else "Foreigner ") + self.__type + " Ticket"

class Cabana:
    def __init__(self, id, size, zone):
        self.__id = id
        self.__size = size
        self.__zone = zone
        cabana_price = {'S':899, 'M':1499, 'L':2499}
        for size, price in cabana_price.items():
            if self.__size == size:
                self.__price = price
        self.__is_reserve = False

    def __str__(self):
        return f"Cabana({self.__size}): {self.__zone} Zone"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def size(self):
        return self.__size
    @property
    def zone(self):
        return self.__zone
    
    @property
    def is_reserve(self):
        return self.__is_reserve    
    
    @property    
    def price(self):
        return self.__price
    
    def update_status(self, type): # A = Add, R = Remove
        if type == 'A':
            self.__is_reserve = False
        elif type == 'R':
            self.__is_reserve = True
            
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
    
    def update_status(self, type, amount): # A = Add, R = Remove
        if type == 'A' and 0 < amount:
            self.remaining_amount += amount
        elif type == 'R' and 0 < amount <= self.remaining_amount:
            self.remaining_amount -= amount

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
    
    def update_status(self, type, amount): # A = Add, R = Remove
        if type == 'A' and 0 < amount:
            self.remaining_amount += amount
        elif type == 'R' and 0 < amount <= self.remaining_amount:
            self.remaining_amount -= amount

    def name(self):
        return "Towel"
    