import requests
from twilio.rest import Client


account_sid = "yours"
auth_token = "your tokken"


parameters = {
    "lat": 16.984011,
    "lon": 81.783508,
    "cnt": 4,

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=16.984011&lon=81.783508&appid=231bc0bf"
                            "a5ba4dc254231407052da210", params=parameters)
# response = requests.get(end_point, params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for hour_data in weather_data["list"]:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain ra mawa. So remember to bring ☂️. Umbrella important bigilu.",
        from_="+14322203181",
        to="your number",
    )
    print(message.status)

