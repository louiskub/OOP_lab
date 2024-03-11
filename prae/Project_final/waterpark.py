from booking import Booking
from stock import DailyStock, Stock
from services import Ticket, Cabana, Locker
from datetime import timedelta, date
from member import  Member
from payment import BankPayment, CardPayment, PaymentTransaction
from bookingmanager import FinishBookingManager
from order import Order
from promotion import Promotion, AmountCoupon, PercentCoupon
from copy import deepcopy
#from starlette import status

class WaterPark:
    def __init__(self):
        Member._Member__ID = 100000
        self.__name = "Rama"
        self.__stock = Stock()
        self.__daily_stock_list = create_daily_stock()
        self.__zone_list = ["Wave Pool", "Activity and Relax", "Hill", "Family"]
        self.__member_list = create_member()
        self.__promotion_list = create_promotion()
        self.__payment_list = [BankPayment(), CardPayment()]
        self.__transaction_list = []
        self.__finish_booking_manager = FinishBookingManager()

    # Get information of system.
    def get_stock(self):
        return self.__stock
    
    def get_zone_list(self):
        return self.__zone_list
    
    def get_daily_stock(self):
        return self.__daily_stock_list

    # Add information to system.    
    def add_daily_stock(self, daily):
        if isinstance(daily, DailyStock):
            self.__daily_stock_list.append(daily)   
        else: return "Error"  
        
    def add_member(self, member):
        if isinstance(member, Member):
            self.__member_list.append(member)
        else: return "Error"      

    def add_promotion(self, promotion):
        if isinstance(promotion, Promotion):
            self.__promotion_list.extend(promotion) 
        else: return "Error"

    def add_transaction(self, transaction):
        if isinstance(transaction, PaymentTransaction):
            self.__transaction_list.append(transaction)  
        else: return "Error"   
    
    # Search for instance.
    def search_member_from_id(self, id): # find instance of member
        for member in self.__member_list:
            if id == member.id:
                return member
        return None 
    
    def search_member_from_email(self, email):
        for member in self.__member_list:
            if email == member.email:
                return member
        return None 
    
    def search_daily_stock_from_date(self, date): # find instance of daily stock 
        for daily in self.__daily_stock_list:
            if date == daily.date:
                return daily
        return None 

    def search_promotion_from_code(self, code: str): # find instance of coupon
        code = code.upper()
        for promotion in self.__promotion_list:
            if promotion.code == code:
                return promotion
        return None

    # def search_booking_from_id(self, id) -> Booking:   # find instance of booking
    #     for member in self.__member_list:
    #         for booking in member.booking_list:
    #             if booking.id == id:
    #                 return booking
    #     return None
    
    def search_booking_from_member(self, member, booking_id): # find instance of booking
        for booking in member.booking_list:
            if booking.id == booking_id:
                return booking
        return None

    def search_transaction_from_id(self, id): # find instance of payment transaction
        for transaction in self.__transaction_list:
            if transaction.id == id:
                return transaction
        return None

    def find_item(self, daily_stock, item: dict): # find instance of selected item
        item = item.dict()
        if item["name"] == None:
            return None
        if item["name"] == "cabana":
            for cabana in daily_stock.get_cabana_in_zone(item["zone"]):
                if item["id"].upper() == cabana.id and item["id"].upper() != None:
                    return cabana
            return None
        elif item["name"] == "locker":
            for locker in daily_stock.locker_list:
                if locker.size == item["size"].upper() and item["size"].upper() != None:
                    return locker
            return None
        elif item["name"] == "ticket":
            for ticket in daily_stock.ticket_list:
                if ticket.type == item["type"] and item["type"] != None:
                    return ticket
            return None
        elif item["name"] == "towel":
            return daily_stock.towel
        return None 

    # Change format of date from string.
    def format_str_to_date(self, str_date): # if input date as string.
        try:
            selected_date = date.fromisoformat(str_date)
            return selected_date
        except ValueError:
            return None

    
    # ## delete member ##
    # def delete_member(self, member_id):
    #     for member in self.__member_list:
    #         if member_id == member.id:
    #             self.__member_list.remove(member)
    #             return [member.id for member in self.__member_list]
    #     return [member.id for member in self.__member_list]
    
    # Log in
    def login_member(self, email, password):
        for member in self.__member_list:
            result = member.verify_member(email, password)
            if result != None:
                member_id = member.verify_member(email, password).id
                return f"Login successful." # return member id
        return "Email or password is incorrect."  
    
    # Subscription
    def become_member(self, name = None, email = None, phone_number = None , birthday = None, password = None):
        for member in self.__member_list:
            if email == member.email or phone_number == member.phone_no:
                return "You are already a member." 
        error = {}
        if Member.check_email(email) == False:
            error["email"] = "Fill the correct email."
        if Member.check_phone_number(phone_number) == False and len(phone_number) != 10:
            error["phone"] = "Fill the correct phone number."
        if Member.check_password(password) == False and len(password) < 8:
            error["password"] = "Password must be at least 8 characters and only the letters 0-9, a-z, A-Z, (.) or (_)."
        if len(error) > 0:
            return error
        self.add_member(Member(name, email, phone_number, birthday, password))
        return "Membership registration completed."

    # Get services information.
    # def get_cabana_in_zone(self, date = None):
    #     if date != None:
    #         stock = self.search_daily_stock_from_date(date)
    #     else: stock = self.__stock
    #     cabana_in_zone = {}
    #     for zone in self.__zone_list:
    #         cabana_in_zone[zone] = stock.get_cabana_in_zone(zone)
    #     return cabana_in_zone 
    
    def get_all_services(self):
        return self.get_services_in_stock(self.__stock)
    
    def get_services_in_date(self, date):
        selected_date = self.format_str_to_date(date)
        if selected_date == None:
            return "Invalid date format. Please use ISO format (YYYY-MM-DD)."
        daily_stock = self.search_daily_stock_from_date(selected_date)
        if daily_stock == None:
            return "Not available date. Please select a new date."
        return self.get_services_in_stock(daily_stock)
    
    def get_services_in_stock(self, stock):
        services = {}
        services["ticket"] = [ticket.to_dict() for ticket in stock.ticket_list]
        services["cabana"] = {}
        for zone in self.__zone_list:
            services["cabana"][zone] =  [cabana.to_dict() for cabana in stock.get_cabana_in_zone(zone)]
        services["locker"] = [locker.to_dict() for locker in stock.locker_list]
        services["towel"] = stock.towel.to_dict()
        return services 
    
    # Add or Reduce item from order.
    def manage_order(self, member_id: int, date: str, items, type): # type A = Add, R = Reduce
        selected_date = self.format_str_to_date(date)
        member = self.search_member_from_id(member_id)
        if selected_date == None:
            return "Invalid date format. Please use ISO format (YYYY-MM-DD)."
        if member == None:
            return "Invalid member id."
        order = member.get_order_from_visit_date(selected_date)
        if order == None:
            return "Order not found."
        daily_stock = self.search_daily_stock_from_date(selected_date)
        if daily_stock == None or selected_date < date.today():
            return "Please select the available date."
        item = self.find_item(daily_stock, items)
        if item != None: 
            if type == "A" and daily_stock.is_available(item, 1): # Press (+) button.
                return order.add_item(item)
            elif type == "R": # Press (-) button.
                return order.reduce_item(item)
            return "Invalid type. Please choose A(Add) or R(Reduce)."
        return "Invalid item."
    
    # Use a coupon to discount total of order.
    def apply_coupon(self, member_id, date, info):
        info = info.dict()
        member = self.search_member_from_id(member_id)
        date = self.format_str_to_date(date)
        if date == None : 
            return "Invalid date format. Please use ISO format (YYYY-MM-DD)."
        if member.order == None :
            return "Please select some services."
        if member.order.visit_date != date : 
            return "Invalid order date."
        
        coupon = self.search_promotion_from_code(info["code"].upper())
        order = member.order
        if coupon == None: 
            return "Incorrect coupon code."
        if coupon.is_expired() == True: 
            return "This code has expired."
        if isinstance(coupon, AmountCoupon) :
            if coupon.min_purchase > order.cal_purchase_amount(): 
                return "The purchase amount is not enough."
        order.promotion = coupon
        return "Coupon successfully used!" 
    
    # Show member info and order detail.
    def show_confirm(self, member_id: int):
        member = self.search_member_from_id(member_id)
        if member.order == None: 
            return "Not found order"
        if member.order.total == 0:
            return "please select some service"
        if member.booking_temp != None:
            if member.order == member.booking_temp.order:
                member.booking_temp.booking_date = date.today()
                return {
                    "member" : member.to_dict(),
                    "booking": member.booking_temp.to_dict()
                }
        member.booking_temp = Booking(member_id, member.order, date.today())
        return {
                "member" : member.to_dict(),
                "booking": member.booking_temp.to_dict()
            }
        
    # Show booking id and info that must be filled in for payment.
    def show_payment(self, member_id: int, payment_method: str):
        member = self.search_member_from_id(member_id)
        booking = member.booking_temp
        if booking == None:
            return "Booking not found."
        if booking.order.total == 0:
            return "please select some service"
        return {
            "booking_id": booking.id,
            "amount": booking.order.total,
            "payment_method": payment_method
        }
    
    # Check if items in order are still available and comfirm payment.
    def is_available(self, order, dailystock): # check still available
        for detail in order.order_detail:
            if dailystock.is_available(detail.item, detail.amount) == False:
                return False
        return True
    
    def paid(self, member_id: int, info, payment_method): # confirm payment
        member = self.search_member_from_id(member_id)
        if member == None : return "Member not found."
        booking = member.booking_temp
        order = booking.order
        date = order.visit_date
        dailystock = self.search_daily_stock_from_date(date)
        if booking == None:
            return "Booking not found."
        if booking.order.total == 0:
            return "please select some service"
        
        # for detail in order.order_detail:
        #     if dailystock.is_available(detail.item, detail.amount) == False:
        #         member.booking_temp = None
        #         member.order = None
        #         return "Your order is no longer available."
    
        if self.is_available(order, dailystock) == True:
            self.update_dailystock(order, dailystock)
            payment_method = deepcopy(self.__payment_list[payment_method]) # Bankpayment
            transaction = PaymentTransaction(booking.id, booking.order.total)
            payment_method.pay(transaction, info)
            self.add_transaction(transaction)
            booking.update_status()
            member.add_booking(booking)
            booking_info = self.booking_to_pdf(member, booking)
            member.booking_temp, member.order = None, None
            self.__finish_booking_manager.create_pdf(booking_info)
            return f"Pay success {member.id}, {booking.id}"
        else:
            member.booking_temp = None
            member.order = None
            return "Your order is no longer available."
    
    # Update stock and show booking after successful payment.
    def update_dailystock(self, order, dailystock): # update stock
        for detail in order.order_detail:
            dailystock.update_item(detail.item, detail.amount)
        
    def show_success_payment(self):
        pass
    
    def show_finish_booking(self, member_id, booking_id): # show complete booking
        member = self.search_member_from_id(member_id)
        if member == None:
            return "Not found this member."
        if self.search_booking_from_member(member, booking_id) == None:
            return "Not found this booking."
        return self.__finish_booking_manager.view_finish_booking(booking_id)
    
    def booking_to_pdf(self, member, bookin):
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
                "Date Of Order": booking.booking_date.strftime("%d %B %Y"),
                "Payment Status": "PAID"
            },
            "Order": {
                "Date Of Visit": order.visit_date.strftime("%d %B %Y"),
                "Total" : order.total,
                "Discount": order.cal_discount(),
                "Order Detail": order.to_pdf()
            }
    }
    

