from tkinter import *
#from api import Item
import ttkbootstrap as ttk
from ttkbootstrap import Style, PRIMARY
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk, ImageDraw, ImageFont
from datetime import datetime, date
from tkcalendar import Calendar 
import requests
import json

member_id = 100000
services_date = None
services_info = None

API_ENDPOINT_LOGIN = "http://127.0.0.1:8000/login"
API_ENDPOINT_SUBSCRIPTION = "http://127.0.0.1:8000/subscription"
API_ENDPOINT_SERVICES = f"http://127.0.0.1:8000/{member_id}/services"
# API_ENDPOINT_SERVICES_DATE = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
API_ENDPOINT_ADD_ITEM = f"http://127.0.0.1:8000//{member_id}/services/{services_date}"

# Create Tkinter window
root = ttk.Window(themename = 'flatly')
root.title("Scroll Frame")
root.geometry('1920x1080')

# Create a ScrolledFrame for pictures
services_frame = ScrolledFrame(root, autohide = True)
services_frame.pack(pady = 10, padx = 15, fill = BOTH, expand = YES)

def change_format_date(str_date):
    month, day, year = str_date.split("/")
    month = month if len(month)==2 else "0"+month
    day = day if len(day)==2 else "0"+day
    ymd = f"{year}-{month}-{day}"
    print(ymd)
    return ymd

def get_services_in_date():
    global member_id
    global services_date
    global services_info
    services_date = visit_date.entry.get()
    services_date = change_format_date(services_date)
    show_visit_date.config(text = f"Your visit date: {services_date}")
    
    API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
    response = requests.get(API_ENDPOINT_SERVICES_DATE)
    print(services_date)
    if response.status_code == 200:
        services_info = response.json().get(f"Services in {services_date}")
        #print(services_info)
        show_services_in_date()
    else:
        print(f"API request failed with status code: {response.status_code}")
        #print(response.json())
        services_info = None

def add_item(item):
    global member_id
    global services_date
    API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"

    response = requests.post(API_ENDPOINT_SERVICES_DATE, data=json.dumps(item))

def reduce_item(item):
    global member_id
    global services_date
    API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"

    response = requests.delete(API_ENDPOINT_SERVICES_DATE, data=json.dumps(item))
    print(response.json())


def create_service():
    ticket = services_info["ticket"]
    locker = services_info["locker"]
    towel = services_info["towel"]
    cabana = services_info["cabana"]
    ticket_list = [{
                    "name": "ticket",
                    "type": item["type"]
                } 
                    for item in ticket if item["amount_per_ticket"] == 1
    ]
    group_list = [{
                    "name": "ticket",
                    "type": item["type"]
                } 
                    for item in ticket if item["amount_per_ticket"] > 1
    ]
    locker_list = [{
                    "name": "locker",
                    "size": item["size"]
                } 
                for item in locker
    ]
    towel_list = [{
        "name": towel["name"]
    }]
    cabana_list = [
        {
            "name": "Cabana",
            "zone": item["zone"],
            "id": item["id"]
        } 
        for zone in cabana.values() for item in zone
    ]
    print(cabana_list)
    return (ticket_list, group_list, locker_list, towel_list, cabana_list)

### Select date ###
visit_date = ttk.DateEntry(services_frame, bootstyle = "danger", startdate = date.today())
visit_date.pack(pady = 15)

confirm_date_button = ttk.Button(services_frame, text = "Confirm visit date.", bootstyle = "danger, outline", command = get_services_in_date)
confirm_date_button.pack(pady = 15)

show_visit_date = ttk.Label(services_frame)
show_visit_date.pack(pady = 15)

##########################################################################
# Show services info

# Create a function to handle button clicks
def button_click(member_id, service_id):
    print(f"Button clicked for member {member_id} and service {service_id}")

services_background = [
    "solo_ticket.png",
    "group_ticket.png",
    "cabana.png",
    "locker_towel.png"
    #"/Users/sirima/Documents/Python/OOP/Project_final/towel.png"
]

