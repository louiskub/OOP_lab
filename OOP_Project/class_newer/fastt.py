from fastapi import FastAPI
from pydantic import BaseModel
# from fastapi.responses import RedirectResponse
# from service import Cabana, Towel, Ticket, Locker 
# from order import Order, OrderDetail
# from member import Member
# from stock import Stock, DailyStock
# from datetime import datetime, timedelta
# from datetime import date

from waterpark import *
app = FastAPI()

class CardInput(BaseModel):
    card_no: int
    card_pin: int

class BankInput(BaseModel):
    account_no: int
    bank_name: str
class CouponInput(BaseModel):
    code: str | None = None

class AddMember(BaseModel):
    name: str
    email:str
    phone_no:str
    birthday:str
    password:str
    
"""log_in"""    
class Login(BaseModel):
    email:str
    password:str
    
# Add and Reduce item
class Item(BaseModel):
    name: str
    size: str | None = None
    type: str | None = None
    zone: str | None = None
    id: str | None = None

system = WaterPark()
member = create_member()
promotion = create_promotion()
#system.add_member(member)
system.add_promotion(promotion)
mem = member[1]
order = create_order()
#print(waterpark.get_member_list())
#mem.add_booking(booking)
print(mem.id)
mem.order = order


"""becom_member"""
@app.post("/subscription", tags = ['Subscription']) #เพิ่ม Member ใหม่เข้าสู่ระบบ(สมัครmember)
async def add_member(member: AddMember) :
    return {"Result": system.become_member(member.name, member.email, member.phone_no, member.birthday, member.password)}

"""log_in"""   
@app.post("/login", tags = ['Login']) #login เข้าสู่ระบบ โดยถ้าอีเมลกับรหัส๔ูกจะ responseกลับว่า 'Login successful'
async def login(login: Login) :
    return {"Result": system.login_member(login.email, login.password)}

""""""
@app.get("/{member_id}/services", tags = ['Services'])
async def show_all_services():
    return {"Services": system.get_services_in_stock(system.get_stock())}

# GET -- > Get services after selected visit date.
@app.get("/{member_id}/services/{date}", tags = ['Services'])
def show_services_in_date( date: str):
    selected_date = system.format_str_to_date(date)
    daily_stock = system.search_daily_stock_from_date(selected_date)
    return {f"Services in {selected_date}": system.get_services_in_stock(daily_stock)}

# POST-- > Add item to order.
@app.post("/{member_id}/services/{date}", tags = ['Services'])
async def add_order(member_id: int, date: str, item: Item):
    return system.manage_order(member_id, date, item, 'A')

# DELETE-- > Remove item from order.
@app.delete("/{member_id}/services/{date}", tags = ['Services'])
async def add_order(member_id: int, date: str, item: Item):
    return system.manage_order(member_id, date, item, 'R')

# ---- apply coupon --> retotal
@app.put('/{member_id}/services/{date}', tags = ['Services'])
def apply_coupon(member_id: int, date: str, info: CouponInput):
    return system.apply_coupon(member_id, date, info)

# ---- show confirm 
@app.get('/{member_id}/show_confirm', tags = ['show_confirm'])
def show_confirm(member_id: int):
    return system.show_confirm(member_id)

@app.get('/{member_id}/show_payment/bank', tags = ['show_payment'])
def show_bank_payment(member_id: int):
    return system.show_payment(member_id, "bank")
    #waterpark.show_payment(int(member_id), "bank")

@app.get('/{member_id}/show_payment/card', tags = ['show_payment'])
def show_card_payment(member_id: int):
    return system.show_payment(member_id, "card")

#กดจ่ายตัง
@app.put('/{member_id}/show_payment/bank', tags = ['show_payment'])
def bank_paid(member_id: int, info: BankInput):
    return system.paid(member_id, info, 0)
    
@app.put('/{member_id}/show_payment/card', tags = ['show_payment'])
def card_paid(member_id: int, info: CardInput):
    return system.paid(member_id, info, 1)




#download pdf via file
@app.get('/{member_id}/finish_booking/{booking_id}', tags = ['finish_booking'])
def show_finish_booking(member_id: int, booking_id: int):
    from bookingmanager import FinishBookingManager
    f = FinishBookingManager()
    return f.view_finish_booking(booking_id)
    #return system.show_finish_booking(int(member_id), int(booking_id))


# # from fastapi.responses import RedirectResponse
# # import uvicorn

# # @app.get('/')
# # def rot():
# #     return "Hello"

# # @app.get('/{booking_id}')
# # def root(booking_id: str):
# #     print(booking_id)
# #     RedirectResponse('/', status_code=200)

# # @app.post('/{booking_id}')
# # def rooot(booking_id):
# #     return str(booking_id)

# # # if __name__ == '__main__':
# # #     uvicorn.

