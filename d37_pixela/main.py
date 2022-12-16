import requests
import datetime as dt

USERNAME = "mo1der"
TOKEN = "das8fds8f3jrfdsh7"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {"token": "das8fds8f3jrfdsh7",
               "username": "mo1der",
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# https://pixe.la/@mo1der



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {"id": "graph17",
               "name": "Cycling Graph",
               "unit": "Km",
               "type": "float",
               "color": "ajisai"}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint , json=graph_config, headers=headers)
# print(response.text)

# https://pixe.la/v1/users/mo1der/graphs/graph17.html

graph17_endpoint = "https://pixe.la/v1/users/mo1der/graphs/graph17"


today = dt.datetime.now()
data_str = today.strftime("%Y%m%d")

point_params = {"date": f"{data_str}",
                "quantity": "100"}
#
# response = requests.post(url=graph17_endpoint , json=point_params, headers=headers)
# print(response.text)
#
#
# point_update_params = {"quantity": "150"}
#
# response = requests.put(url=f"{graph17_endpoint}/{data_str}", json=point_update_params, headers=headers)
# print(response.text)


response = requests.delete(url=f"{graph17_endpoint}/{data_str}", headers=headers)
print(response.text)