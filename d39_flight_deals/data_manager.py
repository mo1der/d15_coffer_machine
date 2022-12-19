import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(SHEETY_PRICES_ENDPOINT)
        sheet_response.raise_for_status()
        self.destination_data = sheet_response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": "TESTy"}}#city["iataCode"]}}
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)








# GOOGLE_SHEET_NAME = "mo1der_flight_deals"
# GOOGLE_SHEET_NAME = "prices"


# Sheety API Call & Authentication

# city = "Rzeszow"
# iata_code = "RZE"
# lowest_price = 100

# sheet_inputs = {
#     "price": {
#         "city": "test",
#         "iataCode": "test",
#         "lowestPrice": 100
#     }
# }
# # POST DATA
# sheet_response = requests.post("https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerFlightDeals/prices", sheet_inputs)
# # sheet_response.raise_for_status()
# # data = sheet_response.json()
# print(sheet_response.text)

# # GET DATA


# GET DATA
# sheet_response = requests.get("https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerFlightDeals/prices")
# sheet_response.raise_for_status()
# data = sheet_response.json()
# print(data)


# mo1der_flight_deals
# get
# https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerFlightDeals/prices
#
# post
# https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerFlightDeals/prices
#
# put
# https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerFlightDeals/prices/[Object ID]
