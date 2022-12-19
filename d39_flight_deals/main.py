#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

datamanager = DataManager()
sheet_data = datamanager.get_destination_data()
# print(pprint(sheet_data))

for row in sheet_data:
    if row["iataCode"] == "":
        x = FlightSearch().get_destination_code(row["city"])
        print(x)
        datamanager.destination_data = sheet_data
        datamanager.update_destination_codes()


# if sheet_data[2]["iataCode"] == "":
#     print("OK")

#
# print(pprint(
#     [(x["city"], x["lowestPrice"]) for x in sheet_data if x["lowestPrice"] > 400][:]
# ))


# # > [d['status'] for d in list_of_dicts if d['name']=='Robert']
#
# print(next(x for x in lstdict if x["name"] == "Klaus"))
# print([x for x in sheet_data if x['city'] == 'Paris'][0])
#
#
# print(sheet_data)
#
