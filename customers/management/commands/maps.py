import requests
from prettyconf import config

API_KEY = config("API_KEY")

def google_map_request(location, api_key):
    """
    Builds the URL to be queried on google platform,
    using two params: location and the API_KEY and
    returns a json response from the request.

    :param str location: the name of the city
    :param str api_key: the api key that is registered on google
    """

    URL = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={API_KEY}'
    return requests.get(URL).json()


def get_coords(response):
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


if __name__ == '__main__':
    coord = get_coords(google_map_request('Warner, NH', API_KEY))
    print(type(coord))
    print(coord)


