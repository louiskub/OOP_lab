from tkinter import *
from api import Item
import ttkbootstrap as ttk
from ttkbootstrap import Style, PRIMARY
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk, ImageDraw, ImageFont
from datetime import datetime, date
from tkcalendar import Calendar
import requests

member_id = 0
services_date = None
services_info = None

API_ENDPOINT_LOGIN = "http://127.0.0.1:8000/login"
API_ENDPOINT_SUBSCRIPTION = "http://127.0.0.1:8000/subscription"
API_ENDPOINT_SERVICES = f"http://127.0.0.1:8000/{member_id}/services"
# API_ENDPOINT_SERVICES_DATE = f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
API_ENDPOINT_ADD_ITEM = f"http://127.0.0.1:8000//{member_id}/services/{services_date}"

# Create Tkinter window
root = ttk.Window(themename="flatly")
root.title("Scroll Frame")
root.geometry("1920x1080")

# Create a ScrolledFrame for pictures
services_frame = ScrolledFrame(root, autohide=True)
services_frame.pack(pady=10, padx=15, fill=BOTH, expand=YES)


def change_format_date(str_date):
    month = str_date[0:2]
    day = str_date[3:5]
    year = str_date[6:10]
    ymd = f"{year}-{month}-{day}"
    return ymd


def get_services_in_date():
    global member_id
    global services_date
    global services_info
    services_date = visit_date.entry.get()
    services_date = change_format_date(services_date)
    show_visit_date.config(text=f"Your visit date: {services_date}")

    API_ENDPOINT_SERVICES_DATE = (
        f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
    )
    response = requests.get(API_ENDPOINT_SERVICES_DATE)

    if response.status_code == 200:
        services_info = response.json().get(f"Services in {services_date}")
        print(services_info)
    else:
        print(f"API request failed with status code: {response.status_code}")
        services_info = None


def get_item_name(item_id):
    id = 0
    item = {}
    global services_info
    if services_info == None:
        return "Services not fornd."
    for item_name, items in services_info.items():
        if item_name == "ticket":
            for ticket in items:
                item[id] = Item(name=ticket["name"])


def add_item():
    global member_id
    global services_date
    API_ENDPOINT_SERVICES_DATE = (
        f"http://127.0.0.1:8000/{member_id}/services/{services_date}"
    )
    response = requests.post(API_ENDPOINT_SERVICES_DATE)


### Select date ###
visit_date = ttk.DateEntry(services_frame, bootstyle="danger", startdate=date.today())
visit_date.pack(pady=15)

confirm_date_button = ttk.Button(
    services_frame,
    text="Confirm visit date.",
    bootstyle="danger, outline",
    command=get_services_in_date,
)
confirm_date_button.pack(pady=15)

show_visit_date = ttk.Label(services_frame)
show_visit_date.pack(pady=15)

##########################################################################
# Show services info


# Create a function to handle button clicks
def button_click(member_id, service_id):
    print(f"Button clicked for member {member_id} and service {service_id}")


services_background = [
    "/Users/sirima/Documents/Python/OOP/Project_final/solo_ticket.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/group_ticket.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/cabana.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/locker_towel.png",
    # "/Users/sirima/Documents/Python/OOP/Project_final/towel.png"
]

# Lists to store buttons and labels
buttons = []
labels = []
tickets = []
lockers = []
cabanas = []

