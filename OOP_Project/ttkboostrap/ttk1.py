from tkinter import *
import ttkbootstrap as ttk
from datetime import date
import requests
from PIL import Image, ImageTk

root = ttk.Window(themename="minty")
root.title("DKUB WATERPARK")
root.geometry("1920x1080")

image_path = "6963703.jpg"  # Provide the path to your image file
image_path2 ="Bank.jpg"
image_path3 ="DKUB_logo.jpg"
image = Image.open(image_path)
image2 = Image.open(image_path2)
image3 = Image.open(image_path3)
resized_image = image.resize((120, 120), Image.BICUBIC)  # Adjust the size as needed
image = ImageTk.PhotoImage(resized_image)
resized_image2 = image2.resize((120, 120), Image.BICUBIC)  # Adjust the size as needed
image2 = ImageTk.PhotoImage(resized_image2)
resized_image3 = image3.resize((1000, 150), Image.BICUBIC)  # Adjust the size as needed
image3 = ImageTk.PhotoImage(resized_image3)

# สร้างตัวแปร global สำหรับแสดงข้อมูล
name_label = None
email_label = None
telephone_label = None
date_of_visit_label = None

frame_home = ttk.Frame(root)
frame_order = ttk.Frame(root)
frame_home_1 = ttk.Frame(root)
frame_view_member = ttk.Frame(root)


############################################################################################################
def show_page_1(page):

    if page == 4:
        frame_home_1.pack()


show_page_1(4)


def show_page(page, current_frame):
    current_frame.pack_forget()  # ซ่อน frame ปัจจุบัน

    if page == 1:
        frame_home.pack()

    if page == 2:
        frame_order.pack()

    if page == 3:
        frame_home_1.pack()

    if page == 4:
        frame_view_member.pack()


############################################################################################################


def coupon_use(member_id,date):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/services/{date}"
    print(promocode)
    response = requests.put(
        API_ENDPOINT, json={"code": promocode}
    )
    if response.status_code == 200:
         data = response.json()  # แก้ไขตรงนี้
         print("Response Data:", data)
    else:
        print("Error:", response.text)
    
    root.after(10000, lambda: coupon_use(member_id,date))


def speak():
    my_label.config(text=f"You typed : {PromotioncodeEntry.get()}")

promotioncode = ttk.Frame(frame_order, bootstyle="light")
promotioncode.pack(pady=5)


PromotioncodeEntry = ttk.Entry(
    promotioncode,
    bootstyle="success",
    font=("Helvetica", 18),
    foreground="blue",
    width=20,
)
PromotioncodeEntry.pack(pady=5, padx=5)

promocode = PromotioncodeEntry.get()

my_button = ttk.Button(
    promotioncode, text="CONFRIM CODE", bootstyle="dark", command=speak
)
my_button.pack(pady=5, padx=5)

my_label = ttk.Label(promotioncode, text="")
my_label.pack(pady=2)

my_button = ttk.Button(frame_order, text="CONFRIM ORDER", bootstyle="dark")
my_button.pack(pady=5, padx=5)

cancel_order3 = ttk.Button(
    frame_order,
    text="BACK",
    bootstyle="dark",
    command=lambda: show_page(3, frame_order),
)
cancel_order3.pack(pady=20, padx=2, ipadx=1)


############################################################################################################


def get_order_detail(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]


        for order_detail in order["order_detail"]:
            item_name = order_detail["item"]
            name = item_name["name"]
            price = item_name["price"]
            subtotal = order_detail["total_price"]
            amount = order_detail["amount"]
            if "size" in item_name:
                size = item_name["size"]
            else:
                size = "None"

            order_label = ttk.Label(
                Order_detail_frame,
                text=f"Item Name: {name},    Size: {size},    Amount: {amount},     Price: {price},       Subtotal: {subtotal}",
                font=("Helvetica", 14),
                bootstyle="dark",
            )
            order_label.pack(pady=5, padx=10, ipadx=10)

        name_label.config(text=f"Name: {data['member']['name']}")
        email_label.config(text=f"Email: {data['member']['email']}")
        telephone_label.config(text=f"Telephone: {data['member']['phone_no']}")
        date_of_visit_label.config(text=f"Date of Visit: {order['visit_date']}")
    else:
        print("Error")


############################################################################################################



def get_order_detail_total(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]
        order_total = order["total"]
        order_discount = order["discount"]
        Sub_Total.config(text=f"Grand Total: {order_total}")
        Discount.config(text=f"Discount:{order_discount}")
    else:
        print("Error")

    root.after(10000, lambda: get_order_detail_total(member_id))

    # สร้าง Label สำหรับแสดงข้อมูล
    

# Contact Detail

Contact_Detail = ttk.Label(
    frame_home,image=image3,
)
Contact_Detail.pack(pady=10)

