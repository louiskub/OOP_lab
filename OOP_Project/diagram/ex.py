import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class ImageDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Display App")

        # Load your .png image (replace 'your_image.png' with the actual filename)
        image_path = 'test.png'

        # Create a PhotoImage object from the image file
        self.image = tk.PhotoImage(file=image_path)
        # Create a ttk Label to display the image
        self.image_label = ttk.Label(root, image=self.image, background='green')
        self.image_label.pack(padx=20, pady=20)

if __name__ == "__main__":
    # Create a themed Tkinter window using ttkbootstrap
    style = Style(theme="flatly")
    root = style.master

    # Create and run the ImageDisplayApp
    app = ImageDisplayApp(root)
    root.mainloop()