for i in range(len(services_background)):
    # Replace this with the path to your image file
    image = Image.open(services_background[i])
    resized_image = image.resize((1000, 450))
    photo = ImageTk.PhotoImage(resized_image)

    label = ttk.Label(services_frame, image=photo)
    label.pack(pady=20)

    if i == 0:
        pass

    if i < 2:

        ## Create item button
        button1 = ttk.Button(
            services_frame, text=f"+", command=lambda i=i: button_click(services[i])
        )
        button2 = ttk.Button(
            services_frame, text=f"+", command=lambda i=i: button_click(services[i])
        )
        button3 = ttk.Button(
            services_frame, text=f"+", command=lambda i=i: button_click(services[i])
        )
        button4 = ttk.Button(
            services_frame, text=f"+", command=lambda i=i: button_click(services[i])
        )
        button5 = ttk.Button(
            services_frame, text=f"-", command=lambda i=i: button_click(services[i])
        )
        button6 = ttk.Button(
            services_frame, text=f"-", command=lambda i=i: button_click(services[i])
        )
        button7 = ttk.Button(
            services_frame, text=f"-", command=lambda i=i: button_click(services[i])
        )
        button8 = ttk.Button(
            services_frame, text=f"-", command=lambda i=i: button_click(services[i])
        )

        # Place the button on top of the image
        button1.place(in_=label, x=750, y=155, anchor=CENTER)
        button2.place(in_=label, x=750, y=230, anchor=CENTER)
        button3.place(in_=label, x=750, y=305, anchor=CENTER)
        button4.place(in_=label, x=750, y=380, anchor=CENTER)
        button5.place(in_=label, x=920, y=155, anchor=CENTER)
        button6.place(in_=label, x=920, y=230, anchor=CENTER)
        button7.place(in_=label, x=920, y=305, anchor=CENTER)
        button8.place(in_=label, x=920, y=380, anchor=CENTER)

        # Store the button and label in the lists
        buttons.append(button1)
        buttons.append(button2)
        buttons.append(button3)
        buttons.append(button4)
        buttons.append(button5)
        buttons.append(button6)
        buttons.append(button7)
        buttons.append(button8)

    else:
        button1 = ttk.Button(
            services_frame,
            text=f"+",
            style="TButton",
            command=lambda i=i: button_click(services[i]),
        )
        button2 = ttk.Button(
            services_frame,
            text=f"+",
            style="TButton",
            command=lambda i=i: button_click(services[i]),
        )
        button3 = ttk.Button(
            services_frame,
            text=f"+",
            style="TButton",
            command=lambda i=i: button_click(services[i]),
        )
        button4 = ttk.Button(
            services_frame,
            text=f"-",
            style="TButton",
            command=lambda i=i: button_click(services[i]),
        )
        button5 = ttk.Button(
            services_frame,
            text=f"-",
            style="TButton",
            command=lambda i=i: button_click(services[i]),
        )
        button6 = ttk.Button(
            services_frame,
            text=f"-",
            style="TButton",
            command=lambda i=i: button_click(services[i]),
        )

        # Place the button on top of the image
        button1.place(in_=label, x=750, y=230, anchor=CENTER)
        button2.place(in_=label, x=750, y=305, anchor=CENTER)
        button3.place(in_=label, x=750, y=380, anchor=CENTER)
        button4.place(in_=label, x=920, y=230, anchor=CENTER)
        button5.place(in_=label, x=920, y=305, anchor=CENTER)
        button6.place(in_=label, x=920, y=380, anchor=CENTER)

        # Store the button and label in the lists
        buttons.append(button1)
        buttons.append(button2)
        buttons.append(button3)
        buttons.append(button4)
        buttons.append(button5)
        buttons.append(button6)

    # Keep a reference to the image to prevent garbage collection
    labels.append(label)
    label.image = photo

    def coupon_use(member_id, date):
        promocode = PromotioncodeEntry.get()
        API_ENDPOINT = f"http://127.0.0.1:8000/%7Bmember_id%7D/services/%7Bdate%7D"
        response = requests.put(API_ENDPOINT, json={"code": promocode})

        if response.status_code == 200:
            data = response.json()  # แก้ไขตรงนี้
            print("Response Data:", data)
        else:
            print("Error:", response.text)


promotioncode = ttk.Frame(services_frame, bootstyle="light")
promotioncode.pack(pady=5)

PromotioncodeEntry = ttk.Entry(
    promotioncode,
    bootstyle="success",
    font=("Arial", 18),
    foreground="blue",
    width=20,
)

PromotioncodeEntry.pack(pady=5, padx=5)

confirm_button = ttk.Button(
    services_frame, text="Confirm Code", command=lambda: coupon_function()
)
confirm_button.pack()


def coupon_function():
    coupon_use(member_id, services_date)


my_label = ttk.Label(promotioncode, text="")
my_label.pack(pady=2)

my_button = ttk.Button(services_frame, text="CONFRIM ORDER", bootstyle="dark")
my_button.pack(pady=5, padx=5)

cancel_order3 = ttk.Button(
    services_frame,
    text="BACK",
    bootstyle="dark",  # ,
    # command=lambda: show_page(3, services_frame),
)
cancel_order3.pack(pady=20, padx=2, ipadx=1)

root.mainloop()
