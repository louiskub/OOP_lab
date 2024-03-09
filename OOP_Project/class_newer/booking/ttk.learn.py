import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")

b1 = ttk.Button(root, text="Button 1", bootstyle="info reverse")
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle="danger outline")
b2.pack(side=TOP, padx=5, pady=10)

b3 = ttk.Button(root, text="Button 2", bootstyle="danger")
b3.pack(side=RIGHT, padx=5, pady=10)
root.mainloop()
