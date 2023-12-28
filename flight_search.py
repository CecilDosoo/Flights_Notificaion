import requests
from flight_data import FlightData

api_key = "q_dwF0dZDAAyyZdtORuZzjQplYdoxWDy"
api_endpoint = "https://tequila-api.kiwi.com/locations/query"
API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:

    def __init__(self):
        pass

    def get_code(self,city_name):
        headers = {"apikey":api_key}
        params = {
            "term": city_name,
        }
        response = requests.get(url=api_endpoint,headers=headers,params=params)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": api_key}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            # "nights_in_dst_from": 7,
            # "nights_in_dst_to": 28,
            "flight_type": "oneway",
            "one_for_city": 1,
            "max_stopovers": 3,
            "curr": "QAR"
        }

        response = requests.get(
            url=API_ENDPOINT,
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
