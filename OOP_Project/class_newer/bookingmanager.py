from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus.tables import Table, TableStyle
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi.responses import FileResponse
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
import os, segno, smtplib
class FinishBookingManager:
    def __init__(self):
        self.__path_now = os.getcwd()
        self.__file_path = self.__path_now + "\\booking\\"
        self.__logo_path = self.__path_now + "\\DKUB_logo.svg"
        self.__sender_email = 'dkubwaterpark@gmail.com'
        self.__sender_password = 'jjqckufjkkbchyjs'
    
    def create_qrcode(self, booking_id):
        qrcode = segno.make_qr(str(booking_id))
        qrcode_path = self.__file_path + str(booking_id) + ".png"
        qrcode.save(qrcode_path, scale=6)
        return qrcode_path
    def svg_scale(self, drawing, scaling_factor):
        scaling_x = scaling_factor
        scaling_y = scaling_factor
        drawing.width = drawing.minWidth() * scaling_x
        drawing.height = drawing.height * scaling_y
        drawing.scale(scaling_x, scaling_y)
        return drawing
    
    def to_table(self, orderdetail: list):    
        table_data = [
            ['Order Detail', 'Price', 'Qty', 'SubTotal'],   #header
        ]
        [table_data.append([
            order["Item Name"], order["Price"], order["Qty"], order["Subtotal"]
            ]) 
            for order in orderdetail
        ]
        return table_data
    def create_pdf(self, info: dict):
        distance = 15
        row_height = 19
        customer, booking, order = info["Customer"], info["Booking"], info["Order"]

        target_path = self.__file_path
        if not os.path.exists(target_path):
            print("create booking folder")
            os.makedirs(target_path)
        pdf_path = target_path + str(booking["Booking Id"]) + '.pdf'
        qrcode_path = self.create_qrcode(booking["Booking Id"])
        c = canvas.Canvas(pdf_path, initialFontSize=20, pagesize=A4)
        c.drawImage(qrcode_path, 393, 602)

        drawing = svg2rlg(self.__logo_path)        
        scaled_drawing = self.svg_scale(drawing, 0.14)
        renderPDF.draw( scaled_drawing, c, 40, 769 )
        c.setFillColor(colors.black)
        
        #c.setFont("Helvetica-Bold", 28)
        #c.drawString(50, 795, "DKUB Water Park")   #BookingId
        

        c.setFont("Helvetica-Bold", 18)
        c.drawString(40, 770,"___________________________________________________")
        c.drawString(460, 785, "E-TICKET")   #BookingId

        c.setFont("Helvetica-Bold", 13)
        c.drawString(50, 740, "BOOKING ID")   #BookingId\
        c.drawString(50, 720, "STATUS")   #Payment Status
        c.drawString(160, 740, ":  " + str(booking["Booking Id"]))
        c.drawString(160, 720, ":  " + str(booking["Payment Status"]))
        c.setFont("Helvetica", 12)
        c.drawString(50, 680 + distance, "Name")
        c.drawString(50, 665 + distance, "Emai")
        c.drawString(50, 650 + distance, "Phone Number")
        c.drawString(50, 635 + distance, "Date Of Order")
        c.drawString(50, 620 + distance, "Date Of Visit")
        c.drawString(160, 680 + distance, ":  " + str(customer["Name"]))
        c.drawString(160, 665 + distance, ":  " + str(customer["Email"]))
        c.drawString(160, 650 + distance, ":  " + str(customer["Phone Number"]))
        c.drawString(160, 635 + distance, ":  " + str(booking["Date Of Order"]))
        c.drawString(160, 620 + distance, ":  " + str(order["Date Of Visit"]))


        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 590, "Order Detail")

        c.setFont("Helvetica", 13)
        print(order["Order Detail"])
        table_detail = self.to_table(order["Order Detail"])
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
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])
        table.setStyle(style)
        table.wrapOn(c, 0, 0)
        table.drawOn(c, 50, 576 - row_height * len(table_detail))

        c.setFont("Helvetica", 16)
        table_detail2 = [
                        ["DISCOUNT :", "- "+ str(order["Discount"])]
                        ,["TOTAL : ", "THB "+ str(order["Total"])]
                        ]
                        
        table2 = Table(table_detail2, colWidths=[420, 75])
        style2 = TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige)
        ])
        table2.setStyle(style2)
        table2.wrapOn(c, 0, 0)
        table2.drawOn(c, 50, 540 - row_height * len(table_detail))

        c.save()
        print(f"PDF saved at: {pdf_path}")

    def send_email(self, reciever, customer_name, booking_id):
        file_name = str(booking_id)+".pdf"
        file_path = self.__file_path + file_name

        attachment = open(file_path, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

        subject = "Your tickets to DKUB Water Park"
        body = f"{customer_name} \
\n\nThank you for your purchasing to DKUB Water Park through our official website. \
Your payment has been processed and you can find your tickets attached to this email in PDF format. \
Bring a printout of your tickets or show your mobile device at our entrance and \
you will receive wristbands for entry to our park."

        msg = MIMEMultipart()
        msg['From'] = self.__sender_email
        msg['To'] = reciever
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(p) 
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.__sender_email, self.__sender_password)
            text = msg.as_string()
            server.sendmail(self.__sender_email, reciever, text)
            server.quit
            print( "Done")
        except:
            print('Email failed to send.')

    def view_finish_booking(self, booking_id):
        file_name = str(booking_id)+".pdf"
        print(file_name)
        file_path = self.__file_path + file_name
        if not os.path.exists(file_path):
            return "booking not found"
        headers = {
                "Content-Disposition": "inline;"
        } 
        return FileResponse(file_path, media_type="application/pdf", filename=file_name, headers=headers)

if '__main__' == __name__ :
    f = FinishBookingManager()
    info = {
        "Customer": {
            "Name": "Manatsavin Kunnantajiam",
            "Email": "louismnsv@gmail.com",
            "Phone Number": "0887826930"
        },
        "Booking": {
            "Booking Id": "1239879219",
            "Date Of Order": "22/10/2024",
            "Payment Status": "PAID"
        },
        "Order": {
            "Date Of Visit": "22/11/2024",
            "Total" : 800,
            "Discount": 300,
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
    f.create_pdf(info)
    #f.send_email(info["Customer"]["Email"], info["Customer"]["Name"], info["Booking"]["Booking Id"])