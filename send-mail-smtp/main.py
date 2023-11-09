

# import smtplib
#### WAY-1
# my_email="######@gmail.com"
# my_password="#####"
# to_email_adress="="######@@gmail.com"


# try:
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
#         connection.ehlo()
#         connection.login(my_email,my_password)
#         connection.sendmail(from_addr=my_email,to_addrs=to_email_adress,msg="Subject:Hello\n\n This is the body of the email")
#         print(f"Email send to {to_email_adress}")
# except:
#     print("Email do not send !!")

##### WAY-2
# import smtplib
# gmail_user = '####@gmail.com'
# gmail_password = '######'

# sent_from = gmail_user
# to = ['#####@gmail.com', '#####@gmail.com']
# subject = 'OMG Super Important Message'
# body = 'Hey, what\'s up?\n\n- You'

# email_text = """\
# From: %s
# To: %s
# Subject: %s

# %s
# """ % (sent_from, ", ".join(to), subject, body)

# try:
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server.ehlo()
#     server.login(gmail_user, gmail_password)
#     server.sendmail(sent_from, to, email_text)
#     server.close()

#     print ('Email sent!')
# except:
#     print ('Something went wrong...')



### EXAMPLE


import smtplib
import datetime as dt
import random

MY_EMAIL="####@gmail.com"
MY_PASSWORD="#####"
TO_EMAIL_ADRESS="####@gmail.com"

now=dt.datetime.now()
weekday=now.weekday()
if weekday==3:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)
    print(quote)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
            connection.ehlo()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=TO_EMAIL_ADRESS,msg=f"Subject:Monday Motivation \n\n {quote}")
            print(f"Email send to {TO_EMAIL_ADRESS}")
    except:
        print("Email could not be sent ")