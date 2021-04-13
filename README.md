# Python-email-sender
 
You can send email with this python file. 

Steps:

* CHANGE my_mail with your email

* CHANGE password with your password

* CHANGE gmail with your email services -> gmail = "smtp.gmail.com" with services code below

* Make sure you've got the correct smtp address for your email provider:
```    
 Gmail: smtp.gmail.com
    
 Hotmail: smtp.live.com
    
 Outlook: outlook.office365.com
    
 Yahoo: smtp.mail.yahoo.com

```
* CHANGE to_addrs with the e-mail address, you want to send email.

* For Gmail you need to do this extra steps 
````
Make sure you've enabled less secure apps if you are sending from a Gmail account. Google Account Settings > Security > Less Secure Apps > On

Also you need to enable Two-factor auth and sms auth > Off 
    
Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
    
Add a port number by changing your code to this:
    
smtplib.SMTP("smtp.gmail.com", port=587)
```
