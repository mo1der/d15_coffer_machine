import requests
from pprint import pprint

TEQUILA_API_KEY = "Y-4VT61YByhX-bkRZgXpjItbbA7GLFaP"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
HEADERS = {"apikey": TEQUILA_API_KEY}


class DataChecker:
    def __init__(self):
        self.checked_city = ""
        self.city_code = ""

    def location_code_search(self, checked_city):
        self.checked_city = checked_city
        question_data = {
            "term": f"{self.checked_city}",
            "locale": "pl-PL",
            "location_types": "airport",
            "limit": 1}
        response = requests.get(url=TEQUILA_ENDPOINT, params=question_data, headers=HEADERS)
        response.raise_for_status()
        self.city_code = response.json()['locations'][0]['code']
        return self.city_code



# The next step is to search for the flight prices from London (LON) to all the destinations i
# n the Google Sheet. In this project, we're looking only for direct flights, that leave anytime
# between tomorrow and in 6 months (6x30days) time. We're also looking for round trips that
# return between 7 and 28 days in length. The currency of the price we get back should be in GBP.


