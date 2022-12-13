import datetime as dt
import random
import smtplib

with open("quotes.txt", mode="r") as file:
    # quotes = [line for line in file]
    quotes = file.readlines()

now = dt.datetime.now()
day_of_the_week = now.weekday()
day_of_the_week_name = now.strftime("%A")

random_quote = random.choice(quotes)
print(quotes)
my_email = "marcin.betlej@gmail.com"
password = "ygqnzuyacfxcfkoe"

if day_of_the_week == 1:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mo1der@hotmail.com",
            msg=f"Subject: Quote of the day\n\n"
                f"{random_quote}")

