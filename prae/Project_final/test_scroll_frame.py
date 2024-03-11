from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk

# Create a function to handle button clicks
def button_click(image_path):
    print(f"Button clicked for image: {image_path}")

# Create Tkinter window
root = ttk.Window(themename='minty')
root.title("Scroll Frame")
root.geometry('1920x1080')

services = [
    "/Users/sirima/Documents/Python/OOP/Project_final/solo_ticket.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/group_ticket.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/cabana.png",
    "/Users/sirima/Documents/Python/OOP/Project_final/locker_towel.png"
]

my_frame = ScrolledFrame(root, autohide=False)
my_frame.pack(pady=10, padx=15, fill=BOTH, expand=YES)

# Lists to store buttons and labels
buttons = []
labels = []

for i, service in enumerate(services):
    image = Image.open(service)
    resized_image = image.resize((1000, 450))
    photo = ImageTk.PhotoImage(resized_image)

    label = ttk.Label(my_frame, image=photo)
    label.pack(pady=10)

    button_positions = [(750, 155), (750, 230), (750, 305), (750, 380), (920, 155), (920, 230), (920, 305), (920, 380)]

    for j, position in enumerate(button_positions):
        command = lambda i=i: button_click(services[i])
        text = "+" if j < 4 else "-"
        button = ttk.Button(my_frame, text=text, style="TButton", command=command)
        button.place(in_=label, x=position[0], y=position[1], anchor=CENTER)
        buttons.append(button)

    labels.append(label)
    label.image = photo  # Keep a reference to the image to prevent garbage collection

root.mainloop()
