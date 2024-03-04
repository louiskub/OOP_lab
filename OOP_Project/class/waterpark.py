from booking import Booking, Order
from stock import DailyStock
from datetime import datetime
from customer import Customer, Member
from payment import Payment, BankPayment, CardPayment, Transaction
from datetime import datetime, date
from reportlab.pdfgen import canvas

class WaterPark:
    def __init__(self, name):
        self.__name = name
        self.__stock = None
        self.__daily_stock_list = []
        self.__customer_list = []
        self.__member_list = []
        self.__promotion_list = []
        self.__reward_list = []
        self.__payment_list = [BankPayment(), CardPayment()]
        self.__transaction_list = []
        

    def selected_payment(self, booking_id, type):
        booking = self.search_booking_from_id(booking_id)
        order, customer = booking.order, booking.customer
        dailystock = self.search_dailystock_from_date(order.visit_date)
        if dailystock.check_still_available(order) == False :
            self.delete_this_booking(booking)
            if not isinstance(customer, Member):
                self.delete_this_customer(customer)
            return "Now is not available anymore"
        dailystock.reserve(order)
    
        payment_method = self.create_payment_from_type(type, booking)
        transaction = Transaction(booking, order.total, payment_method, datetime.now())
        self.add_payment(transaction)
        return transaction.show_payment()

    # def paid_bill(self, payment_id, info: dict):   # success paid
    #     payment = self.search_payment_from_id(payment_id)
    #     if isinstance(payment, Bank):
    #         pass #payment.update_status(transaction_id,"account_no")
    #     elif isinstance(payment, Card):
    #         pass

    def search_booking_from_id(self, id):
        for booking in self.__booking_list:
            if booking.booking_id == id : 
                return booking
        return None
    
    def search_dailystock_from_date(self, date):
        for dailystock in self.__daily_stock_list :
            if dailystock.date == date :
                return dailystock
        dailystock = DailyStock(date)
        self.__daily_stock_list.append(dailystock)
        return dailystock
    
    def delete_this_booking(self, booking: Booking):
        if not isinstance(booking, Booking):
            return None
        self.__booking_list.remove(booking)
        return "Done"
    
    def delete_this_customer(self, customer: Customer):
        if not isinstance(customer, Customer):
            return None
        self.__customer_list.remove(customer)
        return "Done"
    
    def create_payment_from_type(self, type: int, booking: Booking): #type int, 1=Bank 2=Card
        if not isinstance(booking, Booking):
            return None
        if int(type) == 1:
            return BankPayment()
        elif int(type) == 2:
            return CardPayment()
        else : 
            return None
    
    def add_payment(self, payment: Payment):
        if not isinstance(payment, Payment):
            return None
        self.__payment_list.append(payment)
        return "Done"
    
    def show_payment(self, payment: Payment):
        if not isinstance(payment, Payment):
            return None
        return 
    def add_booking(self, booking: Booking):
        self.__booking_list.append(booking)
        return "Done"
    
    def search_payment_from_id(self, id):
        for payment in self.__payment_list:
            if payment.id == id :
                return payment
        return None
    
    def send_finished_booking():
        pass
    def create_booking_file():
        pass

    def cancel_all(self, payment_id):
        payment = self.__search_payment_from_id(payment_id)
        booking = payment.booking
        self.delete_this_payment(payment)
        order = booking.order  
        dailystock = self.search_dailystock_from_date(order.date)
        dailystock.cancel(order)
        if not isinstance(order.customer, Member):
            self.delete_this_customer(order.customer)
        self.delete_this_booking(booking)
        return "Done"


    def delete_this_payment(self, payment: Payment):
        self.__payment_list.remove(payment)
        return "Done"
    

