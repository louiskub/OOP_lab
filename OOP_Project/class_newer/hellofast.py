# from fastapi import FastAPI, HTTPException, Depends, Form
# from fastapi.responses import RedirectResponse
# import starlette.status as status

# app = FastAPI()


# @app.get("/")
# async def main():
#     # Redirect to /docs (relative URL)
#     return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


# @app.get("/sling-academy")
# async def sling_academy():
#     # Redirect to an absolute URL
#     return RedirectResponse(
#         url="https://api.slingacademy.com", status_code=status.HTTP_302_FOUND
#     )

# @app.post('/l')
# def rot():
#     return "Hello"

# @app.get('/{booking_id}')
# def root(booking_id: str):
#     print(booking_id)
#     return RedirectResponse(url='/l', status_code=status.HTTP_302_FOUND)
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import asyncio

app = FastAPI()

# Dictionary to store countdown timers for each payment
payment_timers = {}


async def countdown_timer(payment_id: str, time_limit: int, redirect_url: str):
    await asyncio.sleep(time_limit)
    if payment_id in payment_timers:
        del payment_timers[payment_id]
        raise HTTPException(status_code=400, detail=f"Payment {payment_id} expired")


@app.get("/start_payment")
async def start_payment(payment_id: str, time_limit: int = 5):
    # Check if payment_id already has an active timer
    if payment_id in payment_timers:
        raise HTTPException(status_code=400, detail="Payment already in progress")

    # Start a new countdown timer for the payment
    payment_timers[payment_id] = asyncio.create_task(
        countdown_timer(payment_id, time_limit, "/homepage")
    )

    return {"message": "Payment timer started"}

@app.post("/complete_payment")
async def complete_payment(payment_id: str):
    # Check if payment_id has an active timer
    if payment_id not in payment_timers:
        return HTTPException(status_code=400, detail="No active payment timer found")

    # Stop the countdown timer for the payment
    payment_timers[payment_id].cancel()
    del payment_timers[payment_id]

    return {"message": f"Payment {payment_id} completed successfully"}


@app.exception_handler(400)
async def redirect_to_homepage(request, exc):
    # Redirect to the homepage for payments that weren't completed in time
    return RedirectResponse(url="/homepage", status_code=302)
