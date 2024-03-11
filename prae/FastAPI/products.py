class Cabana:
    def __init__(self, id, size, zone):
        self.__id = id
        self.__size = size
        self.__zone = zone
        self.__price = 0
        self.__is_reserve = False
    
    @property
    def id(self):
        return self.__id
    
    @property
    def is_reserve(self):
        return self.__is_reserve
    
    @property
    def zone(self):
        return self.__zone
        
    @property    
    def price(self):
        # standard_price = 899
        # medium_price = 1499
        # large_price = 2499
        cabana_price = {'S':899, 'M':1499, 'L':2499}
        
        for size, price in cabana_price.items():
            if self.__size == size:
                return price
        return 'Error'
    
    def update_is_reserve(self):
        self.__is_reserve = True
    
class Locker:
    def __init__(self, size):
        self.__size = size
        self.__price = 0
    
    @property
    def size(self):
        return self.__size
        
    @property
    def price(self):
        # locker_medium_price = 149
	    # locker_large_price = 229
        locker_price = {'M':149, 'L':229}
        
        for size, price in locker_price.items():
            if self.__size == size:
                return price
        return 'Error'
    
class Ticket:
    def __init__(self, type, amount_per_ticket, price = 0):
        self.__type = type
        self.__amount_per_ticket = amount_per_ticket
        self.__price = price
        self.__is_thai = True
    
    @property
    def type(self):
        return self.__type
    
    @property
    def price(self):
        if not(self.__is_thai) and self.__price != 0:
            if self.__amount_per_ticket == 1:
                return self.__price + 200                       
            else :
                return self.__price + 150 * self.__amount_per_ticket
        else:
            return self.__price
        
    def update_is_thai(self):
        self.__is_thai = False


        
def create_cabana():
    cabana_list = []
    cabana_list.append(Cabana('W01', 'S', 'Wave Pool')) # Wave Pool Zone
    cabana_list.append(Cabana('W02', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('W03', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W04', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W05', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W06', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W07', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W08', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W09', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W10', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('W11', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('W12', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('W13', 'L', 'Wave Pool'))
    cabana_list.append(Cabana('W14', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('W15', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W16', 'M', 'Wave Pool'))
    cabana_list.append(Cabana('W14', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('W14', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('W14', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('P05', 'S', 'Wave Pool'))
    cabana_list.append(Cabana('P06', 'S', 'Wave Pool'))

    cabana_list.append(Cabana('P01', 'S', 'Activity and Relax')) # Activity and Relax Zone
    cabana_list.append(Cabana('P02', 'S', 'Activity and Relax'))
    cabana_list.append(Cabana('P03', 'M', 'Activity and Relax'))
    cabana_list.append(Cabana('P04', 'M', 'Activity and Relax'))

    cabana_list.append(Cabana('H01', 'S', 'Activity and Relax')) # Hill Zone
    cabana_list.append(Cabana('H02', 'S', 'Activity and Relax'))
    cabana_list.append(Cabana('H03', 'S', 'Activity and Relax'))
    cabana_list.append(Cabana('H04', 'M', 'Activity and Relax'))
    cabana_list.append(Cabana('H05', 'M', 'Activity and Relax'))

    cabana_list.append(Cabana('F01', 'M', 'Family')) # Family Zone
    cabana_list.append(Cabana('F02', 'S', 'Family'))
    cabana_list.append(Cabana('F03', 'L', 'Family'))
    cabana_list.append(Cabana('F04', 'S', 'Family'))
    cabana_list.append(Cabana('F05', 'M', 'Family'))
    cabana_list.append(Cabana('F06', 'M', 'Family'))
    cabana_list.append(Cabana('K05', 'M', 'Family'))
    cabana_list.append(Cabana('K06', 'M', 'Family'))
    cabana_list.append(Cabana('K07', 'S', 'Family'))
    
    return cabana_list

def create_locker():
    locker_list = []
    locker_list.append(Locker('M')) # Locker
    locker_list.append(Locker('L'))
    
    return locker_list
    
def create_ticket():
    ticket_list = []
    
    # Solo Ticket
    ticket_list.append(Ticket('Full Day', 1, 699))
    ticket_list.append(Ticket('Senior', 1, 599)) # >= 60 y.o. and want to play slides
    ticket_list.append(Ticket('Child', 1))
    ticket_list.append(Ticket('SPD', 1)) # including pregnant and disabled 

    # Group Ticket
    ticket_list.append(Ticket('Group for 4', 4, 2599))
    ticket_list.append(Ticket('Group for 6', 6, 3779))
    ticket_list.append(Ticket('Group for 8', 8, 4879))
    ticket_list.append(Ticket('Group for 10', 10, 5999))
    
    return ticket_list