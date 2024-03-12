from tkinter import *
#from api import Item
import ttkbootstrap as ttk
from ttkbootstrap import Style, PRIMARY
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk
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

tickets_val = [IntVar() for i in range(4)]
group_tickets_val = [IntVar() for i in range(4)]
lockers_val = [IntVar() for i in range(2)]
towels_val = IntVar()
cabanas_val = IntVar()


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
    
    API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
    response = requests.get(API_ENDPOINT_SERVICES_DATE)
    #print(f"{services_date} - {response.json()}")
    
    if response.status_code == 200:
        if response.json().get(f"Services in {services_date}") != "Please select the available date.":
            services_info = response.json().get(f"Services in {services_date}")
            show_visit_date.config(text = f"Your visit date: {services_date}", foreground = 'black')
            create_service()
            show_services_in_date()
        else:
            show_visit_date.config(text = str(response.json().get(f"Services in {services_date}")), foreground = 'red')
    else:
        services_info = None
        print(f"API request failed with status code: {response.status_code}")
        #print(response.json())

def update_order(res):
    try:
        #print(detail)
        for detail in res["order_detail"]:
            items = detail["item"]
            print(items)
            if items["name"] == "towel":
                towels_val.set(detail["amount"])

            elif items["name"] == "cabana":
                cabanas_val.set(detail["amount"])

            elif items["name"] == "locker":
                #print("hello", end=" ")
                for i in range(len(lockers)):
                    if lockers[i]["size"] == items["size"]:
                        print("hello", end=" ")
                        lockers_val[i].set(detail["amount"])
                        break

            elif items["name"] == "ticket":
                if items["amount_per_ticket"] == 1:
                    for i in range(len(tickets)):
                        #print(tickets_val[i].get())
                        if tickets[i]["type"] == items["type"]:
                            print("hello", end=" ")
                            tickets_val[i].set(detail["amount"] )
                            break 
                else :
                    for i in range(len(group_tickets)):
                        if group_tickets[i]["type"] == items["type"]:
                            print("hello", end=" ")
                            group_tickets_val[i].set(detail["amount"])
                            break     
        print("OK")
        for i in tickets_val:
            print(i.get(), end=" ")
        print("")
        for i in group_tickets_val:
            print(i.get(), end=" ")
        print("")
        for i in lockers_val:
            print(i.get(), end=" ")
        print("")
        print(towels_val.get())
        print(cabanas_val.get())
    except :
        print(res)

def show_cabana_zone():
    zone_frame = Toplevel(root)
    zone_frame.title("Zone in DKUB Waterpark")
    zone_frame.geometry('1000x690')

    cabana_zone = "/Users/sirima/Documents/Python/OOP/Project_final/cabana_zone.png"
    image = Image.open(cabana_zone)
    resized_image = image.resize((1000, 690))
    photo = ImageTk.PhotoImage(resized_image)

    label = ttk.Label(zone_frame, image=photo)
    label.photo = photo  # Keep a reference to the PhotoImage object
    label.place(anchor = NW)
    
    # Define custom styles for each button
    button_styles = {
        'default': {'background': 'darkblue', 'foreground': 'white'},
        'wavepool': {'background': 'blue', 'foreground': 'white'},
        'activity': {'background': 'green', 'foreground': 'white'},
        'hill': {'background': 'brown', 'foreground': 'white'},
        'family': {'background': 'purple', 'foreground': 'white'}
    }
    # Create and configure buttons with custom styles
    for button_name, style_options in button_styles.items():
        button_style_name = f'{button_name}.TButton'
        ttk.Style().configure(button_style_name, 
                            background = style_options['background'], 
                            foreground = style_options['foreground'], 
                            font=('Arial', 26)
                            )

    zone_list = []
    for zone, cabana_list in services_info['cabana'].items():
        zone_list.append( ttk.Button(zone_frame, text=f"{zone} Zone", style = 'default.TButton') )

        # activity = ttk.Button(selection_frame, text="Activity and Relax Zone", style = 'default.TButton')
        # hill = ttk.Button(selection_frame, text="Hill Zone", style = 'default.TButton')
        # family = ttk.Button(selection_frame, text="Family Zone",style='default.TButton')
    
    zone_list[0].place(in_ = label, x = 335, y = 210, anchor = CENTER)
    zone_list[1].place(in_ = label, x = 320, y = 355, anchor = CENTER)
    zone_list[2].place(in_ = label, x = 670, y = 240, anchor = CENTER)
    zone_list[3].place(in_ = label, x = 540, y = 508, anchor = CENTER)

    close_button = ttk.Button(zone_frame, text="Close", bootstyle = 'danger', command=zone_frame.destroy)
    close_button.place(in_ = label,  x = 970, y = 15, anchor = CENTER)

def add_item(item):
    global member_id
    global services_date

    print(item, end="\n\n")
    API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"

    response = requests.post(API_ENDPOINT_SERVICES_DATE, data=json.dumps(item))
    try : 
        res = response.json()
        update_order(res)
    except:
        print(res)
    
