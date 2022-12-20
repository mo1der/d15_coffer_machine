import requests
from pprint import pprint
import datetime

time_now = datetime.datetime.now()
print(time_now.date())

date_shift = time_now + datetime.timedelta(days=3)
print(date_shift.date())


TEQUILA_API_KEY = "Y-4VT61YByhX-bkRZgXpjItbbA7GLFaP"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
headers = {"apikey": TEQUILA_API_KEY}

question_data = {
    "fly_from": "RZE",
    "fly_to": "LON",
    "date_from": "19/12/2022",
    "date_to": "31/12/2022",
    "curr": "PLN",
    "sort": "price",
    "limit": 1}
response = requests.get(url=TEQUILA_ENDPOINT, params=question_data, headers=headers)
response.raise_for_status()
flight_data = response.json()['data'][0]['price']
pprint(flight_data)


# The next step is to search for the flight prices from London (LON) to all the destinations i
# n the Google Sheet. In this project, we're looking only for direct flights, that leave anytime
# between tomorrow and in 6 months (6x30days) time. We're also looking for round trips that
# return between 7 and 28 days in length. The currency of the price we get back should be in GBP.


def zmianne:
# to jest opis zmiennej
    print("cos")


zmianne()