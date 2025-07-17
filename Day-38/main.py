import datetime
import os
import requests
host_domain = '	https://trackapi.nutritionix.com'
end_point= 'v2/natural/exercise'
api = os.environ.get('api')

headers = {
    'Content-Type': 'application/json',
    'x-app-id': 'cf9dd9d9',
    'x-app-key': api
}
params = {
    'query' : str(input('enter your exercise'))
}
response = requests.post(url=f'{host_domain}/{end_point}', json=params, headers=headers)
print(response.json())
res = response.json()

Exercise = str(res['exercises'][0]['user_input']).title()
Duration = res['exercises'][0]['duration_min']
Calories = res['exercises'][0]['nf_calories']
Date = datetime.datetime.now().strftime('%d/%m/%Y')
time = datetime.datetime.now().strftime('%H:%M:%S')
print(Exercise,Duration,Calories,Date,time)

sheety_api = os.environ.get('sheety_api')
sheety_url = f'https://api.sheety.co/{sheety_api}/workoutTracking/workouts'
body = {
    'workout':{
        'date':Date,
        'time':time,
        'exercise':Exercise,
        'duration':Duration,
        'calories':Calories
    }
}
response = requests.post(url=sheety_url, json=body)
print(response.json())