import tkinter as tk
from tkinter import *
from ttkbootstrap import Style, Label, Entry, Button, PhotoImage
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date, datetime
import requests


API_ENDPOINT1 = "http://127.0.0.1:8000/login"
API_ENDPOINT3 = "http://127.0.0.1:8000/subscription"
#response = requests.get(API_ENDPOINT1)

root = ttk.Window(themename="minty")#themename="solar"
root.geometry('1920x1080')
bg_pic = PhotoImage(file='waterpark.png')
bg2_pic = PhotoImage(file='water.png')

user_id_V = 0


def set_user_id(user_id):
    global user_id_V
    user_id_V = user_id
    return user_id_V
    
def log_out():
    set_user_id(0)
    print(user_id_V)
    home_page()
    
def login_page():
    clear_window(root)
    root.title("Login")
    print(f"Before :{user_id_V}")
    
    label = tk.Label(root, image=bg2_pic)
    label.place(relheight=1, relwidth=1)
    
    f = ttk.Frame(root, borderwidth=20, relief="ridge",padding =20)
    f.place(relx=0.5, rely=0.3, anchor=ttk.CENTER)
    
    f2 =ttk.Frame(root)
    f2.place(relx=0.5, rely=0.5, anchor=ttk.CENTER)
    
    style = Style()
    style.configure("TButton",background="white",foreground="black")# กำหนดสีพื้นหลังและสีข้อความให้กับปุ่ม
    
    
    def login():
        
        email_l = email_entry.get()
        password_l = password_entry.get()
        payload = {
            "email": email_l,
            "password": password_l
        }
        response = requests.post(API_ENDPOINT1, json=payload)
        if email_l== ""  or password_l== "":
            result_label.config(text="Please fill all")
        elif response.json().get("Result") == "Login successful." :
            user_id_V=set_user_id(response.json().get("mem_id"))
            result_label.config(text="Login successful.")
            print(user_id_V)
            home_member_page()
        else:
            result_label.config(text="Incorrect username or password.")
        
    x=2

    # สร้าง Label และ Entry สำหรับชื่อผู้ใช้
    message_label = ttk.Label(f, text="Log in",font = ("Arial", 12, "bold"))
    message_label.grid(row=x-2, columnspan=2)
    
    blank_label = ttk.Label(f, text="")
    blank_label.grid(row=x-1, columnspan=2)
     
     
    email_label = ttk.Label(f, text="Email : ")
    email_label.grid(row=x+0, column=0,sticky='w')

    email_entry = ttk.Entry(f)
    email_entry.grid(row=x+0, column=1, padx=10, pady=5,)

    # สร้าง Label และ Entry สำหรับรหัสผ่าน
    password_label = ttk.Label(f, text="Password : ")
    password_label.grid(row=x+1, column=0,sticky='w')

    password_entry = ttk.Entry(f, show="*")
    password_entry.grid(row=x+1, column=1, padx=10, pady=5)
    
    blank_label = ttk.Label(f, text="")
    blank_label.grid(row=x+2, columnspan=2)

    # สร้างปุ่มเข้าสู่ระบบ
    login_button = ttk.Button(f, text="sign in", command=login,style=PRIMARY)
    login_button.grid(row=x+3, columnspan=2, padx=10, pady=5)

    # สร้าง Label สำหรับผลลัพธ์
    result_label = ttk.Label(f, text="")
    result_label.grid(row=x+4, columnspan=2, padx=10, pady=5)
    
    # blank_label = ttk.Label(f, text="")
    # blank_label.grid(row=x+5, columnspan=2)
    
    be_member_button = ttk.Button(f2, text="register", command=subscription_page,style=PRIMARY)
    be_member_button.grid(row=x, columnspan=2)
    
    home_button = ttk.Button(root, text="Home", command=home_page,width=10,style=PRIMARY,padding=10)
    home_button.grid(row=0,column=0)
    
