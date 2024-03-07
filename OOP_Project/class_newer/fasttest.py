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
    return RedirectResponse(url='/')
