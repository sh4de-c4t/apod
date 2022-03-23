import requests


def get_apod_data(date, api_key, hd=True):
    """
    this function help you to request to apod
    parameters = date , api_key , hd(true or false)
    """
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "date": date, "hd": hd}
    response = requests.get(url, params=params)
    return response.json()