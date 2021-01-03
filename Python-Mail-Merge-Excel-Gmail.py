import pandas as pd
import xlrd
import smtplib

e = pd.read_excel("put your excel file name here", engine='openpyxl')
    # example Excel file name: "EmailAddressList.xlsx"
emails = e['Emails'].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("put your email address here", "put your password here")

msg = "put your email message here"
subject = "put your email subject line here"
body = "Subject: {}\n\n{}".format(subject, msg)

for email in emails:
    
    server.sendmail("put your Gmail email address here", email, body)
    
server.quit()
