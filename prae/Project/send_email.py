import smtplib

def send_email(receiver, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        
        sender_email = '66010853@kmitl.ac.th'
        sender_password = 'Srmxprxe.260305'
        
        server.login(sender_email, sender_password)
        message = f"Subject : {subject}\n\n{msg}"
        server.sendmail(sender_email, receiver, message)
        server.quit()
        print('Success: Email sent')
    except:
        print('Email failed to send.')
        
subject = 'Sent love to Louis from python'
msg = 'Love U naka jubjub >3< muahh'
send_email('66010660@kmitl.ac.th', subject, msg)