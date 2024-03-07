from booking import Booking
from stock import DailyStock, Stock
from service import Ticket, Cabana, Locker, Towel
from datetime import datetime, timedelta, date
from customer import Customer, Member
from payment import Payment, BankPayment, CardPayment, PaymentTransaction
from bookingmanager import FinishBookingManager
from order import Order, OrderDetail
from promotion import Promotion, AmountCoupon, PercentCoupon
from copy import deepcopy
from starlette import status

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
    
    def get_zone(self):
        return self.__zone_list
    
    @property
    def payment_list(self):
        return self.__payment_list
    
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
    
    def format_str_to_date(self, str_date): # If input date as string.
        try:
            selected_date = date.fromisoformat(str_date)
            return selected_date
        except ValueError:
            return None

    def get_services_in_stock(self, stock):
        services = {}
        services["Ticket"] = stock.ticket_list
        services["Cabana"] = {}
        for zone in self.__zone_list:
            services["Cabana"][zone] = stock.get_cabana_in_zone(zone)
        services["Locker"] = stock.locker_list
        services["Towel"] = stock.towel
        return services     
    
    def get_cabana_in_zone(self, date):
        daily_stock = self.search_daily_stock_from_date(date)
        cabana_in_zone = {}
        for zone in self.__zone_list:
            cabana_in_zone[zone] = daily_stock.get_cabana_in_zone(zone)
        return cabana_in_zone
    
    def find_item(self, daily_stock, item: dict):
        item = item.dict()
        if item['name'] == 'cabana':
            for cabana in daily_stock.get_cabana_in_zone(item['zone']):
                if item['id'] == cabana.id:
                    return cabana
        elif item['name'] == 'locker':
            for locker in daily_stock.locker_list:
                if locker.size == item['size']:
                    return locker
        elif item['name'] == 'ticket':
            for ticket in daily_stock.ticket_list:
                if ticket.type == item['type']:
                    return ticket
        elif item['name'] == 'towel':
            return daily_stock.towel
        return None
    
    def manage_order(self, member_id: int, date: str, items, type): # type A = Add, R = Reduce
        selected_date = self.format_str_to_date(date)
        member = self.search_member_from_id(member_id)
        if selected_date != None:
            if member != None:
                order = member.get_order_from_visit_date(selected_date)
                daily_stock = self.search_daily_stock_from_date(selected_date)
                item = self.find_item(daily_stock, items)
                if item != None:
                    if type == 'A' and daily_stock.is_available(item, 1): # Press (+) button.
                        return order.add_item(item)
                    elif type == 'R': # Press (-) button.
                        return order.reduce_item(item)
                    return 'Invalid type. Please choose A(Add) or R(Reduce).'
                return 'Invalid item.'
            return 'Invalid member id.'
        return "Invalid date format. Please use ISO format (YYYY-MM-DD)."

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
    

    #def apply_code(self, member_id: int):


    def show_confirm(self, member_id: int):
        member = self.search_member_from_id(member_id)
        if member.order == None:
            return "No Order"
        member.booking_temp = Booking(member_id, member.order, date.today())
        return {
            "member" : member.to_dict(),
            "booking": member.booking_temp.to_dict()
        }

    def show_payment(self, member_id: int, payment_method: str):
        member = self.search_member_from_id(member_id)
        booking = member.booking_temp
        if booking == None:
            return "No booking"
        return {
            "booking_id": booking.id,
            "amount": str(booking.order.total),
            "payment_method": payment_method
        }
    
    def paid(self, member_id: int, info, payment_method):
        member = self.search_member_from_id(member_id)
        booking = member.booking_temp
        order = booking.order
        date = order.visit_date
        dailystock = self.search_daily_stock_from_date(date)
        if booking == None:
            return "booking not found"
        if self.is_available(order, dailystock) == False:
            member.booking_temp = None
            member.order = None
            return "delete success"
        self.update_dailystock(order, dailystock)
        payment_method = deepcopy(self.payment_list[payment_method]) #bankpayment
        transaction = PaymentTransaction(booking.id, booking.order.total)
        payment_method.pay(transaction, info)
        self.add_transaction(transaction)
        booking.update_status()
        member.add_booking(booking)
        booking_info = self.booking_to_pdf(member)
        member.booking_temp, member.order = None, None
        self.__finish_booking_manager.create_pdf(booking_info)
        return f"pay success {member.id}, {booking.id}"
    
    def show_finish_booking(self, member_id, booking_id):
        member = self.search_member_from_id(member_id)
        if member==None:
            return "mem not found"
        if self.search_booking_from_member(member, booking_id) == None:
            return "booking not found"
        return self.__finish_booking_manager.view_finish_booking(booking_id)

    def search_promotion_from_code(self, code: str):
        code = code.upper()
        for promotion in self.__promotion_list:
            if promotion.code == code:
                return promotion
        return None

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
            print(transaction.id)
            if transaction.id == id:
                return transaction
        return None
    def is_available(self, order, dailystock):
        for detail in order.order_detail:
            if dailystock.is_available(detail.item, detail.amount) == False:
                return False
        return True
    
    def update_dailystock(self, order, dailystock):
        for detail in order.order_detail:
            dailystock.update_item(detail.item, detail.amount)

    def add_transaction(self, transaction: PaymentTransaction):
        self.__transaction_list.append(transaction)
    def add_daily_stock(self, dailystock: DailyStock):
        self.__daily_stock_list.append(dailystock)
    def add_member(self, member: Member):
        self.__member_list.extend(member)
    def add_promotion(self, promotion: Promotion):
        self.__promotion_list.extend(promotion)    
    def get_member_list(self):
        return self.__member_list
    
    def booking_to_pdf(self, member):
        booking = member.booking_temp
        order = booking.order
        return {
            "Customer": {
                "Name": member.name,
                "Email": member.email,
                "Phone Number": str(member.phone_no)
            },
            "Booking": {
                "Booking Id": booking.id,
                "Date Of Order": booking.order_datetime.strftime("%d %B %Y"),
                "Payment Status": "PAID"
            },
            "Order": {
                "Date Of Visit": order.visit_date.strftime("%d %B %Y"),
                "Total" : order.total,
                "Order Detail": order.to_pdf()
            }
    }