def show_services_in_date():
    # Lists to store buttons and labels
    tickets, group_tickets, lockers, towels, cabanas = create_service()
    print("OK")
    labels = []
    services = []
    sub_buttons = [[], []]
    add_buttons = []


    for i in range(len(services_background)):
        # Replace this with the path to your image file
        image = Image.open(services_background[i])
        resized_image = image.resize((1000, 450))    
        photo = ImageTk.PhotoImage(resized_image)
        
        label = ttk.Label(services_frame, image = photo)
        label.pack(pady = 20)

        
        ## Create item button
        #ticket diew
        if i==0 :
            for j in range(len(tickets)):
                button1 = ttk.Button(services_frame, text = f"+", command = lambda i = i: add_item(tickets[j]))
                button2 = ttk.Button(services_frame, text = f"-", command = lambda i = i: reduce_item(tickets[j]))
                button1.command = reduce_item(tickets[j])
                button1.place(in_ = label, x = 790, y = 145 + j*80, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 145 + j*80, anchor = CENTER)
                
        #ticcket klum
        elif i==1 :
            for j in range(len(group_tickets)):
                button1 = ttk.Button(services_frame, text = f"+", command = lambda i = i: add_item(group_tickets[j]))
                button2 = ttk.Button(services_frame, text = f"-", command = lambda i = i: reduce_item(group_tickets[j]))
                button1.place(in_ = label, x = 790, y = 145 + j*78, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 145 + j*78, anchor = CENTER)

        #ticket 
        elif i==2 : 
            pass

        elif i==3 :
            for j in range(len(towels)):
                button1 = ttk.Button(services_frame, text = f"+", command = lambda i = i: add_item(towels[j]))
                button2 = ttk.Button(services_frame, text = f"+", command = lambda i = i: reduce_item(towels[j]))
                button1.place(in_ = label, x = 790, y = 180 + j*80, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 180 + j*80, anchor = CENTER)

            for j in range(len(lockers)):
                button1 = ttk.Button(services_frame, text = f"+", command = lambda i = i: add_item(lockers[j]))
                button2 = ttk.Button(services_frame, text = f"+", command = lambda i = i: reduce_item(lockers[j]))
                button1.place(in_ = label, x = 790, y = 270 + j*70, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 270 + j*70, anchor = CENTER)
            

        labels.append(label)
        label.image = photo 
        
        # def coupon_use(member_id, date):
        #     promocode = PromotioncodeEntry.get()
        #     API_ENDPOINT = f"http://127.0.0.1:8000/%7Bmember_id%7D/services/%7Bdate%7D"
        #     response = requests.put(API_ENDPOINT, json = {"code": promocode})

        #     if response.status_code == 200:
        #         data = response.json()  # แก้ไขตรงนี้
        #         print("Response Data:", data)
        #     else:
        #         print("Error:", response.text)

# promotioncode = ttk.Frame(services_frame, bootstyle="light")
# promotioncode.pack(pady=5)

# PromotioncodeEntry = ttk.Entry(
#     promotioncode,
#     bootstyle="success",
#     font=("Arial", 18),
#     foreground="blue",
#     width=20,
# )

# PromotioncodeEntry.pack(pady = 5, padx = 5)

# confirm_button = ttk.Button(services_frame, text="Confirm Code", command=lambda: coupon_function())
# confirm_button.pack()

# def coupon_function():
#     coupon_use(member_id, services_date)


# my_label = ttk.Label(promotioncode, text="")
# my_label.pack(pady=2)

# my_button = ttk.Button(services_frame, text="CONFRIM ORDER", bootstyle="dark")
# my_button.pack(pady=5, padx=5)

# cancel_order3 = ttk.Button(
#     services_frame,
#     text="BACK",
#     bootstyle="dark" # ,
#     # command=lambda: show_page(3, services_frame),
# )
# cancel_order3.pack(pady=20, padx=2, ipadx=1)
    
root.mainloop()

