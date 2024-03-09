import tkinter as tk
from tkinter import ttk
from io import BytesIO
import requests
import fitz  # PyMuPDF

def fetch_pdf_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to fetch PDF. Status code: {response.status_code}")
        return None

def display_pdf(pdf_content):
    pdf_document = BytesIO(pdf_content)
    # pdf_reader = fitz.open(pdf_document)
    # total_pages = pdf_reader.page_count

    # root = tk.Tk()
    # root.title("PDF Viewer")

    # notebook = ttk.Notebook(root)
    # notebook.pack(expand=True, fill='both')

    # for page_number in range(total_pages):
    #     page = pdf_reader[page_number]
    #     img = page.get_pixmap()
    #     img_bytes = img.get_image_data()
    #     img_tk = tk.PhotoImage(data=img_bytes)

    #     frame = ttk.Frame(notebook)
    #     label = ttk.Label(frame, image=img_tk)
    #     label.pack()
    #     frame.bind("<Configure>", lambda event, label=label: resize_image(event, label))

    #     notebook.add(frame, text=f"Page {page_number + 1}")

    # root.mainloop()

def resize_image(event, label):
    new_width = event.width
    new_height = event.height
    image = label._image.zoom(new_width // label._image.width())
    label.config(image=image)
    label.image = image



if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/100/finish_booking/100000"
    pdf_content = fetch_pdf_from_api(api_url)

    if pdf_content:
        display_pdf(pdf_content)
