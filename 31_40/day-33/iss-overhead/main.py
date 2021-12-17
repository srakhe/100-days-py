import requests
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

my_pos_lat = 40.7
my_pos_long = 74.0


def iss_pos_in_my_proximity():
    if abs(iss_latitude - my_pos_lat) <= 5 and abs(iss_longitude - my_pos_long) <= 5:
        return True
    else:
        return False


def is_dark():
    if sunset <= time_now.time().hour or time_now.time().hour <= sunrise:
        return True
    else:
        return False


if is_dark() and iss_pos_in_my_proximity():
    print('Look Up for the ISS!')
else:
    print('Won\'t be able to see the ISS')
