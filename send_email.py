import smtplib, ssl
def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "littlecoders10@gmail.com"
    password = "yvmx xqfe nozr vjqx"

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = my_context) as server:
        server.login(username, password)
        with open("email.txt", "r") as file:
            emails = file.read()
            for reciever in emails:
                server.sendmail(username, reciever,message)