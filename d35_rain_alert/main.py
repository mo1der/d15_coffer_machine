# import requests
# from data import weather_data
# # OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
# # api_key = "69f04e4613056b159c2761a9d9e664d2"
# # MY_LAT = 50.041187
# # MY_LONG = 21.999121
# # weather_params = {"lat": MY_LAT,
# #                   "lon": MY_LONG,
# #                   "lang": "pl",
# #                   "units": "metric",
# #                   "appid": api_key,
# #                   "part": "daily"}
# #
# # response = requests.get(OWN_Endpoint, params=weather_params)
# # response.raise_for_status()
# # print(response.status_code)
#
# data = weather_data
# # print(data["hourly"][0])
#
# #
# # import datetime as dt
# # now = dt.datetime.now() #current day/time
# # hour = now.hour  #also we have: month day hour minute microsec sec, weekday/dzień tygodnia
# #
# # print(hour)
#
# weather_slice = data["hourly"][:12]
#
# # sky_status = [(weather_slice[hour]["weather"][0]["description"] for hour in range (len(weather_slice))]
# # print(sky_status)
#
# for hour in range(len(weather_slice)):
#     print(weather_slice[hour]["weather"][0]["description"])
#
# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
#
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC157dea973ca8013c9620994a0fcbd646"
auth_token = "af4d9fa1a876bb0002a38c1bd8335c48"
client = Client(account_sid, auth_token)

import datetime as dt
now = dt.datetime.now() #current day/time
minute = now.minute #also we have: month day hour minute microsec sec, weekday/dzień tygodnia


if minute == 15:
    message = client.messages.create(
      body="Hello from Mo1der!!!",
      from_="+13868543985",
      to="+48500076517"
    )

    print(message.sid)
#
#




