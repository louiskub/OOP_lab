from datetime import datetime

def count_days():
    # วันเริ่มต้น
    start_date = input("ป้อนวันที่เริ่มต้น (รูปแบบ: dd-mm-yyyy): ")
    end_date = input("ป้อนวันที่สิ้นสุด (รูปแบบ: dd-mm-yyyy): ")

    # แปลงวันที่เป็นรูปแบบของ datetime
    start_date = datetime.strptime(start_date, '%d-%m-%Y')
    end_date = datetime.strptime(end_date, '%d-%m-%Y')

    # คำนวณจำนวนวัน
    delta = end_date - start_date
    print("จำนวนวันที่ระหว่างวันที่เริ่มต้นกับวันที่สิ้นสุดคือ:", delta.days, "วัน")

count_days()