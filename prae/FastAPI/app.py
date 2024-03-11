from fastapi import FastAPI
from products import Cabana, Locker, Ticket
from stock import Stock, DailyStock 
from member import Member
from datetime import date
from waterpark import WaterPark
import uvicorn

dkub = WaterPark('Dkub')
stock = Stock()

app = FastAPI()
# A minimal app to demonstrate the get request
@app.get("/", tags = ['Home'])
async def root() -> dict:
    return {"Welcome to": "our waterpark"}

# GET -- > Get all services
@app.get("/services", tags = ['Services'])
async def show_all_services():
    return {"Services": dkub.get_all_services()}

@app.get("/member", tags = ['Member'])
async def show_member():
    return {"Member" : [m.name for m in dkub.get_member_list()]}

# # GET -- > Get available services in date
# @app.get("/services/{day}", tags = ['Services'])
# async def show_available_services(day: str):
#     return {"Available Services": dkub.get_available_services(date(day))}

@app.post("/subscription")
async def add_member(name: str, email:str, phone_no:str, birthday:str, password:str) :
    return {"Result": dkub.become_member(name, email, phone_no, birthday, password)}

# print(dkub.get_available_services(date(2024,2,1)))
# print(dkub.become_member('sirima', 'sirima@gmail.com', '0918242283', date(2005, 3, 26), 'srmxprxe123456'))
if __name__ == "__main__":
    uvicorn.run("app:app", host = "127.0.0.1", port = 8000, log_level = "info", reload = True)