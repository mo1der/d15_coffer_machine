import csv
import math
import pandas as pd
from main2 import DataChecker

datachecker = DataChecker()

flight_data = pd.read_csv('flight_data.csv', sep=';')

# arkusz=pd.DataFrame(flight_data)

# flight_data = {row.letter:row.code for (index, row) in nato_data.iterrows()}
#
print(flight_data)

for id in range(len(flight_data)):
    city = flight_data["City"].iloc[id]
    iata_code = datachecker.location_code_search(city)
    flight_data["IATA Code"].iloc[id] = iata_code


flight_data.to_csv('flight_data.csv', sep=';', index=False)