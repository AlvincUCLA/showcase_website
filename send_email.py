import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "alvincUCLA@gmail.com"
    password = "cbml qtkw qzag pbyy"
    receiver = "alvincUCLA@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

