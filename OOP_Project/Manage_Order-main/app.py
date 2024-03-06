from fastapi import FastAPI, HTTPException
from products import Cabana, Locker, Ticket
from stock import Stock, DailyStock 
from member import Member
from datetime import date
from waterpark import WaterPark
import uvicorn

system = WaterPark('Dkub')
stock = Stock()

app = FastAPI()
# A minimal app to demonstrate the get request
@app.get("/", tags = ['Home'])
async def show_homepage() -> dict:
    return {"Welcome to": "our waterpark"}

# GET -- > Get all services. When press services button.
@app.get("/services", tags = ['Services'])
async def show_all_services():
    return {"Services": system.get_all_services()}

# GET -- > Get services in date. After selected date.
@app.get("/services/{day}", tags = ['Services'])
async def show_services_in_date(day: str):
    try:
        selected_date = date.fromisoformat(day)
    except ValueError:
        raise HTTPException(status_code = 400, detail = "Invalid date format. Please use ISO format (YYYY-MM-DD).")
    return {"Services in {selected_date}": system.get_services_in_date(selected_date)}

@app.get("/member", tags = ['Member'])
async def show_member():
    return {"Member" : [member.name for member in system.get_member_list()]}

@app.post("/subscription")
async def add_member(name: str, email:str, phone_no:str, birthday:str, password:str) :
    return {"Result": system.become_member(name, email, phone_no, birthday, password)}

if __name__ == "__main__":
    uvicorn.run("app:app", host = "127.0.0.1", port = 8000, log_level = "info", reload = True)