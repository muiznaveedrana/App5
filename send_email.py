import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "littlecoders10@gmail.com"
    password = "koxb ummm vlck ufgs"  # Consider using environment variables for this

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        with open("email.txt", "r") as file:
            emails = file.readlines()  # Read all lines from the file
            
            for receiver in emails:
                receiver = receiver.strip()  # Remove any surrounding whitespace/newlines
                if receiver:  # Ensure that the line is not empty
                    try:
                        server.sendmail(username, receiver, message)
                        print(f"Email sent to {receiver}")
                    except Exception as e:
                        print(f"Failed to send email to {receiver}: {e}")

