import requests
from datetime import datetime
import smtplib

MY_LAT = 55.711311 # Your latitude
MY_LONG = 9.536354 # Your longitude
MY_EMAIL = ""
PASSWORD = ""
EMAIL = ""


def proximity_check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if int(MY_LAT) in range(int(iss_latitude - 5), int(iss_latitude + 5)) and int(MY_LONG) in range(int(iss_longitude - 5), int(iss_longitude + 5)):
        return True
    else:
        return False


def sun_check():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    my_time = time_now.hour
    dark_hours = 24 - sunset + sunrise
    dark = [sunset + hour if sunset + hour <= 24 else sunset + hour - 24 for hour in range(dark_hours + 1)]
    if my_time in dark:
        return True
    else:
        return False


if proximity_check() and sun_check():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: ISS is close!!!!\n\nISS IS CLOSE"
        )

