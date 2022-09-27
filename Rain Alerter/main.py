import requests
from twilio.rest import Client
import datetime as dt

api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC53ec064be5648bd7f999240577aede51"
auth_token = "ff2b126422fd7a2fcba54f78c30997ea"

parameters = {
    "lat": 55.676098,
    "lon": 12.568337,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

now = dt.datetime.now()
day = now.weekday()

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
rain_day = []
hour = 0

for hour_data in range(0, 13):
    condition_code = weather_data["hourly"][hour_data]["weather"][0]["id"]
    if int(condition_code) < 700 and 0 <= day < 5:
        time_of_rain = 8 + hour_data
        rain_day.append(str(time_of_rain) + ":00")
        will_rain = True


if will_rain:
      client = Client(account_sid, auth_token)
      message = client.messages \
          .create(
          body=f'Hej skat! Det kommer til at regne 🌧️ omkring klokken {", ".join(rain_day)} i dag. Husk din paraply! Jeg elsker dig! ❤️',
          from_='$SENDER',
          to='$RECEIVER'
      )
      print(message.status)



