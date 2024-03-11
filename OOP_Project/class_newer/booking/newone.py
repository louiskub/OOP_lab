import tkinter as tk

root = tk.Tk()
btn = tk.Button(root, 
                bg='#009658',
                fg='#b7f731',
                relief='flat',
                text='hello button',
                width=20)
btn.pack()

root.mainloop()