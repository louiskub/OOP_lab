from datetime import datetime, date, time, timedelta
import re
from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
from typing import List

app = FastAPI()

class WaterPark:
    def __init__(self, name):
        self.__name = name
        self.__stock = Stock()
        self.__daily_stock_list = create_daily_stock()
        self.__zone_list = ['Wave Pool', 'Activity and Relax', 'Hill', 'Family']
        self.__member_list = []
        self.__promotion_list = []
        self.__payment_list = []
        self.__transaction_list = []
    
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
    
    def iscorrect_info(self,email, phone_no):

        email_pattern = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
        is_valid_email = re.match(email_pattern, email) is not None

        phone_pattern = r'^[0-9]{10}$'
        is_valid_phone = re.match(phone_pattern, phone_no) is not None

        return is_valid_email, is_valid_phone
    


class Booking :
    __booking_id = 1
    def __init__(self, member, order):
        self.__member = member
        self.__booking_id = Booking.__booking_id
        self.__order = order
        self.__status = False #ispaid ?
        Booking.__booking_id +=1
        
    @property
    def booking_id(self):
        return self.__booking_id
    @property
    def order(self):
        return self.__order
    @property
    def member(self):
        return self.__member
    @property
    def date_time(self):
        return self.__order_datetime
    
    
    def update_status(self):
        self.__status = True
        return "Done" 
    
    def get_booking_detail(self):
        order = self.__order
        customer = self.__customer
        date = self.__order_datetime
        return {"detail": order, "customer": [customer.name, customer.email],"date": date}


class Stock:
    def __init__(self):
        self.__cabana_list = create_cabana()
        self.__locker_list = create_locker()
        self.__ticket_list = create_ticket()
        self.__towel = Towel()
    
    @property
    def cabana_list(self):
        return self.__cabana_list
    
    @property
    def locker_list(self):
        return self.__locker_list
    
    @property
    def ticket_list(self):
        return self.__ticket_list
    
    @property
    def towel(self):
        return self.__towel
    
    @property
    def towel_price(self):
        return self.__towel
    
    def add_cabana(self, cabana):
        if isinstance(cabana, Cabana):
            self.__cabana_list.append(cabana)
        else: return 'Error'
            
    def add_locker(self, locker):
        if isinstance(locker, Locker):
            self.__locker_list.append(locker)
        else: return 'Error'
            
    def add_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.__ticket_list.append(ticket)
        else: return 'Error'
    
    def show_all(self):
        pass 
    
    def get_cabana_in_zone(self, cabana_zone):
        for zone in range (len(self.__cabana_list)):
            for cabana in range (len(self.__cabana_list[zone])):
                if cabana_zone == self.__cabana_list[zone][cabana].zone:
                    return self.__cabana_list[zone]
                cabana_zone += 1        
        return None
    
class DailyStock(Stock):
    def __init__(self, date):
        super().__init__()
        self.__date = date
        self.__booking_list = []
    
    @property
    def date(self):
        return self.__date
    
    def is_available(self, item, amount):
        if isinstance(item, Cabana):
            return not item.is_reseve # If reserved = Not available
        elif not isinstance(item, Ticket):
            return item.remaining_amount >= amount
        return True

def create_daily_stock():
    daily_list = []
    daily_list.append(DailyStock(date(2024, 2, 1)))
    daily_list.append(DailyStock(date(2024, 2, 2)))
    daily_list.append(DailyStock(date(2024, 2, 3)))
    daily_list.append(DailyStock(date(2024, 2, 4)))
    daily_list.append(DailyStock(date(2024, 2, 5)))
    daily_list.append(DailyStock(date(2024, 2, 6)))
    daily_list.append(DailyStock(date(2024, 2, 7)))
    daily_list.append(DailyStock(date(2024, 2, 8)))
    daily_list.append(DailyStock(date(2024, 2, 9)))
    daily_list.append(DailyStock(date(2024, 2, 10)))
    
    return daily_list


        
class Cabana:
    def __init__(self, id, size, zone):
        self.__id = id
        self.__size = size
        self.__zone = zone
        cabana_price = {'S':899, 'M':1499, 'L':2499}
        for size, price in cabana_price.items():
            if self.__size == size:
                self.__price = price
        self.__is_reserve = False
    
    def __str__(self):
        return f"Cabana({self.__size}): {self.__zone} Zone"
    
    @property
    def id(self):
        return self.__id
    
    @property
    def size(self):
        return self.__size
    
    @property
    def zone(self):
        return self.__zone
    
    @property
    def is_reserve(self):
        return self.__is_reserve
        
    @property    
    def price(self):
        return self.__price
    
    def update_is_reserve(self, type): # A = Add, R = Remove
        if type == 'A':
            self.__is_reserve = True
        elif type == 'R':
            self.__is_reserve = False
    
