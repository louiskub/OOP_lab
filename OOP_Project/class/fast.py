from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import starlette.status as status

from waterpark import WaterPark
from stock import DailyStock
from customer import Customer, Member
from booking import Booking, Order

from service import Locker

from datetime import datetime, date
import requests as req
import json

waterpark = WaterPark("Rama")
order = Order(date(2024, 2, 15),None)
Locker1 = Locker('L')
order.add_select([[Locker1, 100]])
waterpark.add_booking(Booking(None, 2, order, date(1996, 12, 11)))
# customer, booking_id, order, order_datetime

app = FastAPI()

import json

@app.get('/')
def root():
    return "Hello"

@app.put('/payment', tags=['payment'])
async def show_payment():
    data = waterpark.selected_payment(2, 1)
    if data == "Now is not available anymore":
        return "Now is not available anymore" #RedirectResponse(url="/")
    return data