import tkinter as tk
from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import filedialog
import ttkbootstrap as ttk
import requests

x_size, y_size = 1920, 1080


def get_all_services(member_id=""):
    api = f"http://127.0.0.1:8000/{member_id}/services"
    if not member_id:
        api = "http://127.0.0.1:8000/services"
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

def download(member_id, booking_id):
    api = f"http://127.0.0.1:8000/{str(member_id)}/finish_booking/{str(booking_id)}"
    req = requests.get(api, stream=True)
    
    try:
        print(req.json())
    except:
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not save_path:
            return
        
        req.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in req.iter_booking(chunk_size=8192):
                file.write(chunk)

def main():
    
    member_id = 100000
    booking = get_show_all_booking(member_id)

    root = ttk.Window(themename = 'flatly')
    root.title("Scroll Frame")
    root.geometry('1920x1080')


    # canvas = Canvas(root, width=x_size, height=y_size)
    #background_image = PhotoImage(file="background.png")
    # canvas.create_image(0, 0, anchor=NW, image=background_image)
    # canvas.pack()
    # Load your background image
    
    booking_frame = Frame(root)
    booking_frame.pack()
    background_image = PhotoImage(file="background.png")
    label = ttk.Label(booking_frame, image=background_image)
    label.pack()

    # tab = ttk.Label(booking_frame, text="   ",padding=14, width=250, background='#009658')
    # tab.place(x=0,y=0)
    home_button = tk.Button(root, 
                bg='#ffffff',
                relief='flat',
                text='Home',
                width=20)
    home_button.place(x=x_size*0.02, y=16)
    for i in range(len(booking)):
        # Labels
        b = ttk.Button(booking_frame, text="Download", bootstyle="success outline",padding="10 5",  # Adjust padding as needed
        command=lambda: download(member_id, booking[i]["booking_id"]))

        
        # Positioning using place
        line.place(x=x_size*0.5, y=228 + i * 40, anchor = CENTER)
        l1.place(x=x_size*0.3, y=220 + i * 40, anchor = CENTER)
        l2.place(x=x_size*0.5, y=220 + i * 40, anchor = CENTER)
        b.place(x=x_size*0.71, y=220 + i * 40, anchor = CENTER)
        
    root.mainloop()

if __name__ == "__main__":
    main()