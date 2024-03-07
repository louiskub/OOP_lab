from datetime import datetime, date, timedelta

class Booking:
    __ID = 1
    
    def __init__(self, mem_id, order, booking_date: date):
        self.__id = Booking.__ID
        self.__mem_id = mem_id
        self.__order = order
        self.__booking_date = booking_date
        self.__status = 'Unpaid'
        Booking.__ID += 1
        
    @property
    def id(self):
        return self.__id
    
    @property
    def mem_id(self):
        return self.__mem_id
    
    @property
    def order(self):
        return self.__order
    
    @property
    def booking_date(self):
        return self.__booking_date
    
    @property
    def status(self):
        return self.__status
    
    def update_status(self,sta):
        pass