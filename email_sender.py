import smtplib
import ssl
from email.message import EmailMessage
import os

def send_mail():
    # Email credentials and settings
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "shripad.sdabir135@gmail.com"
    receiver_email = "shripad0304@gmail.com"
    password = "zzsonmmgredaufwy"

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Monthly Financial Report - May 2025'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content('Please find the monthly report attached.')

    # Attach the PDF file
    pdf_path = "monthly_report.pdf"
    with open(pdf_path, 'rb') as f:
        pdf_data = f.read()
        msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename='monthly_report.pdf')

    # Send the email
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        os.remove(r'monthly_report.pdf')

    print("Email with PDF sent successfully!")
