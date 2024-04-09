import smtplib
import ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "abcd@example.com"
    password = "<app password>"
    receiver = "xyz@example.com"
    context = ssl.create_default_context()
    # message = "Hello"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


# send_mail("message")
