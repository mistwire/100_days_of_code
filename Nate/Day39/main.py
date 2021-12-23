from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
import datetime as dt

flight_search = FlightSearch()
datamgr = DataManager()
sheet_data = datamgr.get_destination_data()

for index, row in enumerate(sheet_data):
    if not row['iataCode']:
        iataCode = flight_search.get_destination_code(row['city'])
        datamgr.destination_data[index]['iataCode'] = iataCode

datamgr.update_destination_codes()

today = dt.datetime.today()
depart_start = (today + dt.timedelta(days=1))
depart_end = (today + dt.timedelta(days=181))
return_start = depart_start + dt.timedelta(days=8)
return_end = depart_end + dt.timedelta(days=29)

# formatting and turning into str
fmt_depart_start = depart_start.strftime("%d/%m/%Y")
fmt_depart_end = depart_end.strftime("%d/%m/%Y")
fmt_return_start = return_start.strftime("%d/%m/%Y")
fmt_return_end = return_end.strftime("%d/%m/%Y")

best_flight = {
    "price": "",
    "depart": "",
    "return": ""
}
best_price = 0

# ['data'][0]['price']
for row in sheet_data:
    sheet_price = row['lowestPrice']
    flight_data = FlightData('BOS', row['iataCode'], fmt_depart_start, fmt_depart_end, fmt_return_start, fmt_return_end)
    flight_options = flight_search.search_flight(flight_data)
    best_price = flight_options['data'][0]['price']
    for flight in flight_options['data']:
        if flight['price'] < best_price:
            best_price = flight['price']
            best_flight = {
                "price": best_price,
                "depart": flight['route'][0]['local_departure'],
                "return": flight['route'][1]['local_departure']
            }
            print("test")

    print(f"Best flight to {row['city']}: ${best_price} - {best_flight}")
