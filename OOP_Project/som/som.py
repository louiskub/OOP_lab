from fastapi import FastAPI, HTTPException
from booking import Booking
# from products import Cabana, Locker, Ticket
# from stock import Stock, DailyStock 
from member import Member
from datetime import date
from waterpark import WaterPark
import uvicorn
from pydantic import BaseModel

"""becom_member"""
class add_mem(BaseModel):
    name: str
    email:str
    phone_no:str
    birthday:str
    password:str
    
"""log_in"""    
class log_in(BaseModel):
    email:str
    password:str
    
# Add and Reduce item
class item(BaseModel):
    name: str
    size: str | None = None
    type: str | None = None
    zone: str | None = None
    id: str | None = None
    
# ที่ทำbasemodelเพราะpathจะได้ไม่ยาว และ protect ข้อมูล user
    

system = WaterPark('Dkub')
mem=Member("Nong","123456@gmail.ac.th","0811111111",date(2004, 2, 2),"1111111111")
mem2=Member("Ki","355@gmail.ac.th","0811234111",date(2002, 1, 2),"125698851")
system.add_member(mem)
system.add_member(mem2)
order = system.create_order(date(2024, 2, 2))
book=Booking(mem.id,order,date(2024, 2, 2))
mem.add_booking(book)

app = FastAPI()
# A minimal app to demonstrate the get request
# @app.get("/member_list", tags = ['Member']) 
# async def show_member():
#     return {"Member" : [system.get_member_list()]} 

"""becom_member"""
@app.post("/subscription") #เพิ่ม Member ใหม่เข้าสู่ระบบ(สมัครmember)
async def add_member(mem:add_mem) :
    return {"Result": system.become_member(mem.name, mem.email, mem.phone_no, mem.birthday, mem.password)}

"""log_in"""   
@app.post("/login", tags = ['login']) #login เข้าสู่ระบบ โดยถ้าอีเมลกับรหัส๔ูกจะ responseกลับว่า 'Login successful'
async def login(log:log_in) :
    return {"Result" :system.login_member(log.email,log.password)}

"""view_booking"""
@app.get("/viewbooking", tags = ['booking'])#แสดงรายการจองของสมาชิกทั้งหมด
async def booking() :
    #print(system.get_member_list()[0].booking_list[0])
    return {"Member" : [member.booking_list for member in system.get_member_list()]}

# GET -- > Get all services. When press services button.
@app.get("/{member_id}/services", tags = ['Services'])
async def show_all_services():
    return {"Services": system.get_services_in_stock(system.get_stock())}

# GET -- > Get services after selected visit date.
@app.get("/{member_id}/services/{day}", tags = ['Services'])
def show_services_in_date(date: str):
    selected_date = system.format_str_to_date(date)
    daily_stock = system.search_daily_stock_from_date(selected_date)
    return {f"Services in {selected_date}": system.get_services_in_stock(daily_stock)}

# POST-- > Add item to order.
@app.post("/{member_id}/services/{day}", tags=['Services'])
async def add_order(member_id: int, date: str, item: item):
    return system.manage_order(member_id, date, item, 'A')

# DELETE-- > Remove item from order.
@app.delete("/{member_id}/services/{day}", tags=['Services'])
async def add_order(member_id: int, date: str, item: item):
    return system.manage_order(member_id, date, item, 'R')


if __name__ == "__main__":
    uvicorn.run("all_api:app", host = "127.0.0.1", port = 8000, log_level = "info", reload = True)
#รียกใช้ Uvicorn เพื่อรัน FastAPI ที่ host "127.0.0.1" และ port 8000 โดยใช้ไฟล์ all_api.py และกำหนดให้โหลดโมดูลใหม่อัตโนมัติเมื่อมีการแก้ไขโค้ด (reload)
