##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import datetime as dt
import pandas as pd
import random
import smtplib


def send_letter():
    my_email = "marcin.betlej@gmail.com"
    password = "ygqnzuyacfxcfkoe"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person_email,
            msg=f"Subject: {person_age} Birthday wishes\n\n"
                f"{final_letter}")


persons_data = pd.read_csv("birthdays.csv")
birthdays = persons_data.to_dict(orient="records")

letters = []
with open("./letter_templates/letter_1.txt", "r") as text1:
    letters.append(text1.read())
with open("./letter_templates/letter_2.txt", "r") as text2:
    letters.append(text2.read())
with open("./letter_templates/letter_3.txt", "r") as text3:
    letters.append(text3.read())

today = dt.datetime.now()
today_year = today.year
today_month = today.month
today_day = today.day

for person in birthdays:
    if person["month"] == today_month and person["day"] == today_day:
        person_name = person["name"]
        person_email = person["email"]
        person_year = person["year"]
        person_month = person["month"]
        person_day = person["day"]
        person_age = today_year-person_year

        selected_letter = random.choice(letters)
        final_letter = selected_letter.replace("[NAME]", person_name)
        send_letter()
















