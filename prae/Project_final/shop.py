from tkinter import *
import ttkbootstrap as ttk
from waterpark import WaterPark
from datetime import date
import requests
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk

system = WaterPark()
images = []
photo = []
services_label = []

# label = tk.Label(root, image = PhotoImage(file = ticket[0]))
# label.place(relheight = 1, relwidth = 1)

root = ttk.Window(themename = 'minty')
root.title("Scroll Frame")
root.geometry('1920x1080')
services = [
    "/Users/sirima/Documents/Python/OOP/Project_final/solo_ticket.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/group_ticket.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/cabana.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/locker.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/towel.png"
]

my_frame = ScrolledFrame(root, autohide = False)
my_frame.pack(pady = 5, padx = 15, fill = BOTH, expand = YES)

for i in range(len(services)):
    # Replace this with the path to your image file
    images.append(Image.open(services[i]))
    resized_image = images[i].resize((1000, 450))
    photo.append(ImageTk.PhotoImage(resized_image))

    # Display the image outside the buttons
    services_label.append(ttk.Label(my_frame, image = photo[i]))
    services_label[i].pack(pady = 10)

# for x in range(2):
#     button = ttk.Button(my_frame, text=f"Click Me! {x}", bootstyle="info")
#     button.pack(padx=15)

    # # Add an image to each button
    # button.config(image=photo, compound=LEFT)

root.mainloop()