class Locker:
    def __init__(self, size, price, remaining_amount):
        self.__size = size
        self.__price = price
        self.__remaining_amount = remaining_amount
    
    def __str__(self):
        return f"Locker: Size {self.__size}"
    
    @property
    def size(self):
        return self.__size
        
    @property
    def price(self):
        return self.__price
    
    @property
    def remaining_amount(self):
        return self.__remaining_amount
    
    def update_remaining_amount(self, type, amount): # A = Add, R = Remove
        if type == 'A':
            self.remaining_amount += amount
        elif type == 'R':
            self.remaining_amount -= amount
                
class Ticket:
    def __init__(self, type, amount_per_ticket, price = 0):
        self.__type = type
        self.__amount_per_ticket = amount_per_ticket
        self.__price = price
        self.__is_thai = True
    
    def __str__(self):
        return f"Ticket: {self.__type}"
    
    @property
    def type(self):
        return self.__type
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def is_thai(self):
        return self.__is_thai
    
    @property
    def price(self):
        if not(self.__is_thai) and self.__price != 0:
            if self.__amount_per_ticket == 1:
                return self.__price + 200                       
            else :
                return self.__price + 150 * self.__amount_per_ticket
        else:
            return self.__price
        
    def update_is_thai(self, type): # F = Foreign, T = Thai
        if type == 'T':
            self.__is_thai = True
        elif type == 'F':
            self.__is_thai = False
            
class Towel:
    def __init__(self):
        self.__price = 99
        self.__remaining_amount = 5000
    
    def __str__(self):
        return f"Towel: "
        
    @property
    def price(self):
        return self.__price
    
    @property
    def remaining_amount(self):
        return self.__remaining_amount
    
    def update_remaining_amount(self, type, amount): # A = Add, R = Remove
        if type == 'A':
            self.remaining_amount += amount
        elif type == 'R':
            self.remaining_amount -= amount
        

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
        self.__account_no = None

    def gen_payment():
        pass
    def update_status(self, transaction_id, account_no):
        self.__status = True
        self.__transcation_id = transaction_id
        self.__account_no = account_no

class Card(Payment):
    def __init__(self, booking: Booking, datetime):
        Payment.__init__(self, booking, datetime)
        self.__card_no = None
        self.__card_pin = None

    def gen_payment():
        pass


class Order:
    def __init__(self, visit_date):
        self.__visit_date = visit_date
        self.__order_detail = []
        self.__total = 0
        self.__coupon = None
    
    def __str__(self):
        return f"{[order for order in self.__order_detail]}\nTOTAL: {self.total}"
    
    @property
    def visit_date(self):
        return self.__visit_date
    
    @property
    def total(self):
        self.__total = 0 
        for items in self.__order_detail:
            self.__total += items.total_price
        if self.__coupon:
            self.__total -= self.__coupon.discount  # ลดราคาตามค่าส่วนลดจากคูปอง
        return self.__total
    
    @property
    def order_detail(self):
        return self.__order_detail
        
    def add_item(self, item) : # Press the add button
        if isinstance(item, Cabana):
            for items in self.__order_detail:
                if isinstance(items.item, Cabana):
                    return self
        elif isinstance(item, (Locker, Towel, Ticket)):
            for items in self.__order_detail:
                if items.item == item:
                    items + 1
                    return self
        self.__order_detail.append(OrderDetail(item))         
        return self
    
    def remove_item(self, item) : # Press the reduce button
        for items in self.__order_detail:
            if item == items.item:
                items - 1
                if items.amount == 0:
                    self.__order_detail.remove(items)
                return self
        return self
    
    def apply_coupon(self, coupon): 
        if coupon.is_expired():
            return False, "Coupon has expired"
        
        if self.__total >= coupon.min_purchase:
            self.__coupon = coupon
            self.__total -= coupon.discount  # ลดราคาตามค่าส่วนลดจากคูปอง
            return True, "Coupon applied successfully"
        else:
            return False, "Minimum purchase amount not met for this coupon"

    # def check_still_available(self) -> bool:
    #     for order_detail in self.__order_detail_list:
    #         item = order_detail.item
    #         if isinstance(item, Cabana):
    #             return not item.is_reseve # If reserved = Not available
    #         elif not isinstance(item, Ticket):
    #             return item.remaining_amount >= order_detail.amount
    #     return True
    
    def reserve(self):
        for order_detail in self.__order_detail_list:
            item = order_detail.item
            if isinstance(item, Cabana):
                item.is_reseve = True
            elif not isinstance(self.__item, Ticket):
                item.remaining_amount -= order_detail.amount
        return "Done"
    
    
