import requests

def getTemperature(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={str(latitude)}&longitude={str(longitude)}&current_weather=true"
    response = requests.get(url, timeout=5)

    if response.ok:
        data = response.json()
        try:
            temperature = data["current_weather"]["temperature"]
            return temperature
        except KeyError:
            return None
    return None