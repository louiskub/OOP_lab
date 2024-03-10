import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests


root = ttk.Window(themename="superhero")
root.geometry('1920x1080')
#style
my_style = ttk.Style(theme="flatly")
#my_style.configure('my.louis', font=("Helvetica",30))

member_id = 100001
def get_all_services(member_id = ""):
    api = f"http://127.0.0.1:8000/{member_id}/services"
    if member_id == "":
        api = f"http://127.0.0.1:8000/services"
    req = requests.get(api)
    if req.status_code != 200:
        return "error"
    data = req.json()
    for key, val in data.items():
        print(key, val)

def get_show_all_booking(member_id):
    api = f"http://127.0.0.1:8000/{str(member_id)}/show_all_booking"
    req = requests.get(api)
    if req.status_code != 200:
        return "error"
    return req.json()
    #api = f"http://127.0.0.1:8000/{member_id}/show_all_booking"
    
def download(member_id, booking_id):
    api = f"http://127.0.0.1:8000/{str(member_id)}/finish_booking/{str(booking_id)}"
    req = requests.get(api, stream=True)
    try:
        req.json()
        #return "error"
    except:
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not save_path:
            return
        req.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)

booking = get_show_all_booking(member_id)
print(booking)
for i in range(len(booking)):
    l = ttk.Label(root, 
                text=f"Booking ID : {str(booking[i]['booking_id'])}     Date : { str(booking[i]['visit_date']) }",  
                bootstyle="info"
        )
    b = ttk.Button(root, 
                text="Download", 
                bootstyle="success outline", 
                #command=lambda: download(member_id, api[i]["booking_id"])
        )
    l.pack(side="left", padx=200)
    b.pack(side="right", padx=200)

root.mainloop()