class OrderDetail:
    def __init__(self, item, amount = 1):
        self.__item = item  # ใส่เป็น instance 
        self.__amount = amount
        self.__total_price = 0
    
    def __str__(self):
        return f"{self.item} x {self.__amount} = {self.total_price} THB"
    
    def __add__(self, amount):
        if 0 < amount:
            self.__amount += 1
        
    def __sub__(self, amount):
        if 0 < amount <= self.__amount:
            self.__amount -= amount 
        
    @property
    def item(self):
        return self.__item
    
    @property 
    def amount(self):
        return self.__amount
    
    @property
    def total_price(self):
        return self.__item.price * self.__amount
    
    def check_still_available(self) -> bool:
        for order_detail in self.__order_detail_list:
            item = order_detail.item
            if isinstance(item, Cabana):
                return not item.is_reseve #ถ้าจองแล้ว = ไม่ว่าง
            elif not isinstance(item, Ticket):
                return item.remaining_amount >= order_detail.amount
        return True



class Ticket:
    def __init__(self, type, amount_per_ticket, price = 0):
        self.__type = type
        self.__amount_per_ticket = amount_per_ticket
        self.__price = price
        self.__is_thai = True
    
    def __str__(self):
        return f"Ticket: {self.__type}"
    
    @property
    def type(self):
        return self.__type
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def is_thai(self):
        return self.__is_thai
    
    @property
    def price(self):
        if not(self.__is_thai) and self.__price != 0:
            if self.__amount_per_ticket == 1:
                return self.__price + 200                       
            else :
                return self.__price + 150 * self.__amount_per_ticket
        else:
            return self.__price
        
    def update_is_thai(self, type): # F = Foreign, T = Thai
        if type == 'T':
            self.__is_thai = True
        elif type == 'F':
            self.__is_thai = False

    
class Coupon:
    def __init__(self, code, discount, min_purchase, start_date: date, end_date : date):
        self.__code = code
        self.__discount = discount
        self.__end_date = end_date
        self.__min_purchase = min_purchase  # ยอดซื้อขั้นต่ำ
    
    def is_expired(self):
        today = datetime.now().date()
        return today > self.__end_date

    @property
    def code(self):
        return self.__code
    
    @property
    def discount(self):
        return self.__discount
    
    @property
    def min_purchase(self):
        return self.__min_purchase
    
    def get_discount_amount(self):
        return self.__discount
        
class Member():
    def __init__(self, name, email, phone_number, birthday):
        self.__email = email
        self.__name = name
        self.__phone_number = phone_number
        self.__birthday = birthday
        self.__password = None
        self.__booking_list = []
        
    @property
    def password(self):
        return self.__password
    
    @property
    def email(self):
        return self.__email  
    
    @property
    def name(self):
        return self.__name   
    
    @property
    def phone_number(self):
        return self.__phone_number  
        
    def __add__(self, amounts):
        if amounts > 0:
            self.__point += amounts
            return 'Success'
        else: 
            return 'Invalid Amounts'
    
    def add_booking(self,booking):
        self.__booking_list.append(booking)
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone_number
    
    
    def get_booking_list(self):
        # สร้างรายการว่างเพื่อเก็บรายการการจองทั้งหมด
        booking_list = []
        # วนลูปผ่านรายการการจองทั้งหมดแล้วเพิ่มข้อมูลเกี่ยวกับการจองลงในรายการ
        for booking in self.__booking_list:
            booking_list.append({
                "booking_id": booking.booking_id,
                "order": booking.order,  # เข้าถึงข้อมูลลูกค้าและดึงชื่อ
                "name" : booking.member.get_name(),
                "email" : booking.member.get_email(),
                "phone" : booking.member.get_phone(),
            })
        return booking_list
        
    def __sub__(self, amounts):
        if self.__point >= amounts > 0:
            self.__point -= amounts
            return 'Success'
        else: 
            return 'Not enough points'
    
    def check_password(self, password):
        for char in password:
            if char.isnumeric() or char.isalpha() or char == '.':
                continue
            return False
        
    def add_password(self, password):
        if len(password) >= 8 and self.check_password(password) != False:
            self.__password = password
            return 'Success'
        elif len(password) < 8:
            return 'Please use a password with at least 8 characters.'
        elif self.check_password(password) == False:
            return 'Please use passwords that contain only the letters 0-9, a-z, A-Z, or (.)'
        else: 
            return 'Please use a password with at least 8 characters and only the letters 0-9, a-z, A-Z, or (.)' 
    
    def get_member_id(self):
        return self.__id
    

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
        
