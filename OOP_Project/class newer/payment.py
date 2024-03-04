from datetime import datetime, date

class Payment :
    
    def pay(self):
        return True
    def request_info():
        return None

class BankPayment(Payment) :
    def __init__(self):
        self.__account_no = None

    def pay(self, transaction, acount_no):
        self.__account_no = acount_no
        transaction.status = True
        return True
    
    def request_info(self):
        return {"acount_no": None}

class CardPayment(Payment) :
    def __init__(self):
        self.__card_no = None
        self.__card_pin = None 

    def pay(self, transaction, card_no, card_pin):
        self.__card_no = card_no
        self.__card_pin = card_pin
        transaction.status = True
        return True

    def request_info(self):
        return {
            "card_no": None, 
            "card_pin": None
                }

class PaymentTransaction :
    __id = 0
    def __init__(self, booking, amount, payment_method: Payment, datetime): #
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method
        self.__create_datetime = datetime
        self.__transaction_id = PaymentTransaction.__id
        self.__status = False
        PaymentTransaction.__id += 1

    @property
    def payment_method(self):
        return self.__payment_method
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: bool):
        self.status = status

    def show_payment(self):
        return {
                "request_info": self.__payment_method.request_info(),
                "transaction_id": self.__transaction_id,
                "amount": self.__amount,
                "create_datetime": self.__create_datetime.strftime("%m/%d/%Y, %H:%M:%S")
                }
    def booking_to_pdf_info(self):
        booking = self.__booking
        customer, order = booking.customer, booking.order
        return {
            "Customer": {
                "Name": customer.name,
                "Email": customer.email,
                "Phone Number": customer.phone_no
            },
            "Booking": {
                "Booking Id": booking.booking_id,
                "Date Of Order": booking.order_datetime.strftime("%d %B %Y"),
                "Payment Status": "PAID"
            },
            "Order": {
                "Date Of Visit": order.visit_date.strftime("%d %B %Y"),
                "Total" : order.total,
                "Order Detail": order.show_order_detail()
            }
        }