def reduce_item(item):
    global member_id
    global services_date

    API_ENDPOINT_SERVICES_DATE  = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"

    response = requests.delete(API_ENDPOINT_SERVICES_DATE, data=json.dumps(item))
    res = response.json()
    update_order(res)

def create_service():
    ticket = services_info["ticket"]
    locker = services_info["locker"]
    towel = services_info["towel"]
    cabana = services_info["cabana"]
    global tickets
    global group_tickets
    global lockers
    global towels
    global cabanas
    tickets = [{
                    "name": "ticket",
                    "type": item["type"]
                } 
                    for item in ticket if item["amount_per_ticket"] == 1
    ]
    group_tickets = [{
                    "name": "ticket",
                    "type": item["type"]
                } 
                    for item in ticket if item["amount_per_ticket"] > 1
    ]
    lockers = [{
                    "name": "locker",
                    "size": item["size"]
                } 
                for item in locker
    ]
    towels = [{
        "name": "towel"
    }]
    cabanas = [
        {
            "name": "cabana",
            "zone": item["zone"],
            "id": item["id"]
        } 
        for zone in cabana.values() for item in zone
    ]
    #print(tickets, group_tickets, lockers, sep="\n\n\n")
    #print(cabanas)

### Select date ###
visit_date = ttk.DateEntry(services_frame, bootstyle = "danger", startdate = date.today())
visit_date.pack(pady = 15)

confirm_date_button = ttk.Button(services_frame, text = "Confirm visit date.", bootstyle = "danger, outline", command = get_services_in_date)
confirm_date_button.pack(pady = 15)

show_visit_date = ttk.Label(services_frame)
show_visit_date.pack(pady = 15)

##########################################################################
# Show services info

services_background = [
    "solo_ticket.png",
    "group_ticket.png",
    "cabana.png",
    "locker_towel.png"
    #"/Users/sirima/Documents/Python/OOP/Project_final/towel.png"
]

#tickets, group_tickets, lockers, towels, cabanas = create_service()

def show_services_in_date():
    # Lists to store buttons and labels
    
    for i in range(len(services_background)):
        # Replace this with the path to your image file
        image = Image.open(services_background[i])
        resized_image = image.resize((1000, 450))    
        photo = ImageTk.PhotoImage(resized_image)
        
        label = ttk.Label(services_frame, image = photo)
        label.pack(pady = 20)

        ## Create item button
        # solo ticket
        if i==0 :
            for j in range(len(tickets)):
                #print(tickets[j], end="  ")
                button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(tickets[j]))
                button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(tickets[j]))
                amount1 = ttk.Label(services_frame, textvariable=tickets_val[j], bootstyle="info", font=("Arial", 18))
                button1.place(in_ = label, x = 790, y = 145 + j*80, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 145 + j*80, anchor = CENTER)
                amount1.place(in_ = label, x = 865, y = 145 + j*80, anchor = CENTER)
                
        # group ticket 
        elif i==1 :
            print("\n\n")
            for j in range(len(group_tickets)):
                amount1 = ttk.Label(services_frame, textvariable=group_tickets_val[j], bootstyle="info", font=("Arial", 18))
                button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(group_tickets[j]))
                button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(group_tickets[j]))
                button1.place(in_ = label, x = 790, y = 145 + j*78, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 145 + j*78, anchor = CENTER)
                amount1.place(in_ = label, x = 865, y = 145 + j*78, anchor = CENTER)
        # cabana
        elif i==2 : 
            button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: show_cabana_zone())
            button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(towels[j]))
            amount1 = ttk.Label(services_frame, textvariable=cabanas_val, bootstyle="info", font=("Arial", 18))
            button1.place(in_ = label, x = 790, y = 270, anchor = CENTER)
            button2.place(in_ = label, x = 940, y = 270, anchor = CENTER)
            amount1.place(in_ = label, x = 865, y = 270, anchor = CENTER)
        #towel lockers
        elif i==3 :
            for j in range(len(towels)):
                button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(towels))
                button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(towels))
                amount1 = ttk.Label(services_frame, textvariable=towels_val, bootstyle="info", font=("Arial", 18))
                button1.place(in_ = label, x = 790, y = 180 + j*80, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 180 + j*80, anchor = CENTER)
                amount1.place(in_ = label, x = 865, y = 180 + j*80, anchor = CENTER)

            for j in range(len(lockers)):
                button1 = ttk.Button(services_frame, text = f"+", command = lambda j=j: add_item(lockers[j]))
                button2 = ttk.Button(services_frame, text = f"-", command = lambda j=j: reduce_item(lockers[j]))
                amount1 = ttk.Label(services_frame, textvariable=lockers_val[j], bootstyle="info", font=("Arial", 18))
                button1.place(in_ = label, x = 790, y = 270 + j*70, anchor = CENTER)
                button2.place(in_ = label, x = 940, y = 270 + j*70, anchor = CENTER)
                amount1.place(in_ = label, x = 865, y = 270 + j*70, anchor = CENTER)
            
        label.image = photo 


root.mainloop()
