from tkinter import *
import ttkbootstrap as ttk
from datetime import date
import requests

root = ttk.Window(themename="minty")
root.title("DKUB WATERPARK")
root.geometry("1600x900")

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


def coupon_use(member_id):
    API_ENDPOINT = f"http://127.0.0.1:8000/{member_id}/services"
    response = requests.put(
        API_ENDPOINT, json={"info": {"coupon_code": "your_coupon_code"}}
    )

    if response.status_code == 200:
        print("Coupon added successfully")

    else:
        print("Error:", response.text)


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
        order_total = order["total"]
        order_discount = order["discount"]

        for order_detail in order["order_detail"]:
            item_name = order_detail["Item Name"]
            price = order_detail["Price"]
            subtotal = order_detail["Subtotal"]
            amount = order_detail["Qty"]
            item_type = ""  # ใส่ตามข้อมูลใน order_detail ที่ได้รับจาก FastAPI

            order_label = ttk.Label(
                Order_detail_frame,
                text=f"Item Name: {item_name}, Type: {item_type}, Amount: {amount}, Price: {price}, Subtotal: {subtotal}",
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


Contact_Detail = ttk.Label(
    frame_home, text="Contact Detail", font=("Helvetica", 18), bootstyle="info"
)
Contact_Detail.grid(pady=10)

Contact_Detail_Frame = ttk.Frame(frame_home, bootstyle="light")
Contact_Detail_Frame.pack(pady=10)

name_label = ttk.Label(
    Contact_Detail_Frame, text="Name :", font=("Helvetica", 14), bootstyle="dark"
)
name_label.pack(pady=10, padx=10, ipadx=300)

email_label = ttk.Label(
    Contact_Detail_Frame, text="Email :", font=("Helvetica", 14), bootstyle="dark"
)
email_label.pack(pady=10, padx=10, ipadx=300)

telephone_label = ttk.Label(
    Contact_Detail_Frame, text="Telephone :", font=("Helvetica", 14), bootstyle="dark"
)
telephone_label.pack(pady=10, padx=10, ipadx=280)

date_of_visit_label = ttk.Label(
    Contact_Detail_Frame,
    text="Date of Visit :",
    font=("Helvetica", 14),
    bootstyle="dark",
)
date_of_visit_label.pack(pady=10, padx=10, ipadx=275)

Order_detail = ttk.Label(
    frame_home, text="Order Detail", font=("Helvetica", 18), bootstyle="info"
)
Order_detail.pack(pady=10)

Order_detail_frame = ttk.Frame(frame_home, bootstyle="light")
Order_detail_frame.pack(pady=10)

Order_detail_frame1 = ttk.Frame(frame_home, bootstyle="light")
Order_detail_frame1.pack(pady=10)

Sub_Total = ttk.Label(
    Order_detail_frame1, text="Sub Total :", font=("Helvetica", 14), bootstyle="dark"
)
Sub_Total.pack(pady=10, padx=10, ipadx=290)

Discount = ttk.Label(
    Order_detail_frame1, text="Discount :", font=("Helvetica", 14), bootstyle="dark"
)
Discount.pack(pady=10, padx=10, ipadx=290)

Payment_Method = ttk.Label(
    frame_home, text="Payment Method", font=("Helvetica", 18), bootstyle="info"
)
Payment_Method.pack(pady=10)

cancel_order3 = ttk.Button(
    frame_home, text="BACK", bootstyle="dark", command=lambda: show_page(3, frame_home)
)
cancel_order3.pack(pady=20, padx=2, ipadx=1)


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
    frame_view_member, text="Member Detail", font=("Helvetica", 18), bootstyle="info"
)
Contact_Detail.pack(pady=10)

Member_detail_frame = ttk.Frame(frame_view_member, bootstyle="light")
Member_detail_frame.pack(pady=10)

Member_name_view = ttk.Label(
    Member_detail_frame, text="Name :", font=("Helvetica", 14), bootstyle="dark"
)
Member_name_view.pack(pady=10, padx=10, ipadx=300)

Email_view = ttk.Label(
    Member_detail_frame, text="Email :", font=("Helvetica", 14), bootstyle="dark"
)
Email_view.pack(pady=10, padx=10, ipadx=300)

telephone_view = ttk.Label(
    Member_detail_frame, text="Telephone :", font=("Helvetica", 14), bootstyle="dark"
)
telephone_view.pack(pady=10, padx=10, ipadx=280)

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
