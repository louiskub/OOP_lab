import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import requests
member_id = 100000
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
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not save_path:
        return
    req = requests.get(api, stream=True)
    req.raise_for_status()
    with open(save_path, "wb") as file:
        for chunk in req.iter_content(chunk_size=8192):
            file.write(chunk)

api = get_show_all_booking(member_id)
root = ttk.Window(themename="darkly")

for i in range(len(api)):
    b = ttk.Button(root, text="Download", bootstyle="success", command=lambda: download(member_id, api[i]["booking_id"]))
    b.pack(side=TOP, padx=10, pady=15)

root.mainloop()
