import datetime
from booking import Booking

class Payment :
    def __init__(self, booking: Booking, datetime):
        if not isinstance(booking, Booking):
            return None
        self.__booking = booking
        self.__transcation_id = None
        self.__status = False
        self.__create_datetime = datetime
        
    @property
    def booking(self):
        return self.__booking

    def gen_payment():
        pass
    def update_status(self, transaction_id):
        self.__status = True
        self.__transcation_id = transaction_id

class Bank(Payment):
    def __init__(self, booking: Booking, datetime):
        Payment.__init__(self, booking, datetime)
        self.type = "Bank"
        self.__account_no = None

    def gen_payment():
        pass
    def update_status(self, transaction_id, account_no):
        Payment.update_status(transaction_id)
        self.__account_no = account_no

class Card(Payment):
    def __init__(self, booking: Booking, datetime):
        Payment.__init__(self, booking, datetime)
        self.__card_no = None
        self.__card_pin = None

    def gen_payment(self, transaction_id, card_no, card_pin):
        Payment.update_status(transaction_id)
        self.__card_no = card_no
        self.__card_pin = card_pin