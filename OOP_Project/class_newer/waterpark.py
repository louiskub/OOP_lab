from booking import Booking, Order
from stock import DailyStock, Stock
from service import Ticket, Cabana, Locker, Towel
from datetime import datetime, timedelta, date
from customer import Customer, Member
from payment import Payment, BankPayment, CardPayment, PaymentTransaction
from bookingmanager import FinishBookingManager
from fastapi.responses import RedirectResponse
class WaterPark:
    def __init__(self):
        self.__name = "rama"
        self.__stock = Stock()
        self.__daily_stock_list = []
        self.__zone_list = ['Wave Pool', 'Activity and Relax', 'Hill', 'Family']
        self.__customer_list = []
        self.__member_list = []
        self.__promotion_list = []
        self.__payment_list = [BankPayment(), CardPayment()]
        self.__transaction_list = []
        self.__finish_booking_manager = FinishBookingManager()
    def get_member_list(self):
        return self.__member_list
    def add_daily_stock(self, daily):
        self.__daily_stock_list.append(daily)    
        
    def add_member(self, member):
        if isinstance(member, Member):
            self.__member_list.append(member)
        else: return 'Error'     
        
    def search_member_from_id(self, id):
        for member in self.__member_list:
            if id == member.id:
                return member
        return 'Not Found' 
    
    def search_daily_stock_from_date(self, date):
        for daily in self.__daily_stock_list:
            if date == daily.date:
                return daily
        return 'Not Found'  
    
    def get_services_in_stock(self, stock):
        services = {}
        services["Ticket"] = stock.ticket_list
        services["Cabana"] = stock.cabana_list
        services["Locker"] = stock.locker_list
        services["Towel"] = stock.towel
        return services    
        
    def get_all_services(self) : # When press services button
        return self.get_services_in_stock(self.__stock)
        
    def get_services_in_date(self, date): # After selected date
        daily_stock = self.search_daily_stock_from_date(date)
        return self.get_services_in_stock(daily_stock)
    
    def get_zone(self):
        return self.__zone_list
    
    def get_cabana_in_zone(self, date):
        daily_stock = self.search_daily_stock_from_date(date)
        cabana_in_zone = {}
        for zone in self.__zone_list:
            cabana_in_zone[zone] = daily_stock.get_cabana_in_zone(zone)
        return cabana_in_zone
    
    def create_order(self, date):
        return Order(date)
    
    def add_item(self, item, order): # Press (+) button.
        daily_stock = self.search_daily_stock_from_date(order.visit_date)
        if daily_stock.is_available(item, 1):
            order.add_item(item)
        return order
    
    def remove_item(self, item, order): # Press (-) button.
        return order.remove_item(item)
    
    def become_member(self, name, email, phone_number, birthday, password):
        for member in self.__member_list:
            if email == member.email or phone_number == member.phone_number:
                return 'You are already a member.' 
        if Member.check_email(email):
            if Member.check_phone_number(phone_number) and len(phone_number) == 10:
                if Member.check_password(password) and len(password) >= 8:
                    self.add_member(Member(name, email, phone_number, birthday, password))
                    return 'Membership registration completed.'
                return 'Please use a password with at least 8 characters and only the letters 0-9, a-z, A-Z, or (.)'
            return 'Fill the correct phone number.'
        return 'Fill the correct email.'                 

    def verify_member(self, email, password):
        for member in self.__member_list:
            member.verify_member(email, password)
        return 'Email or password is incorrect.'
    
    

    def selected_payment(self, booking_id, payment_method: int):
        booking = self.search_booking_from_id(booking_id)
        if not isinstance(booking, Booking):
            return "Error"
        order = booking.order
        if order.check_still_availabe() == False:
            self.delete_this_booking(booking) #delete it along with booking
            return RedirectResponse('/', status_code=200)

        transaction = PaymentTransaction(booking, order.total, self.__payment_list[payment_method], datetime.now())
        self.add_transaction(transaction)
        return RedirectResponse(url=f'/show_payment/{transaction.transaction_id}', status_code=200)
    def show_payment(self, transaction_id):
        # info = {
        #     "account_no": "902138013"
        #     "paid_time" : "datetime"
        # }
        transaction = self.search_transaction_from_id(transaction_id)
        if transaction == None :
            return RedirectResponse('/pagenotfound', status_code=404)
        return transaction.show_payment()
    def cancel_payment(self, transaction_id, transaction: PaymentTransaction = None):
        if transaction == None :
            transaction = self.search_transaction_from_id(transaction_id)
        booking = transaction.booking
        self.delete_this_booking(booking)      # if customer has 1 booking --> delete cus
        self.delete_this_transaction(transaction)   
        return RedirectResponse('/', status_code=200)
    def paid_bill(self, transaction_id, info: dict):
        transaction = self.search_transaction_from_id(transaction_id)
        booking, payment_method = transaction.booking, transaction.payment_method
        customer, order = booking.customer, booking.order
        if order.check_still_availabe() == False:
            return self.cancel_payment(transaction_id, transaction)
        order.reserve()
        payment_method.pay(transaction, info)
        booking.update_status()
        booking_info = transaction.booking_to_pdf_info()
        self.__finish_booking_manager.create_pdf(booking_info)
        self.__finish_booking_manager.send_email(customer.email, customer.name, booking.booking_id)
        return RedirectResponse(url=f'/finish_booking/{transaction_id}', status_code=200)  
    def show_finish_booking(self, transaction_id):
        transaction = self.search_transaction_from_id(transaction_id)
        if not isinstance(transaction, PaymentTransaction) or transaction.status == False:
            return RedirectResponse('/pagenotfound', status_code=200)
        booking = transaction.booking
        return self.__finish_booking_manager.show_finish_booking(booking.booking_id)
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
    def add_daily_stock(self, dailystock: DailyStock):
        self.__daily_stock_list.append(dailystock)
    def add_customer(self, customer: Customer):
        self.__customer_list.append(customer)
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

