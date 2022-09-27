import smtplib

my_email = "mord2672@gmail.com"
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()
     connection.login(user=my_email, password=password)
     connection.sendmail(
         from_addr=my_email,
         to_addrs="mord2672@yahoo.com",
         msg="Subject:Hello\n\nThis is the body"
     )

import datetime as dt
import random
now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()
     connection.login(user=my_email, password=password)
     connection.sendmail(
         from_addr=my_email,
         to_addrs="mord2672@yahoo.com",
         msg=f"Subject:Motivational quote\n\n{random.choice(quotes)}"
     )
