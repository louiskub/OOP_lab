from fastapi import FastAPI
from bookingmanager import FinishBookingManager

f = FinishBookingManager()

app = FastAPI()


@app.get('/{booking_id}')
def showfinish(booking_id: str):
    return f.show_booking(booking_id)

