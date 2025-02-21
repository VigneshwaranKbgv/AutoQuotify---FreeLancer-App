import requests

def get_location_adjustment(location):
    """
    Uses the Nominatim API to geocode the location string.
    If the returned address includes a 'city' or 'town', returns 1.2,
    otherwise returns 1.0.
    """
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location,
        "format": "json",
        "addressdetails": 1,
        "limit": 1
    }
    headers = {"User-Agent": "AutoQuotifyApp"}  # Required by Nominatim
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            address = data[0].get("address", {})
            if "city" in address or "town" in address:
                return 1.2
    return 1.0
