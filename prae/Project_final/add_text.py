from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk

# Open the image
image_path = "/Users/sirima/Documents/Python/OOP/Project_final/solo_ticket.png"
image = Image.open(image_path)

# Create Tkinter window
root = ttk.Window(themename = 'superhero')
root.title("Image with Button")

# Convert the image to Tkinter PhotoImage format
image_tk = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = ttk.Label(root, image = image_tk)
image_label.pack()

# Create a button
button_label = "Click Me!"
button = ttk.Button(root, text=button_label, style="TButton")

# Place the button on the image label
button.place(relx=0.8, rely=0.3)  # Adjust the relative position as needed

root.mainloop()
