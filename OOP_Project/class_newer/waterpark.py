from booking import Booking
from stock import DailyStock, Stock
from service import Ticket, Cabana, Locker, Towel
from datetime import datetime, timedelta, date
from customer import Customer, Member
from payment import Payment, BankPayment, CardPayment, PaymentTransaction
from bookingmanager import FinishBookingManager
from fastapi.responses import RedirectResponse
from order import Order, OrderDetail
from copy import deepcopy

class WaterPark:
    def __init__(self):
        self.__name = "rama"
        self.__stock = Stock()
        self.__daily_stock_list = create_daily_stock()
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
        return None 
    
    def search_daily_stock_from_date(self, date):
        for daily in self.__daily_stock_list:
            if date == daily.date:
                return daily
        return None  
    
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
    
    def show_confirm(self, member_id, booking_id):
        member = self.search_member_from_id(member_id)
        booking = self.search_booking_from_member(member, booking_id)
    
    def selected_payment(self, booking_id, payment_method: int):
        booking = self.search_booking_from_id(booking_id)
        if not isinstance(booking, Booking):
            return "Error"
        order = booking.order
        transaction = PaymentTransaction(booking, order.total, deepcopy(self.__payment_list[payment_method]), datetime.now())
        self.add_transaction(transaction)
        #show_payment/{transaction.transaction_id}
        #print(transaction.id)
        path = "bank" if payment_method==0 else "card"
        return RedirectResponse(url=f'/show_payment/{transaction.id}/{path}', status_code=200)

    def show_payment(self, transaction_id, method_type):
        # info = {
        #     "account_no": "902138013"
        #     "paid_time" : "datetime"
        # }
        transaction = self.search_transaction_from_id(transaction_id)
        if transaction == None :
            return RedirectResponse('/pagenotfound', status_code=404)
        if transaction.status == True:
            return RedirectResponse('/', status_code=404)
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
        self.__finish_booking_manager.send_email(customer.email, customer.name, booking.id)
        return RedirectResponse(url=f'/finish_booking/{transaction_id}', status_code=200)  
    
    def show_finish_booking(self, transaction_id):
        transaction = self.search_transaction_from_id(transaction_id)
        if not isinstance(transaction, PaymentTransaction) or transaction.status == False:
            return RedirectResponse('/pagenotfound', status_code=200)
        booking = transaction.booking
        return self.__finish_booking_manager.show_finish_booking(booking.id)
    
    def search_booking_from_id(self, id) -> Booking:   #search in customer&&member
        for member in self.__member_list:
            for booking in member.booking_list:
                if booking.id == id:
                    return booking
        return None
    
    def search_booking_from_member(self, member, booking_id):
        for booking in member.booking_list:
            if booking.id == booking_id:
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
    def add_member(self, member: Member):
        self.__member_list.extend(member)

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
    
    def get_member_list(self):
        return self.__member_list
def create_member():
    return [ Member("James", "james123@gmail.com", "0812345678", date(2001,2,14), "12xncvbj34")
    ,Member("Yuji", "yuji1234@gmail.com", "0823456789", date(2002,1,3), "1xbv3z234")
    ,Member("Irene", "irene123@gmail.com", "0834567890", date(2003,4,2), "jdies234")
    ,Member("Charlotte", "charlotte@gmail.com", "0845678901", date(2004,1,4), "w.sa12sm.34")
    ,Member("Sharon", "sharon12@gmail.com", "0856789012", date(1998,12,1), "1ksl23aqo4")
    ,Member("Rose", "rose1234@gmail.com", "0867890123", date(1999,6,1), "sznkal34")
    ,Member("Lucian", "lucian123@gmail.com", "0878901234", date(2000,1,1), "2.lasm_p4")
    ,Member("Zeno", "zeno1234@gmail.com", "0889012345", date(2005,9,1), "1splalr0es3")
    ,Member("Apollo", "apollo12@gmail.com", "0890123456", date(2006,3,1), "wqygwoaqr234")
    ,Member("Lucian", "lucian123@gmail.com", "0801234567", date(1997,10,1), "teosrl_234")
    ,Member("Dion", "dion1234@gmail.com", "0898765432", date(1996,1,1), "sjgflxlsj_t") ]

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

def create_daily_stock():
    today = date.today()
    lst = []
    for i in range(60) :
        lst.append(DailyStock(today + timedelta(days=i)))
    return lst

def create_booking(member):
    t = Ticket('Full Day', 1, 699)
    c = Cabana('W01', 'S', 'Wave Pool')
    order = Order(date.today()+ timedelta(days=3))
    order.add_item(t)
    order.add_item(t)
    order.add_item(c)
    order.add_item(c)
    c = create_member()
    booking = Booking(member, order, date.today())
    #print(booking.to_dict())
    return booking

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

# if '__main__' == __name__ :
    
#     # create_booking()