stock = Stock()

dkub = WaterPark("Dkub")

my_order = dkub.create_order(date(2024, 2, 2))

my_order2 = dkub.create_order(date(2024, 2, 2))

daily_stock = dkub.search_daily_stock_from_date(my_order.visit_date)

daily_stock = dkub.search_daily_stock_from_date(my_order2.visit_date)

towel = daily_stock.towel

for locker in daily_stock.locker_list:
    locker_L = locker
for ticket in daily_stock.ticket_list: 
    my_ticket = ticket

dkub.add_item(towel, my_order)
dkub.add_item(towel, my_order)
dkub.add_item(locker_L, my_order)
dkub.add_item(my_ticket, my_order)
dkub.remove_item(towel, my_order)

dkub.add_item(towel, my_order2)
dkub.add_item(towel, my_order2)

total = my_order.total

print(total)

coupon_test = Coupon("CODE123",100, 1000, date.today(), date.today() + timedelta(days=30))


if my_order.apply_coupon(coupon_test):
    print("Coupon applied successfully!")
    print("New total after discount:", my_order.total)
else:
    print("Coupon cannot be applied. Total amount does not meet minimum purchase requirement.")

james = Member('Jame', 'james123@asd.com', '0812345678',date(2004,4,18))

beam = Member('Beam', 'Beam@asd.com', '0921239393',date(2004,4,18))


Customer1 = dkub.add_member(beam)
Customer2 = dkub.add_member(james)

Booking_test = Booking(beam,my_order2)

Booking_test2 = Booking(james,my_order)

Booking2 = beam.add_booking(Booking_test)

Booking1 = james.add_booking(Booking_test2)

print(beam.get_booking_list())


class PhoneInput(BaseModel):
    phone_number: str

@app.get("/order_detail", tags=['order_detail'])
def bookinglist(phone_number: str = Query(...)):
    member_booking_lists = []
    for member in dkub.get_member_list():
        if member.phone_number == phone_number:
            member_booking_lists = member.get_booking_list()
            break

    if not member_booking_lists:
        return {"message": "No bookings found for the provided phone number"}

    return {"phone_number": phone_number, "booking_list": member_booking_lists}

@app.get("/price", tags = ['price'])
def price():
    return total

valid_coupons = {
    "CODE123": Coupon("CODE123", 100, 1000, date.today(), date.today() + timedelta(days=30))
}
class CouponInput(BaseModel):
    code: str
    
@app.post("/apply_coupon", tags=['coupon'])
def apply_coupon(coupon_input: CouponInput, booking_id: int = Query(...)):
    
    coupon_code = coupon_input.code

    # ตรวจสอบว่า booking_id นี้มีอยู่จริงในระบบหรือไม่
    booking_exists = False
    for member in dkub.get_member_list():
        for booking in member.get_booking_list():
            if booking["booking_id"] == booking_id:
                booking_exists = True
                break
        if booking_exists:
            break

    if not booking_exists:
        raise HTTPException(status_code=404, detail="Booking ID not found")

    if coupon_code not in valid_coupons:
        raise HTTPException(status_code=404, detail="COUPON NOT FOUND")
    
    
    coupon = valid_coupons[coupon_code]
    if my_order.total < coupon.min_purchase:
        raise HTTPException(status_code=400, detail="Minimum purchase amount not met for this coupon")

    
    if my_order.apply_coupon(coupon):
        return {"message": "Coupon applied successfully!", "new_total_after_discount": my_order.total}
    else:
        return {"message": "Coupon cannot be applied."}
#@app.get('/{member_id}/services/{date}/')
#@app.post("/{member_id}/show_confirm")
# @app.get('/{member_id}/show_payment/{transaction_id}/bank')
# @app.get('/{member_id}/finish_booking/{booking_id}')