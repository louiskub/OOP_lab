from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from waterpark import WaterPark

system = WaterPark()
app = FastAPI()
# uvicorn api:app --host 10.66.11.191 --port 3838
# uvicorn api:app
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


# print(system.member_list[0].id, end="  ")
# print(system.member_list[1].id, end="  ")
# print(system.member_list[2].id)
# member = create_member()
# promotion = create_promotion()
# #system.add_member(member)
# mem = member[1]
# order = create_order()
# #print(waterpark.get_member_list())
# #mem.add_booking(booking)
# print(mem.id)
# mem.order = order


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
def show_services_in_date(date: str):
    selected_date = system.format_str_to_date(date)
    daily_stock = system.search_daily_stock_from_date(selected_date)
    return {f"Services in {selected_date}": system.get_services_in_stock(daily_stock)}

# POST-- > Add item to order.
@app.post("/{member_id}/services/{date}", tags = ['Services'])
async def add_order(member_id: int, date: str, item: Item):
    #print(date)
    return system.manage_order(member_id, date, item, 'A')

# DELETE-- > Remove item from order.
@app.delete("/{member_id}/services/{date}", tags = ['Services'])
async def reduce_order(member_id: int, date: str, item: Item):
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


@app.get('/{member_id}/payment_success/{booking_id}', tags = ['finish_booking'])
def payment_success(member_id: int, booking_id: int):
    return {
        "Hello": "World"
    }

#download pdf via file ---> click button to download pdf
@app.get('/{member_id}/finish_booking/{booking_id}', tags = ['finish_booking'])
def show_finish_booking(member_id: int, booking_id: int):
    from bookingmanager import FinishBookingManager
    f = FinishBookingManager()
    return f.view_finish_booking(booking_id)
    #return system.show_finish_booking(int(member_id), int(booking_id))

# view member info
@app.get('/{member_id}/show_member_info', tags=["View Info"])
def show_member_info(member_id: int):
    member = system.search_member_from_id(member_id)
    return member.to_dict()

# view all booking 
@app.get('/{member_id}/show_all_booking', tags=["View Info"])
def show_all_booking(member_id: int):
    member = system.search_member_from_id(member_id)
    booking_detail = []
    if member == None:
        return "Member Not found"
    for booking in member.booking_list:
        booking_detail.append({
            "booking_id": booking.id,
            "visit_date": booking.order.visit_date
        })
    if len(booking_detail) > 0 :
        booking_detail.sort(key = lambda item: item['visit_date'])
    #print(booking_detail)
    return booking_detail 
    
# @app.get('/root')
# def root():
#     return date(2002, 5, 15)

