from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from service import Cabana, Towel, OrderDetail, Ticket, Locker 
from customer import Customer, Member
from stock import Stock, DailyStock
from datetime import datetime, timedelta

from datetime import date
import time, json
from waterpark import WaterPark, constructor
app = FastAPI()


# a = Towel()
# b = OrderDetail(a)
# print(b.total)
# b.add_item()
# print(b.amount)
# print(b.total)

# waterpark, customer_list = constructor()
waterpark = WaterPark()


@app.get('/show_confirm/{booking_id}', tags=['show_confirm'])
def show_confirm():
    return waterpark.show_condfirm()

@app.put('/show_confirm/{booking_id}', tags=['show_confirm'])
def going_to_payment(booking_id: str, payment_method: int):     #0=bank, 1=card  
    return waterpark.selected_payment(booking_id, int(payment_method))

@app.get('/show_payment/{transaction_id}', tags=['show_payment'])
def show_payment(transaction_id):
    return waterpark.show_payment(transaction_id)

@app.delete('/show_payment/{transaction_id}', tags=['show_payment']) #delte tranasaction
def delete_payment(transaction_id):
    return waterpark.cancel_payment(transaction_id)

#กดจ่ายตัง
@app.put('/show_payment/{transaction_id}', tags=['show_payment'])
def paid(transaction_id, info: dict):
    return waterpark.paid_bill(transaction_id, info)

@app.get('/finish_booking/{transaction_id}', tags=['finish_booking'])
def show_finish_booking(transaction_id):
    return waterpark.show_finish_booking(transaction_id)


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

