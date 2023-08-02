# import smtplib
#
email = "your mail"
pswd = "your app password"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=pswd)
#     connection.sendmail(from_addr=email,
#                         to_addrs="ydubey7979@gmail.com",
#                         msg="Subject:for learning\n\n Hello maam, yashkumar here I'm on day 32 of python 100days of code this id for just testing m automated work email.")

import pandas as pd
import smtplib
import random
import datetime as dt
today = dt.datetime.now()
today_day_month = (today.day, today.month)
print(today_day_month)
data = pd.read_csv("birthdat.csv")
my_dict = {(alldata.day,alldata.month):alldata for (index,alldata) in data.iterrows()}
print(my_dict)
if today_day_month in my_dict:
    birthday_boy = my_dict[today_day_month]
    file_path = "letter_templates/letter_1.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_boy["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=pswd)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_boy["email"],
                            msg=f"Subject:Wish You Happy Birthday!\n\n{contents} ")




