import tkinter as tk
from tkinter import *
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import filedialog
import ttkbootstrap as ttk
import requests

x_size, y_size = 1920, 1080

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
            for chunk in req.iter_content(chunk_size=8192):
                file.write(chunk)

def main():
    root = ttk.Window(themename="flatly")
    root.geometry('1920x1080')
    my_style = ttk.Style(theme="flatly")

    member_id = 100000
    booking = get_show_all_booking(member_id)

    # Create a canvas to hold the ScrolledFrame with a background image
    canvas = Canvas(root, width=x_size, height=y_size)
    canvas.pack(fill=BOTH, expand=YES)

    # Load your background image
    background_image = PhotoImage(file="background.png")
    canvas.create_image(0, 0, anchor=NW, image=background_image)

    # Create a frame to hold the content
    content_frame = ttk.Frame(canvas)
    content_frame.pack(pady=10, padx=15)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas to scroll with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Bind the canvas to the function that updates the scroll region
    canvas.bind("<Configure>", lambda event, canvas=canvas: on_configure(event, canvas, content_frame))

    if len(booking) > 0:
        head1 = ttk.Label(
            root,
            text="Booking ID",
            bootstyle="success inverse",
            font=("Helvetica", 20)
        )
        head2 = ttk.Label(
            root,
            text="Visit Date",
            bootstyle="success inverse",
            font=("Helvetica", 20)
        )
        head3 = ttk.Label(
            root,
            text="Download",
            bootstyle="success inverse",
            font=("Helvetica", 20)
        )

        head1.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        head2.grid(row=0, column=1, padx=20, pady=20, sticky="w")
        head3.grid(row=0, column=2, padx=20, pady=20)
    for i in range(len(booking)):
        # Labels
        l1 = ttk.Label(
            root,
            text=f"{str(booking[i]['booking_id'])}",
            bootstyle="success",
            font=("Helvetica", 14)
        )
        l2 = ttk.Label(
            root,
            text=f"{str(booking[i]['visit_date'])}",
            bootstyle="info",
            font=("Helvetica", 14)
        )

        # Download button
        b = ttk.Button(
            root,
            text="Download",
            bootstyle="success outline",
            padding="10 5",  # Adjust padding as needed
            command=lambda: download(member_id, booking[i]["booking_id"])
        )

        # Packing widgets using grid
        l1.grid(row=i + 1, column=0, padx=20, pady=10, sticky="w")
        l2.grid(row=i + 1, column=1, padx=20, pady=10, sticky="w")
        b.grid(row=i + 1, column=2, padx=20, pady=10)

    root.mainloop()

def on_configure(event, canvas, frame):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfig(frame, height=canvas.winfo_height())  # Adjust frame height

if __name__ == "__main__":
    main()
