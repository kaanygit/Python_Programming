from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL="####@gmail.com"
MY_PASSWORD="####"
today=datetime.now()
today_tuple=(today.month,today.day)

print(today_tuple)

data=pandas.read_csv("birthdays.csv")

birthdays_dict={(data_row["month"],data_row["day"]):data_row for(index,data_row) in data.iterrows()}

if(today_tuple in birthdays_dict):
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contens=letter_file.read()
        contens=contens.replace("[NAME]",birthday_person["name"])
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
            connection.ehlo()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday! \n\n {contens}") 
            print(f"Send birtday mail to {birthday_person["name"]}")
    except:
        print("Email could be not send!!")