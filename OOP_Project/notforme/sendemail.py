import smtplib, os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# def send_email(reciever, booking_id):

#     file_name = str(booking_id)+".pdf"
#     file_path = os.getcwd() + "\\booking\\"+str(booking_id)+".pdf"

#     attachment = open(file_path, "rb")
#     p = MIMEBase('application', 'octet-stream')
#     p.set_payload((attachment).read())
#     encoders.encode_base64(p)
#     p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

#     sender_email = 'dkubwaterpark@gmail.com'
#     sender_password = 'jjqckufjkkbchyjs'
#     subject = "Test with attachment"
#     body = "Your booking"
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = reciever
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))

#     msg.attach(p) 
#     server = smtplib.SMTP('smtp.gmail.com:587')
#     server.ehlo()
#     server.starttls()
#     server.login(sender_email, sender_password)
#     text = msg.as_string()
#     server.sendmail(sender_email, reciever, text)
#     server.quit

import smtplib

def send_email(receiver, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        
        sender_email = 'dkubwaterpark@gmail.com'
        sender_password = 'jjqckufjkkbchyjs'
        
        server.login(sender_email, sender_password)
        message = f"Subject : {subject}\n\n{msg}"
        server.sendmail(sender_email, receiver, message)
        server.quit()
        print('Success: Email sent')
    except:
        print('Email failed to send.')
        
subject = 'Link Attachment'
body = "Dear Manatsavin \
\n\nThank you for your purchasing to DKUB Water Park through our official website. \
Your payment has been processed and you can find your tickets attached to this email in PDF format. \
Bring a printout of your tickets or show your mobile device at our entrance and \
you will receive wristbands for entry to our park."
send_email('66010660@kmitl.ac.th', subject, body)

# if __name__ == '__main__':
#     send_email("66010660@kmitl.ac.th", "230032131")