Contact_Detail = ttk.Label(
    frame_home, text="Contact Detail", font=("Helvetica", 18), foreground="green"
)
Contact_Detail.pack(pady=10)

Contact_Detail_Frame = ttk.Frame(frame_home)
Contact_Detail_Frame.pack(pady=10, ipadx=100)

name_label = ttk.Label(
    Contact_Detail_Frame, text="Name :", font=("Helvetica", 14)
)
name_label.pack(pady=5, padx=5)

email_label = ttk.Label(
    Contact_Detail_Frame, text="Email :", font=("Helvetica", 14)
)
email_label.pack(pady=5, padx=5)

telephone_label = ttk.Label(
    Contact_Detail_Frame, text="Telephone :", font=("Helvetica", 14)
)
telephone_label.pack(pady=5, padx=5)

date_of_visit_label = ttk.Label(
    Contact_Detail_Frame,
    text="Date of Visit :",
    font=("Helvetica", 14)
)
date_of_visit_label.pack(pady=5, padx=5)

# Order Detail
Order_detail = ttk.Label(
    frame_home, text="Order Detail", font=("Helvetica", 18), foreground="green"
)
Order_detail.pack(pady=10)

Order_detail_frame = ttk.Frame(frame_home)
Order_detail_frame.pack(pady=10)

Order_detail_frame1 = ttk.Frame(frame_home)
Order_detail_frame1.pack(pady=10)

Sub_Total = ttk.Label(
    Order_detail_frame1, text="Sub Total :", font=("Helvetica", 14)
)
Sub_Total.pack(pady=5, padx=5)

Discount = ttk.Label(
    Order_detail_frame1, text="Discount :", font=("Helvetica", 14)
)
Discount.pack(pady=5, padx=5)

# Payment Method
Payment_Method = ttk.Label(
    frame_home, text="Payment Method", font=("Helvetica", 18), foreground="green"
)
Payment_Method.pack(pady=10)

button1 = ttk.Button(frame_home, image=image, command=lambda: show_page(3,frame_home))
button1.pack(side="left", pady=10, padx=10)

button2 = ttk.Button(frame_home, image=image2, command=lambda: show_page(4,frame_home))
button2.pack(side="left", pady=10, padx=500)

cancel_order3 = ttk.Button(frame_home, text="BACK", command=lambda: show_page(3, frame_home))
cancel_order3.pack(side="bottom", pady=100, padx=1)

################################################################################################################################


def get_member_detail(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/show_confirm"
    response = requests.get(API_ENDPOINT)

    if response.status_code == 200:
        data = response.json()
        booking = data["booking"]
        order = booking["order"]

        Member_name_view.config(text=f"Name: {data['member']['name']}")
        Email_view.config(text=f"Email: {data['member']['email']}")
        telephone_view.config(text=f"Telephone: {data['member']['phone_no']}")
    else:
        print("Error")


Contact_Detail = ttk.Label(
    frame_view_member, text="Member Detail", font=("Helvetica", 18), foreground="green" ,)
Contact_Detail.pack(pady=10)

Member_detail_frame = ttk.Frame(frame_view_member, bootstyle="light")
Member_detail_frame.pack(pady=10,ipadx=100)

Member_name_view = ttk.Label(
    Member_detail_frame, text="Name :", font=("Helvetica", 14)
)
Member_name_view.pack(pady=10, padx=10, ipadx=10)

Email_view = ttk.Label(
    Member_detail_frame, text="Email :", font=("Helvetica", 14)
)
Email_view.pack(pady=10, padx=10, ipadx=10)

telephone_view = ttk.Label(
    Member_detail_frame, text="Telephone :", font=("Helvetica", 14)
)
telephone_view.pack(pady=10, padx=10, ipadx=10)

cancel_order3 = ttk.Button(
    Member_detail_frame,
    text="BACK",
    bootstyle="dark",
    command=lambda: show_page(3, frame_view_member),
)
cancel_order3.pack(pady=20, padx=2, ipadx=1)

################################################################################################################################


############################################################################################################################


get_order_detail("100001")

coupon_use("100001","2024-03-15")
get_order_detail_total("100001")
get_member_detail("100001")


home = ttk.Button(
    frame_home_1,
    text="VIEW_ORDER_DETAIL",
    bootstyle="dark",
    command=lambda: show_page(1, frame_home_1),
)
home.pack(pady=20, padx=2, ipadx=1)

home2 = ttk.Button(
    frame_home_1,
    text="VIEW_COUPON_DETAIL",
    bootstyle="dark",
    command=lambda: show_page(2, frame_home_1),
)
home2.pack(pady=20, padx=2, ipadx=1)

home3 = ttk.Button(
    frame_home_1,
    text="VIEW_MEMBER_DETAIL",
    bootstyle="dark",
    command=lambda: show_page(4, frame_home_1),
)
home3.pack(pady=20, padx=2, ipadx=1)


root.mainloop()