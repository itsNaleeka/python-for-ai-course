import requests

def get_weather_data(lat, lon):
    # Build the API URL with our parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"

    response = requests.get(url)
    data = response.json()
    print(data["current"]["temperature_2m"] , '°C')

kandy = get_weather_data(lat=7.290572, lon=80.633728)
pera_gym = get_weather_data(lat=7.256659545077611, lon=80.59498742280428)