def create_promotion():
    return [
        AmountCoupon(date.today()-timedelta(days=1) ,date.today()+timedelta(days=3) , "35IWK0M5" , 200, 1000),
        AmountCoupon(date.today()-timedelta(days=5) ,date.today()+timedelta(days=4) , "O1KSXG0X" , 300, 1000),
        AmountCoupon(date.today()-timedelta(days=10) ,date.today()+timedelta(days=5) , "QLC6EBTS" , 350, 2000),
        AmountCoupon(date.today()+timedelta(days=20) ,date.today()-timedelta(days=7) , "VBH7P77F" , 300, 2000),
        PercentCoupon(date.today()-timedelta(days=1) ,date.today()+timedelta(days=3) , "DU4LY3HV" , 10),
        PercentCoupon(date.today()-timedelta(days=5) ,date.today()+timedelta(days=4) , "IV3WLCHW" , 15),
        PercentCoupon(date.today()-timedelta(days=10) ,date.today()+timedelta(days=5) , "VROPTVOJ" , 20, 2500),
        PercentCoupon(date.today()+timedelta(days=20) ,date.today()-timedelta(days=7) , "UCJHSTWQ" , 30)
    ]
def create_member():
    return [ 
        Member("James", "james123@gmail.com", "0812345678", date(2001,2,14), "12xncvbj34")
        ,Member("Yuji", "66010660@kmitl.ac.th", "0823456789", date(2002,1,3), "1xbv3z234")
        ,Member("Irene", "irene123@gmail.com", "0834567890", date(2003,4,2), "jdies234")
        ,Member("Charlotte", "charlotte@gmail.com", "0845678901", date(2004,1,4), "w.sa12sm.34")
        ,Member("Sharon", "sharon12@gmail.com", "0856789012", date(1998,12,1), "1ksl23aqo4")
        ,Member("Rose", "rose1234@gmail.com", "0867890123", date(1999,6,1), "sznkal34")
        ,Member("Lucian", "lucian123@gmail.com", "0878901234", date(2000,1,1), "2.lasm_p4")
        ,Member("Zeno", "zeno1234@gmail.com", "0889012345", date(2005,9,1), "1splalr0es3")
        ,Member("Apollo", "apollo12@gmail.com", "0890123456", date(2006,3,1), "wqygwoaqr234")
        ,Member("Lucian", "lucian123@gmail.com", "0801234567", date(1997,10,1), "teosrl_234")
        ,Member("Dion", "dion1234@gmail.com", "0898765432", date(1996,1,1), "sjgflxlsj_t") 
    ]

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
    locker_list = [Locker('M', 149, 80), Locker('L', 229, 20)]
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
    for i in range(60):
        lst.append(DailyStock(today + timedelta(days=i)))
    return lst

def create_order():
    t = Ticket('Full Day', 1, 699)
    c = Cabana('W01', 'S', 'Wave Pool')
    order = Order(date.today()+ timedelta(days=3))
    order.add_item(t)
    order.add_item(t)
    order.add_item(c)
    order.add_item(c)
    return order

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


    # customer_list = create_customer()
    # [dkub.add_customer(customer) for customer in customer_list]
    # return (dkub, customer_list)
# constructor()

# if '__main__' == __name__ :
    
#     # create_booking()