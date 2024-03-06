from booking import Booking, Order
from stock import DailyStock
from datetime import datetime, date
from customer import Customer, Member
from payment import Payment, BankPayment, CardPayment, PaymentTransaction
from datetime import datetime, date
from customerservice import FinishBookingManager
import os
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
        self.__finish_booking_manager = FinishBookingManager()
        
    def selected_payment(self, booking_id, payment_method: Payment):
        booking = self.search_booking_from_id(booking_id)
        order = booking.order
        if order.check_still_availabe() == False:
            self.delete_this_booking(booking) #delete it along with booking
            return "Error"

        order.reserve()
        transaction = PaymentTransaction(booking, order.total, payment_method, datetime.now())
        self.add_transaction(transaction)
        return transaction.show_payment()

    def paid_bill(self, transaction_id, info: dict):
        transaction = self.search_transaction_from_id(transaction_id)
        payment_method = transaction.payment_method
        booking = transaction.booking
        customer = booking.customer
        if isinstance(payment_method, BankPayment):
            payment_method.pay(transaction, info["account_no"])
        elif isinstance(payment_method, CardPayment):
            payment_method.pay(transaction, info["card_no"], info["card_pin"])
        booking.update_status()

        booking_info = transaction.booking_to_pdf_info()
        file_path = os.getcwd() + "\\booking\\"
        self.__finish_booking_manager.create_pdf(booking_info)
        self.__finish_booking_manager.send_email(customer.email, customer.name, booking.booking_id)
        return self.__finish_booking_manager.show_finish_booking(booking.booking_id)

    def cancel_payment(self, transaction_id):
        transaction = self.search_transaction_from_id(transaction_id)
        booking = transaction.booking
        booking.order.cancel_reserve()
        self.delete_this_booking(booking)      # if customer has 1 booking --> delete cus
        self.delete_this_transaction(transaction)   

    def search_booking_from_id(self, id) -> Booking:   #search in customer&&member
        for customer in self.__customer_list:
            for booking in customer.booking_list:
                if booking.id == id:
                    return booking
        for member in self.__member_list:
            for booking in member.booking_list:
                if booking.id == id:
                    return booking
        return None
    def search_transaction_from_id(self, id) -> PaymentTransaction:
        for transaction in self.__transaction_list:
            if transaction.id == id:
                return transaction
        return None

    def add_transaction(self, transaction: PaymentTransaction):
        self.__transaction_list.append(transaction)
    def delete_this_customer(self, customer: Customer):
        if not isinstance(customer, Customer):
            return None
        self.__customer_list.remove(customer)
        return "Done"
    def delete_this_transaction(self, transaction: PaymentTransaction):
        self.__transaction_list.remove(transaction)
        return "Done"
    def delete_this_booking(self, booking: Booking):
        customer = booking.customer
        customer.remove_booking(booking)
        if len(customer.booking_list) == 0 and not isinstance(customer, Member):
            self.delete_this_customer(customer)
        return "Done"





