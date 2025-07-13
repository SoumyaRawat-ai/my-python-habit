import requests
from twilio.rest import Client

account_sid = "tyuiloghjkl;"
auth_token = "1234567890-"
api_key = "123456789"
parameters = {
    'lat': 29.852970,
    'lon': 77.875450,
    'appid': api_key,
    'cnt' : 4
}
url = 'https://api.openweathermap.org/data/2.5/forecast'
req = requests.get(url=url, params=parameters)
data = req.json()

will_rain = False
for i in data['list']:
    if i['weather'][0]['id'] < 700:
        # print('Bring an umbrella')
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today. Remember to bring an ☔",
        from_="+1456789",
        to="+967890-",
    )
    print(message.status)