def create_customer():
    return [ Customer("James", "james123@gmail.com", "0812345678")
    ,Customer("Yuji", "yuji1234@gmail.com", "0823456789")
    ,Customer("Irene", "irene123@gmail.com", "0834567890")
    ,Customer("Charlotte", "charlotte@gmail.com", "0845678901")
    ,Customer("Sharon", "sharon12@gmail.com", "0856789012")
    ,Customer("Rose", "rose1234@gmail.com", "0867890123")
    ,Customer("Lucian", "lucian123@gmail.com", "0878901234")
    ,Customer("Zeno", "zeno1234@gmail.com", "0889012345")
    ,Customer("Apollo", "apollo12@gmail.com", "0890123456")
    ,Customer("Lucian", "lucian123@gmail.com", "0801234567")
    ,Customer("Dion", "dion1234@gmail.com", "0898765432") ]


def constructor():
    dkub = WaterPark()
    today = date.today()
    for i in range(60) :
        dkub.add_daily_stock(DailyStock(today + timedelta(days=i)))
    my_order = dkub.create_order(date.today())
    daily_stock = dkub.search_daily_stock_from_date(my_order.visit_date)
    towel = daily_stock.towel   
    for locker in daily_stock.locker_list: # choose locker
        locker_L = locker
    for ticket in daily_stock.ticket_list: # choose ticket
        my_ticket = ticket
        
    dkub.add_item(towel, my_order)
    dkub.add_item(towel, my_order)
    dkub.add_item(towel, my_order)
    dkub.add_item(locker_L, my_order)
    dkub.add_item(my_ticket, my_order)
    dkub.remove_item(towel, my_order)


    customer_list = create_customer()
    [dkub.add_customer(customer) for customer in customer_list]
    return (dkub, customer_list)
# constructor()