def create_promotion():
    return [ AmountCoupon(date(2024, 3, 1) ,date(2024, 3, 31) , "35IWK0M5" , 200, 1000),
        AmountCoupon(date(2024, 3, 3) ,date(2024, 4, 10) , "O1KSXG0X" , 300, 1000),
        AmountCoupon(date(2024, 3, 10) ,date(2024, 3, 31) , "QLC6EBTS" , 350, 2000),
        AmountCoupon(date(2024, 4, 4) ,date(2024, 3, 31) , "VBH7P77F" , 300, 2000),
        PercentCoupon(date(2024, 2, 2) ,date(2024, 3, 15) , "DU4LY3HV" , 0.1),
        PercentCoupon(date(2024, 3, 15) ,date(2024, 4, 15) , "IV3WLCHW" , 0.15),
        PercentCoupon(date(2024, 3, 10) ,date(2024, 3, 31) , "VROPTVOJ" , 0.2, 2500),
        PercentCoupon(date(2024, 3, 31) ,date(2024, 4, 30) , "UCJHSTWQ" , 0.3) 
    ]

def create_member():
    return [ 
        Member("James", "james123@gmail.com", "0812345678", date(2001,2,14), "12xncvbj34")
        ,Member("Yuji", "66010660@kmitl.ac.th", "0823456789", date(2002,1,3), "1xbv3z234")
        ,Member("Irene", "irene123@gmail.com", "0834567890", date(2003,4,2), "jdies234")
        ,Member("Charlotte", "charlotte@gmail.com", "0845678901", date(2004,1,4), "w.sa12sm.34")
        ,Member("Sharon", "66010853@kmitl.ac.th", "0856789012", date(1998,12,13), "1ksl23aqo4")
        ,Member("Rose", "rose1234@gmail.com", "0867890123", date(1999,6,1), "sznkal34")
        ,Member("Lucian", "lucian123@gmail.com", "0878901234", date(2000,1,1), "2.lasm_p4")
        ,Member("Zeno", "zeno1234@gmail.com", "0889012345", date(2005,9,26), "1splalr0es3")
        ,Member("Apollo", "apollo12@gmail.com", "0890123456", date(2006,3,8), "wqygwoaqr234")
        ,Member("Lucian", "lucian123@gmail.com", "0801234567", date(1997,10,9), "teosrl_234")
        ,Member("Dion", "dion1234@gmail.com", "0898765432", date(1996,11,22), "sjgflxlsj_t") 
    ]

def create_daily_stock():
    lst = []
    today = date.today()
    for i in range(60):
        lst.append(DailyStock(today + timedelta(days = i)))
    return lst