# Read README.md to config to use this program. Link : https://github.com/cagataybalikci/Python-email-sender/blob/main/README.md
# This is just a program for implementing "sending email". Don't use with real mail adresses if you are not sure
# about this package. If you really want to use it, try it with some dummy email account that you can easily create

import smtplib

my_mail = ""
password = ""
gmail = "smtp.gmail.com"

subject = input("Subject Of E-mail: ")
body_of_mail = input("Message: ")

with smtplib.SMTP(gmail, port=587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs=my_mail,
        msg=f"Subject:{subject}\n\n{body_of_mail}"
    )
