import requests
import config
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
WEATHER_MAP_API = config.weather_map_api_key
ACCOUNT_SID = config.account_sid
AUTH_TOKEN = config.auth_token

parameters = {
    "lat": 19.26,
    "lon": 126.45,
    "appid": WEATHER_MAP_API,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# hourly_data = data["hourly"][0]["weather"][0]["id"]
will_rain = False

for hourly in data["hourly"][:12]:
    weather = hourly["weather"][0]["id"]
    if int(weather) < 700:
        will_rain = True
if will_rain:
    # print("Bring your umbrella")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body = "It's going to rain today. Remember to bring an Umbrella",
        from_="+18773984454",
        to='+16193419392'
    )
    print(message.status)