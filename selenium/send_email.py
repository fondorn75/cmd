import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sendMail():
    from_addr = 'fondorn@mail.ru'
    to_addr = 'fondorn@mail.ru'
    mypass = 'Sq9tcu6USFEVTZcqmmMc'
    report_name = 'log.txt'

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Report from Python'

    with open(report_name, "rb") as f:
        part = MIMEApplication(f.read(), name=report_name)

    msg.attach(part)
    body = "This test message"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(from_addr, mypass)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