def subscription_page():
    clear_window(root)
    f = ttk.Frame(root, borderwidth=5, relief="ridge",padding =20)
    f.place(relx=0.5, rely=0.3, anchor=ttk.CENTER)
    
    style = Style(theme='superhero')
     
    def become_member():
        
        name = name_entry.get()
        email = email_entry.get()
        phone_no = phone_no_entry.get()
        
        date_str = birthday.entry.get()
        try:
            datetime.strptime(date_str, '%m/%d/%Y')  # ตรวจสอบว่าสามารถแปลงวันที่เป็นรูปแบบที่ถูกต้องหรือไม่
        except ValueError:
            result_label.config(text="Incorrect date format", foreground="red")
            return
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")# แปลงสตริงเป็นวัตถุ datetime
        birth_day =  date_obj.strftime("%Y-%m-%d")
        
        password = password_entry.get()
        
        
        
        payload = {
            "name": name,
            "email": email,
            "phone_no": phone_no,
            "birthday": birth_day,
            "password": password
        }
        #print("Becoming a member...")
        
        
            
        response = requests.post(API_ENDPOINT3, json=payload)
        if name== "" or email== "" or phone_no== "" or birth_day== "" or password== "":
            result_label.config(text="Please fill in complete information", foreground="red")
            
        elif response.json().get("Result") ==  'Membership registration completed.':
            result_label.config(text="Membership registration completed.",foreground="black")
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            phone_no_entry.delete(0, tk.END)
            birthday.entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            #login_page()
        else :
            result_label.config(text=response.json().get("Result"),foreground="red")
            print(response.json().get("Result") )
        print(response.json().get("Result") )



    # สร้างสไตล์ ttkbootstrap
    style = Style(theme='minty')


    # สร้าง Label และ Entry สำหรับกรอกชื่อ
    name_label = Label(f, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=5,sticky='w')

    name_entry = Entry(f)
    name_entry.grid(row=0, column=1, padx=10, pady=5,sticky="news")

    # สร้าง Label และ Entry สำหรับกรอกอีเมล
    email_label = Label(f, text="Email:")
    email_label.grid(row=1, column=0, padx=10, pady=5,sticky='w')

    email_entry = Entry(f)
    email_entry.grid(row=1, column=1, padx=10, pady=5,sticky="news")

    phone_no_label = Label(f, text="Phone Number:")
    phone_no_label.grid(row=2, column=0, padx=10, pady=5 ,sticky='w')

    phone_no_entry = Entry(f)
    phone_no_entry.grid(row=2, column=1, padx=10, pady=5,sticky="news")

    birthday_label = Label(f, text="Birthday:")
    birthday_label.grid(row=3, column=0, padx=10, pady=5)

    birthday = ttk.DateEntry(f, bootstyle="danger", startdate=date.today())
    birthday.grid(row=3, column=1, padx=10, pady=5,sticky="news")

    password_label = Label(f, text="Password:")
    password_label.grid(row=4, column=0, padx=10, pady=5,sticky='w')

    password_entry = Entry(f)
    password_entry.grid(row=4, column=1, padx=10, pady=5,sticky="news")


    # สร้างปุ่ม "Become a Member"
    become_member_button = Button(f, text="Become a Member", command=become_member)
    become_member_button.grid(row=5, columnspan=2, padx=10, pady=5)
    result_label = ttk.Label(f, text="")
    result_label.grid(row=6, columnspan=2)
    
    home_button = ttk.Button(root, text="Home", command=home_page,width=10,padding=10)
    home_button.grid(row=0,column=0)
   
        
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()
        
def home_member_page():
    width_botton = 56
    c=0
    pading_button=13
    style = Style(theme='minty')
    style.configure("TButton",foreground="black")
    
    
    label = tk.Label(root, image=bg_pic)
    label.place(relheight=1, relwidth=1)
    
    home_button = ttk.Button(root, text="Home", command=home_member_page,width=width_botton,padding=pading_button)
    home_button.grid(row=0,column=c)
    
    service_button = ttk.Button(root, text="Service", command=service_member,width=width_botton,padding=pading_button)
    service_button.grid(row=0,column=c+1)
    
    login_button = ttk.Button(root, text="info", command=mem_info,width=width_botton,padding=pading_button)
    login_button.grid(row=0,column=c+2)
    
    register_button = ttk.Button(root, text="Log out", command=log_out,width=width_botton,padding=pading_button)
    register_button.grid(row=0,column=c+3)
    
    print(f"Member :{user_id_V}")
    


    
def home_page():
    
    clear_window(root)
    style = Style(theme='flatly')
    
    width_botton = 56
    c=0
    pading_button=13
    
    label = tk.Label(root, image=bg_pic)
    label.place(relheight=1, relwidth=1)
    
    home_button = ttk.Button(root, text="Home", command=home_page,width=width_botton,padding=pading_button,style=PRIMARY)
    home_button.grid(row=0,column=c)
    
    service_button = ttk.Button(root, text="Service", command=service,width=width_botton,padding=pading_button,style=PRIMARY)
    service_button.grid(row=0,column=c+1)
    
    login_button = ttk.Button(root, text="Log in", command=login_page,width=width_botton,padding=pading_button,style=PRIMARY)
    login_button.grid(row=0,column=c+2)
    
    register_button = ttk.Button(root, text="Register", command=subscription_page,width=width_botton,padding=pading_button,style=PRIMARY)
    register_button.grid(row=0,column=c+3)
    
    print(f"Home :{user_id_V}")
    """
    #tab
    
    notebook = ttk.Notebook(root,height=1080,width=1920)
    # First tab
    home = ttk.Frame(notebook)
    notebook.add(home, text=' Home ')

    # Second tab
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text='Tab 2')

    # Third tab
    login = ttk.Frame(notebook)
    notebook.add(login, text='Login')
    
    become = ttk.Frame(notebook)
    notebook.add(become, text='Register')

    # Bind the event to switch tabs
    notebook.bind("<<NotebookTabChanged>>", switch_tab)

    # Add some content to the tabs (optional)
    home_label=ttk.Label(home, text="This is Home")
    home_label.grid(row=0,column=0,padx=10, pady=10)

    ttk.Label(tab2, text="This is Tab 2").grid(row=0,column=0,padx=10, pady=10)

    notebook.grid(row=0, column=0, sticky="nsew")
    label = tk.Label(home, image=bg_pic)
    label.place(relheight=1, relwidth=1)
    
    my_button = ttk.Button(home,text="Get Date", bootstyle="danger, outline")
    my_button.place(x=100,y=100)
    """
def service():
    pass

def service_member():
    pass

def mem_info():
    pass

def switch_tab(event):
    tab = event.widget.select()
    tab_text = event.widget.tab(tab, "text")
    print(f"Switched to {tab_text} tab")
    if tab_text == "Login":
        login_page()
    elif tab_text == "Register" :
        subscription_page()
    
    
#login_page()
#home_page()
home_member_page()
root.mainloop()