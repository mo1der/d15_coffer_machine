import requests
from pprint import pprint


SHEETY_ENDPOINT = "https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerFlightDeals/prices"
headers = {"Authorization": "Bearer thisissheetiymo1dertoken"}


# READ SHEETY ###########################################################
response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
response.raise_for_status()
sheet_data = response.json()["prices"]
print(pprint(sheet_data))

# ADD TO SHEETY ###########################################################
new_city = "Rzeszow"
new_iatacode = "RZE"
new_lowest_price = 99

data_to_put = {"price":
                    {"city": new_city,
                     "iataCode": new_iatacode,
                     "lowestPrice": new_lowest_price}
}
response = requests.post(url=SHEETY_ENDPOINT, json=data_to_put, headers=headers)
response.raise_for_status()
# print(response.text)

# UPDATE ROW SHEETY ###########################################################

editted_row_id = 2
editted_city = "Rzeszow"
editted_iatacode = "RZE"
editted_lowest_price = 100

data_to_update = {"price":
                    {"lowestPrice": editted_lowest_price}
}

response = requests.put(url=f"{SHEETY_ENDPOINT}/{editted_row_id}", json=data_to_update, headers=headers)
response.raise_for_status()
# print(response.text)

# ##########################################################################################################

for row in sheet_data:
    if row["iataCode"] == "":
        new_code = "TEST"
        data_to_update = {"price":
                              {"iataCode": new_code}}
        response_url = f'{SHEETY_ENDPOINT}/{row["id"]}'
        response = requests.put(url=response_url, json=data_to_update, headers=headers)
    print(row)
