from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus.tables import Table, TableStyle
import os, segno

def create_qrcode(booking_id):
    qrcode = segno.make_qr(str(booking_id))
    qrcode_path = os.getcwd() + "\\booking\\"+str(booking_id)+".png"
    qrcode.save(qrcode_path, 
                scale=6, 
                dark="darkblue",
                quiet_zone="white",
                )
    return qrcode_path

def to_table(orderdetail: list):    
    table_data = [
        ['Order Detail', 'Price', 'Qty', 'SubTotal'],
    ]
    [table_data.append([
        order["Item Name"], order["Price"], order["Qty"], order["Subtotal"]
        ]) 
        for order in orderdetail
    ]
    return table_data

def create_pdf(info: dict):
    distance = 15
    row_height = 19

    customer = info["Customer"]
    booking = info["Booking"]
    order = info["Order"]
    target_path = os.getcwd() + "\\booking"
    if not os.path.exists(target_path):
        print("create booking folder")
        os.makedirs(target_path)
    pdf_path = os.path.join(target_path, str(booking["Booking Id"])+'.pdf')
    qrcode_path = create_qrcode(booking["Booking Id"])
    c = canvas.Canvas(pdf_path, initialFontSize=20, pagesize=A4)
    c.drawImage(qrcode_path, 393, 618)
    c.setFillColor(colors.black)

    c.setFont("Helvetica-Bold", 28)
    c.drawString(50, 795, "DKUB Water Park")   #BookingId
    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, 780,"___________________________________________________")
    c.drawString(460, 795, "E-TICKET")   #BookingId
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, 750, "BOOKING ID")   #BookingId\
    c.drawString(50, 730, "STATUS")   #Payment Status
    c.drawString(160, 750, ":  " + str(booking["Booking Id"]))
    c.drawString(160, 730, ":  " + str(booking["Payment Status"]))


    c.setFont("Helvetica", 12)
    c.drawString(50, 690 + distance, "Name")
    c.drawString(50, 675 + distance, "Emai")
    c.drawString(50, 660 + distance, "Phone Number")
    c.drawString(50, 645 + distance, "Date Of Order")
    c.drawString(50, 630 + distance, "Date Of Visit")
    
    c.drawString(160, 690 + distance, ":  " + str(customer["Name"]))
    c.drawString(160, 675 + distance, ":  " + str(customer["Email"]))
    c.drawString(160, 660 + distance, ":  " + str(customer["Phone Number"]))
    c.drawString(160, 645 + distance, ":  " + str(booking["Date Of Order"]))
    c.drawString(160, 630 + distance, ":  " + str(order["Date Of Visit"]))


    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 590, "Order Detail")

    c.setFont("Helvetica", 13)
    table_detail = to_table(order["Order Detail"])
    table = Table(table_detail, colWidths=[305, 75, 40, 75])
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0),(0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('ALIGN', (3, 0), (3, -1), 'RIGHT'),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)
    table.wrapOn(c, 0, 0)
    table.drawOn(c, 50, 558 - row_height * len(table_detail))

    c.setFont("Helvetica", 16)
    table_detail2 = [["TOTAL : ", "THB "+ str(order["Total"])]]
    table2 = Table(table_detail2, colWidths=[420, 75])
    style2 = TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (0, 0), (-1, 0), 'RIGHT'),
    ])
    table2.setStyle(style2)
    table2.wrapOn(c, 0, 0)
    table2.drawOn(c, 50, 540 - row_height * len(table_detail))

    c.save()
    print(f"PDF saved at: {pdf_path}")

info = {
    "Customer": {
        "Name": "Name",
        "Email": "Email",
        "Phone Number": "0887826930"
    },
    "Booking": {
        "Booking Id": "230032131",
        "Date Of Order": "22/10/2024",
        "Payment Status": "PAID"
    },
    "Order": {
        "Date Of Visit": "22/11/2024",
        "Total" : 1000,
        "Order Detail": [
            {
                "Item Name": "Cabana Zone2 Id9",
                "Price": 100,
                "Qty": 1,
                "Subtotal": 100
            },  
            {
                "Item Name": "Cabana Zone2 Id9",
                "Price": 100,
                "Qty": 1,
                "Subtotal": 100
            },
            {
                "Item Name": "Cabana Zone2 Id9",
                "Price": 100,
                "Qty": 1,
                "Subtotal": 100
            }         
        ]
    }
}
create_pdf(info)