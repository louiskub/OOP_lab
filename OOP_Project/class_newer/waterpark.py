from booking import Booking
from stock import DailyStock, Stock
from service import Ticket, Cabana, Locker
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
    def get_zone(self):
        return self.__zone_list
    
    def get_stock(self):
        return self.__stock
    
    def get_zone_list(self):
        return self.__zone_list

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
            self.__promotion_list.append(promotion) 
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
            print(transaction.id)
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

    # Log in
    def login_member(self, email, password):
        for member in self.__member_list:
            if member.verify_member(email, password) != None:
                # member_id = member.verify_member(email, password).id
                return "Login successful" # return member id
        return "Email or password is incorrect."  
    
    # Subscription
    def become_member(self, name, email, phone_number, birthday, password):
        for member in self.__member_list:
            if email == member.email or phone_number == member.phone_no:
                return "You are already a member." 
        error = {}
        if Member.check_email(email) == False:
            error["email"] = "Fill the correct email."
        if Member.check_phone_number(phone_number) == False and len(phone_number) != 10:
            error["phone"] = "Fill the correct phone number."
        if Member.check_password(password) == False and len(password) < 8:
            error["password"] = "Please use a password with at least 8 characters and only the letters 0-9, a-z, A-Z, (.) or (_)."
        if len(error) > 0:
            return error
        self.add_member(Member(name, email, phone_number, birthday, password))
        return "Membership registration completed."

    # Get services information.
    # def get_cabana_in_zone(self, date):
    #     daily_stock = self.search_daily_stock_from_date(date)
    #     cabana_in_zone = {}
    #     for zone in self.__zone_list:
    #         cabana_in_zone[zone] = daily_stock.get_cabana_in_zone(zone)
    #     return cabana_in_zone 
    
    def get_services_in_stock(self, stock):
        services = {}
        services["ticket"] = [ticket.to_dict() for ticket in stock.ticket_list]
        services["cabana"] = {}
        for zone in self.__zone_list:
            services["cabana"][zone] = [cabana.to_dict() for cabana in stock.get_cabana_in_zone(zone)]
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
        if daily_stock == None:
            return "Please select the available date."
        item = self.find_item(daily_stock, items)
        if item != None:
            #if type == "A" and daily_stock.is_available(item, 1): # Press (+) button.
            if type == "R": # Press (-) button.
                return order.reduce_item(item)
            elif daily_stock.is_available(item, order.order_amount(item) + 1 ) == False:
                return "Order limit"
            elif type == "A": # Press (+) button.
                return order.add_item(item)
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
            return "Please Select Some Service"
        if member.order.visit_date != date : 
            return "Invalid order date"
        
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
    return [
        AmountCoupon(date.today()-timedelta(days=1) ,date.today()+timedelta(days=3) , "35IWK0M5" , 200, 1000),
        AmountCoupon(date.today()-timedelta(days=5) ,date.today()+timedelta(days=4) , "O1KSXG0X" , 300, 1000),
        AmountCoupon(date.today()-timedelta(days=10) ,date.today()+timedelta(days=5) , "QLC6EBTS" , 350, 2000),
        AmountCoupon(date.today()+timedelta(days=20) ,date.today()-timedelta(days=7) , "VBH7P77F" , 300, 2000),
        PercentCoupon(date.today()-timedelta(days=1) ,date.today()+timedelta(days=3) , "DU4LY3HV" , 0.1),
        PercentCoupon(date.today()-timedelta(days=5) ,date.today()+timedelta(days=4) , "IV3WLCHW" , 0.15),
        PercentCoupon(date.today()-timedelta(days=10) ,date.today()+timedelta(days=5) , "VROPTVOJ" , 0.2, 2500),
        PercentCoupon(date.today()+timedelta(days=20) ,date.today()-timedelta(days=7) , "UCJHSTWQ" , 0.3)
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
    wave_pool_zone.append(Cabana("W01", "S", "Wave Pool")) # Wave Pool Zone
    wave_pool_zone.append(Cabana("W02", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("W03", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W04", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W05", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W06", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W07", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W08", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W09", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W10", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("W11", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("W12", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("W13", "L", "Wave Pool"))
    wave_pool_zone.append(Cabana("W14", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("W15", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W16", "M", "Wave Pool"))
    wave_pool_zone.append(Cabana("W14", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("W14", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("W14", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("P05", "S", "Wave Pool"))
    wave_pool_zone.append(Cabana("P06", "S", "Wave Pool"))

    activity_relax_zone = []
    activity_relax_zone.append(Cabana("P01", "S", "Activity and Relax")) # Activity and Relax Zone
    activity_relax_zone.append(Cabana("P02", "S", "Activity and Relax"))
    activity_relax_zone.append(Cabana("P03", "M", "Activity and Relax"))
    activity_relax_zone.append(Cabana("P04", "M", "Activity and Relax"))

    hill_zone = []
    hill_zone.append(Cabana("H01", "S", "Activity and Relax")) # Hill Zone
    hill_zone.append(Cabana("H02", "S", "Activity and Relax"))
    hill_zone.append(Cabana("H03", "S", "Activity and Relax"))
    hill_zone.append(Cabana("H04", "M", "Activity and Relax"))
    hill_zone.append(Cabana("H05", "M", "Activity and Relax"))

    family_zone = []
    family_zone.append(Cabana("F01", "M", "Family")) # Family Zone
    family_zone.append(Cabana("F02", "S", "Family"))
    family_zone.append(Cabana("F03", "L", "Family"))
    family_zone.append(Cabana("F04", "S", "Family"))
    family_zone.append(Cabana("F05", "M", "Family"))
    family_zone.append(Cabana("F06", "M", "Family"))
    family_zone.append(Cabana("K05", "M", "Family"))
    family_zone.append(Cabana("K06", "M", "Family"))
    family_zone.append(Cabana("K07", "S", "Family"))
    
    cabana_list = []
    cabana_list.extend([wave_pool_zone, activity_relax_zone, hill_zone, family_zone])
    return cabana_list

def create_locker():
    locker_list = [Locker("M", 149, 80), Locker("L", 229, 20)]
    return locker_list
    
def create_ticket():
    ticket_list = []
    
    # Solo Ticket
    ticket_list.append(Ticket("Full Day", 1, 699))
    ticket_list.append(Ticket("Senior", 1, 599)) # >= 60 y.o. and want to play slides
    ticket_list.append(Ticket("Child", 1, 0))
    ticket_list.append(Ticket("SPD", 1, 0)) # including pregnant and disabled 

    # Group Ticket
    ticket_list.append(Ticket("Group for 4", 4, 2599))
    ticket_list.append(Ticket("Group for 6", 6, 3779))
    ticket_list.append(Ticket("Group for 8", 8, 4879))
    ticket_list.append(Ticket("Group for 10", 10, 5999))
    
    return ticket_list

def create_daily_stock():
    today = date.today()
    lst = []
    for i in range(60):
        lst.append(DailyStock(today + timedelta(days=i)))
    return lst

def create_order():
    t = Ticket("Full Day", 1, 699)
    c = Cabana("W01", "S", "Wave Pool")
    order = Order(date.today()+ timedelta(days=3))
    order.add_item(t)
    order.add_item(t)
    order.add_item(c)
    order.add_item(c)
    return order

# def constructor():
#     dkub = WaterPark()
#     today = date.today()
#     for i in range(60) :
#         dkub.add_daily_stock(DailyStock(today + timedelta(days=i)))
#     my_order = dkub.create_order(date.today())
#     daily_stock = dkub.search_daily_stock_from_date(my_order.visit_date)
#     towel = daily_stock.towel   
#     for locker in daily_stock.locker_list: # choose locker
#         locker_L = locker
#     for ticket in daily_stock.ticket_list: # choose ticket
#         my_ticket = ticket
        
#     dkub.add_item(towel, my_order)
#     dkub.add_item(towel, my_order)
#     dkub.add_item(towel, my_order)
#     dkub.add_item(locker_L, my_order)
#     dkub.add_item(my_ticket, my_order)
#     dkub.remove_item(towel, my_order)


#     # customer_list = create_customer()
#     # [dkub.add_customer(customer) for customer in customer_list]
#     # return (dkub, customer_list)

# # constructor()

# # if "__main__" == __name__ :
    
# #     # create_booking()