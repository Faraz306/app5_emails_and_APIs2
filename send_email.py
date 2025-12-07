import smtplib
import ssl

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    user_name = "private.1984@gmail.com"
    password = "epqz yybg vofe lrsp"
    receiver = "private.1984@gmail.com"

    context = ssl.create_default_context()

    msg = f"Subject: News Update\n\n{message}".encode("utf-8")

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, msg)

# Example usage
body = "Latest Tesla news:\n— Tesla announces new factory in Asia\n— Model Y becomes best-selling car globally"
send_email(body)