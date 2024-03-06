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
    
    def update_is_reserve(self, type): # A = Add, R = Remove
        if type == 'A':
            self.__is_reserve = True
        elif type == 'R':
            self.__is_reserve = False
    
class Locker:
    def __init__(self, size, price, remaining_amount):
        self.__size = size
        self.__price = price
        self.__remaining_amount = remaining_amount
    
    def __str__(self):
        return f"Locker: Size {self.__size}"
    
    @property
    def size(self):
        return self.__size
        
    @property
    def price(self):
        return self.__price
    
    @property
    def remaining_amount(self):
        return self.__remaining_amount
    
    def update_remaining_amount(self, type, amount): # A = Add, R = Remove
        if type == 'A':
            self.remaining_amount += amount
        elif type == 'R':
            self.remaining_amount -= amount
                
class Ticket:
    def __init__(self, type, amount_per_ticket, price = 0):
        self.__type = type
        self.__amount_per_ticket = amount_per_ticket
        self.__price = price
        self.__is_thai = True
    
    def __str__(self):
        return f"Ticket: {self.__type}"
    
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
            
class Towel:
    def __init__(self):
        self.__price = 99
        self.__remaining_amount = 5000
    
    def __str__(self):
        return f"Towel: "
        
    @property
    def price(self):
        return self.__price
    
    @property
    def remaining_amount(self):
        return self.__remaining_amount
    
    def update_remaining_amount(self, type, amount): # A = Add, R = Remove
        if type == 'A':
            self.remaining_amount += amount
        elif type == 'R':
            self.remaining_amount -= amount
       
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
