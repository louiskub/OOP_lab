from fastapi import FastAPI
from bookingmanager import FinishBookingManager
from fastapi.responses import RedirectResponse
from waterpark import WaterPark
from payment import PaymentTransaction
f = FinishBookingManager()

app = FastAPI()
#PaymentTransaction()

@app.get('/')
def d():
    return "hello"
@app.get('/view')
def view():
    booking_id = "12345"
    return f.show_booking(str(booking_id))


@app.get('/vieww/{booking_id}')
def viewwwww(booking_id: str):
    return f.show_booking(str(booking_id))

# @app.get('/select_payment/{booking_id}')
# def select():

waterpark = WaterPark()

@app.get('/payment/{transaction_id}')
def payment(transaction_id):
    return waterpark.show_payment(transaction_id)

