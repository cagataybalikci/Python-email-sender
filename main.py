import smtplib


# CHANGE my_mail with you email
my_mail = ""
# CHANGE password with you email
password = ""

gmail = "smtp.gmail.com"
"""
1- Make sure you've got the correct smtp address for your email provider:
     
    Gmail: smtp.gmail.com
    
    Hotmail: smtp.live.com
    
    Outlook: outlook.office365.com
    
    Yahoo: smtp.mail.yahoo.com
    
"""

subject = input("Subject Of E-mail: ")
body_of_mail = input("Message: ")

# to_addrs=my_mail change with the mail adress that you want to send email.

with smtplib.SMTP(gmail, port=587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs=my_mail,
        msg=f"Subject:{subject}\n\n{body_of_mail}"
    )

# Below are steps specific to users sending email from Gmail addresses.
"""
    2. Make sure you've enabled less secure apps if you are sending from a Gmail account. (Refer to the video in the next lesson for steps).
    
    3. Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
    
    4. Add a port number by changing your code to this:
    
    smtplib.SMTP("smtp.gmail.com", port=587)
"""