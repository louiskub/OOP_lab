from datetime import datetime

class Payment :
    def pay(self):
        return True
    
    def request_info():
        return None

class BankPayment(Payment) :
    def __init__(self):
        self.__account_no = None
        self.__bank_name = None

    def pay(self, transaction, info):
        info = info.dict()
        self.__account_no = info["account_no"]
        self.__bank_name = info["bank_name"]
        transaction.status = True
        transaction.set_payment_datetime()
        transaction.payment_method = self
        return True

class CardPayment(Payment) :
    def __init__(self):
        self.__card_no = None
        self.__card_pin = None 

    def pay(self, transaction, info):
        info = info.dict()
        self.__card_no = info["card_no"]
        self.__card_pin = info["card_pin"]
        transaction.status = True
        transaction.set_payment_datetime()
        transaction.payment_method = self
        return True

class PaymentTransaction :

    __id = 100000

    def __init__(self, booking_id, amount): #
        self.__id = PaymentTransaction.__id
        self.__booking_id = booking_id
        self.__amount = amount
        self.__payment_method = None
        self.__payment_datetime = None
        self.__status = False
        PaymentTransaction.__id += 1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def payment_method(self):
        return self.__payment_method
    
    @property
    def status(self):
        return self.__status

    @payment_method.setter
    def payment_method(self, payment_method: Payment):
        self.__payment_method = payment_method

    @status.setter
    def status(self, status: bool):
        self.__status = status
        
    def set_payment_datetime(self):
        self.__payment_datetime = datetime.now()

    # def show_payment(self, payment_method):
    #     return {
    #             "transaction_id": str(self.__id),
    #             "amount": str(self.__amount),
    #             "create_datetime": self.__create_datetime,
    #             "payment_method": payment_method
    #     }