import requests
from prettyconf import config

API_KEY = config("API_KEY")


class Maps:
    def __init__(self):
       self.internal_cache = []

    def google_request(self, location, api_key):
        """
        Builds the URL to be queried on google platform,
        using two params: location and the API_KEY and
        returns a json response from the request.

        :param str location: the name of the city
        :param str api_key: the api key that is registered on google
        """
        print(f'Location to be searched on google: {location}')

        URL = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}'
        return requests.get(URL).json()


    def get_internal_coords(self, response):
        """
        Extracts the latitude and longitude from the response.
        Returns a Dictionary with the Keys: Latitude and Longitude
        :param str response: the json format of the response requested on google_map_request
        """

        latitude = response['results'][0]['geometry']['location']['lat']
        longitude = response['results'][0]['geometry']['location']['lng']
        coordinates = dict({
            'Latitude': latitude,
            'Longitude': longitude
        })
        return coordinates
    
    def get_coords(self, location):
        index = next((i for i, item in enumerate(self.internal_cache) if item["location"] == location), None)
        if index == None:
            req = self.google_request(location, API_KEY)
            coord = self.get_internal_coords(req)
            self.internal_cache.append({"location": location, "coordinate": coord})
            return coord

        dict = next(item for item in self.internal_cache if item["location"] == location)
        coord = dict['coordinate']
        return coord


if __name__ == '__main__':
    maps = Maps()
    coord = maps.get_coords('Warner, NH')
    coord = maps.get_coords('Center, MA')
    coord = maps.get_coords('Warner, NH')
    coord = maps.get_coords('Center, MA',)
    print(type(coord))
    print(coord)


