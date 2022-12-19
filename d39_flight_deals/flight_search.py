import requests
TEQUILA_API_KEY = "Y-4VT61YByhX-bkRZgXpjItbbA7GLFaP"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

headers = {"apikey": TEQUILA_API_KEY}
city = "Warsaw"
# question_data = {
#     "term": "New York",
#     "locale": "pl-PL",
#     "location_types": "airport",
#     "limit": 10}


question_data = {"term": "Rzeszow",
                 "location_types": "airport",
                 "limit": 10}


# class FlightSearch:
#     def get_destination_code(self, city_name):
#         response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query}", json=question_data, headers=headers)
#         print(response.text)
#         code = "TESTING"
#         return code

response = requests.get(url=TEQUILA_ENDPOINT, params=question_data, headers=headers)

# response = requests.get(url="https://api.tequila.kiwi.com/locations/query?term=New%20York&locale=pl-PL&location_types=airport&limit=10&active_only=true", headers=headers)
print(response.text)

#
# request_params = {"partner": TEQUILA_API_KEY,
#                   "partner_market": "pl",
#                   "fly_from": "FRA",
#                   "fly_to": "LON"
#                   }
#
# sheet_response = requests.get(TEQUILA_ENDPOINT, request_params)
# sheet_response.raise_for_status()
# data = sheet_response.json()
# print(sheet_response.text)
# print(data)
