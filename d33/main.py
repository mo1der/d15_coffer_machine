# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json") #zmienna = odpowiedź na zapytanie
# response.raise_for_status()
# # if response.status_code != 200:
# #     raise Exception("Bad response from ISS API")
#
# data = response.json()  #wyciągnięcie wszytkiego do postaci słownika
# # print(data["iss_position"])
#
# # data = response.json()["iss_position"]   #wyciągnięcie specyficznej informacji
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
#

# from tkinter import *
# import requests
#
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest/")
#     response.raise_for_status()
#     if response.status_code != 200:
#         raise Exception("Bad response from ISS API")
#
#
#     data = response.json()["quote"]
#     canvas.itemconfig(quote_text, text=data)
#     # print(data)
#     #Write your code here.
#
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()
#
# import requests
# from datetime import datetime
#
# # response = requests.get(url="https://api.sunrise-sunset.org/json?lat=50.041187&lng=21.999121&date=today")
# # lub
#
# MY_LAT = 50.041187
# MY_LONG = 21.999121
# parameters = {"lat": MY_LAT,
#               "lng": MY_LONG,
#               "formatted": 0}
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
#
# response.raise_for_status()
# if response.status_code != 200:
#     raise Exception("Bad response from API")
# data = response.json()["results"]["sunrise"]
# print(data)
#
# sunset_hour = data.split("T")
# print(sunset_hour)
#
# sunset_hour2 = sunset_hour[1]
# print(sunset_hour2)
#
# sunset_hour3 = sunset_hour2[0:5]
#
# sunset_hour4 = sunset_hour3.split(":")
# print(sunset_hour4)
#
#
#
# from datetime import datetime
# time_now = datetime.now()
# print(time_now)
#





#Your position is within +5 or -5 degrees of the ISS position.



#If the ISS is close to my current position
from datetime import datetime
import requests

MY_LAT = 50.041187
MY_LONG = 21.999121

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    else:
        return False


def check_darkness():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if sunrise <= time_now.hour or time_now.hour >= sunset:
        return True
    else:
        return False

print(check())
print(check_darkness())

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




