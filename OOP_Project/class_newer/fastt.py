from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from service import Cabana, Towel, Ticket, Locker 
from order import Order, OrderDetail
from customer import Member
from stock import Stock, DailyStock
from datetime import datetime, timedelta

from datetime import date
import time, json
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
    is_delete: int | None = None # 1

waterpark = WaterPark()
member = create_member()
promotion = create_promotion()
waterpark.add_member(member)
waterpark.add_promotion(promotion)
mem = member[1]
order = create_order()
#print(waterpark.get_member_list())
#mem.add_booking(booking)
print(mem.id)
mem.order = order


















# ---- apply coupon
@app.put('/{member_id}/services', tags=['services'])
def add_coupon(member_id: int, info: CouponInput):
    info = info.dict()
    member = waterpark.search_member_from_id(member_id)
    if info["is_delete"] == 1 : 
        member.order.promotion = None
        return "delete coupon in order"
    coupon = waterpark.search_promotion_from_code(info["code"])
    order = member.order
    # if coupon == None: return "coupon not found"
    # if coupon.is_expired() == True : return "coupon Expired"
    # if coupon.min_purchase > order.total : return "cannot use this"
    order.promotion = coupon
    return order.to_dict()


# ---- show confirm 
@app.get('/{member_id}/show_confirm', tags=['show_confirm'])
def show_confirm(member_id: int):
    return waterpark.show_confirm(member_id)

@app.get('/{member_id}/show_payment/bank', tags=['show_payment'])
def show_bank_payment(member_id: int):
    return waterpark.show_payment(member_id, "bank")
    #waterpark.show_payment(int(member_id), "bank")
@app.get('/{member_id}/show_payment/card', tags=['show_payment'])
def show_card_payment(member_id: int):
    return waterpark.show_payment(member_id, "card")

#กดจ่ายตัง
@app.put('/{member_id}/show_payment/bank', tags=['show_payment'])
def bank_paid(member_id: int, info: BankInput):
    return waterpark.paid(member_id, info, 0)
    
@app.put('/{member_id}/show_payment/card', tags=['show_payment'])
def card_paid(member_id: int, info: CardInput):
    return waterpark.paid(member_id, info, 1)

# show pdf via file
@app.get('/{member_id}/finish_booking/{booking_id}', tags=['finish_booking'])
def show_finish_booking(member_id: int, booking_id: int):
    return waterpark.show_finish_booking(int(member_id), int(booking_id))


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

