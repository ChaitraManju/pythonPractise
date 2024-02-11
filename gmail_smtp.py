import smtplib


def sendmail():
    port = 465  # For SSL
    username = "pythonpractise11feb2024@gmail.com"
    sender = "pythonpractise"
    password = input("Enter the app password: ")
    context_msg = "Alert! : Links are down"

    header = 'To:' + username + '\n' + 'From:' \
             + sender + '\n' + 'subject:Alert! : Link is down\n'
    msg = context_msg+header

    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.starttls()
    mail_server.login(username, password)
    mail_server.sendmail("smtp.gmail.com", username, msg)
    mail_server.close()
