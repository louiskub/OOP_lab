import threading
import tkinter as tk
from urllib.request import urlopen
from PIL import ImageTk

def getImageFromURL(url, controller):
    print('hai')
    try:
        controller.image = ImageTk.PhotoImage(file=urlopen(url))
        # notify controller that image has been downloaded
        controller.event_generate("<<ImageLoaded>>")
    except Exception as e:
        print(e)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.imagelab = tk.Label(self, width=50, height=5)
        self.imagelab.pack()

        self.bind("<<ImageLoaded>>", self.on_image_loaded)

        # start a thread to fetch the image
        url = "https://promptpay.io/0889876539/200.png"
        threading.Thread(target=getImageFromURL, args=(url, self)).start()

    def on_image_loaded(self, event):
        self.imagelab.config(image=self.image, width=1000, height=1000)

App().mainloop()