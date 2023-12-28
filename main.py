import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import datetime as dt
from notification_manager import NotificationManager


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()

ORIGIN_CITY_IATA = "DOH"

API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "q_dwF0dZDAAyyZdtORuZzjQplYdoxWDy"

now = dt.datetime.now()
tomorrow = now + dt.timedelta(days = 1)
six_months = now + dt.timedelta(days = 2*30)


for row in sheet_data:
    row["iataCode"] = flight_search.get_code(row["city"])
    data_manager.destination_data = sheet_data
    

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months)
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}"
                    f"-{flight.origin_airport} to {flight.destination_city}"
                    f"-{flight.destination_airport}, from {flight.out_date} "
                    f"to {flight.return_date}.")
