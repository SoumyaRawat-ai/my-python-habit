import time

import requests
from datetime import datetime
import smtplib
my_lat = 29.852970
my_lng = 77.875450

def iss_position():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()

    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    if my_lng-5<= longitude <= my_lng+5 and my_lat-5 <= latitude <= my_lng+5:
        return True

def night_time():
    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour
    if sunset <= time_now <= sunrise :
        return True
my_user = 'vidvide766@gmail.com'
password = 'hrmapppbygiytlmx'

while True:
    time.sleep(60)
    if iss_position() and night_time():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_user, password=password)
            connection.sendmail(from_addr=my_user, to_addrs='soumyarawat0305@gmail.com', msg='Subject:Internation Space station is around you\n\n Vist out side in sky Internation space station is around you')