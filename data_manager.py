import requests

sheety_endpoint = "https://api.sheety.co/1fc853c5dae57a1046b04eeac781d27c/flightDeals/prices"


class DataManager():

    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def code_update(self):
        for city in self.destination_data:
            params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=params)
            print(response.text)


