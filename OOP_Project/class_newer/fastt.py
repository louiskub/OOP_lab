from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import RedirectResponse
from service import Cabana, Towel, Ticket, Locker 
from order import OrderDetail
from customer import Customer, Member
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

waterpark = WaterPark()
member = create_member()
mem = member[0]
print(mem.id)
waterpark.add_member(member)
print(waterpark.get_member_list())
booking = create_booking(mem)
mem.add_booking(booking)
print(booking.id)


@app.get('/{member_id}/show_confirm/{booking_id}', tags=['show_confirm'])
def show_confirm(member_id: str, booking_id: str):
    return waterpark.show_condfirm(int(member_id), int(booking_id))

@app.post('/show_confirm/{booking_id}', tags=['show_confirm'])
def going_to_payment(booking_id: str, payment_method: int):     #0=bank, 1=card  
    return waterpark.selected_payment(int(booking_id), int(payment_method))
    
@app.get('/show_payment/{transaction_id}/bank', tags=['show_payment'])
def show_payment(transaction_id):
    return waterpark.show_payment(int(transaction_id))
@app.get('/show_payment/{transaction_id}/card', tags=['show_payment'])
def show_payment(transaction_id):
    return waterpark.show_payment(int(transaction_id))
# @app.post('/show_payment/{transaction_id}/card', tags=['show_payment'])
# def show_payment(transaction_id):
#     return waterpark.show_payment(int(transaction_id))

#กดออก
@app.delete('/show_payment/{transaction_id}/bank', tags=['show_payment']) #delte tranasaction
def delete_payment(transaction_id):
    return waterpark.cancel_payment(int(transaction_id))
@app.delete('/show_payment/{transaction_id}/card', tags=['show_payment']) #delte tranasaction
def delete_payment(transaction_id):
    return waterpark.cancel_payment(int(transaction_id))

#กดจ่ายตัง
@app.put('/show_payment/{transaction_id}/bank', tags=['show_payment'])
def paid(transaction_id, info: BankInput):
    return waterpark.paid_bill(int(transaction_id), info)
@app.put('/show_payment/{transaction_id}/card', tags=['show_payment'])
def paid(transaction_id, info: CardInput):
    return waterpark.paid_bill(int(transaction_id), info)


@app.get('/finish_booking/{transaction_id}', tags=['finish_booking'])
def show_finish_booking(transaction_id):
    return waterpark.show_finish_booking(int(transaction_id))


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

