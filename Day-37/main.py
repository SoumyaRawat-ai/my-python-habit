import requests
from datetime import datetime
pixela_endpoint = 'https://pixe.la/v1/users'
username = 'soumyarawat03'
token = '34567890'
id = '234567890'

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService" : 'yes',
    "notMinor" : 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"


graph_config = {
    "id": 'yy4567890-',
    "name": 'Coding Graph',
    "unit": "hr",
    "type": "int",
    "color": 'sora',
}

headers = {
    "X-USER-TOKEN" : token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers = headers)
# print(response.text)
today = datetime.now()
today_date = str(datetime.today().strftime('%Y%m%d'))
value_url = f'{pixela_endpoint}/{username}/graphs/{id}'
param = {
    'date' : today.strftime('%Y%m%d'),
    'quantity': str(input('how many hour did you code today: '))
}
head = {
    'X-USER-TOKEN' : token
}

response = requests.post(url=value_url, json=param, headers=head)
print(response.text)
print(today.strftime('%Y%m%d'))


update_url = f"{pixela_endpoint}/{username}/graphs/{id}/{today.strftime('%Y%m%d')}"

params_update = {
    'quantity': '5'
}
heads = {
    'X-USER-TOKEN' : token
}

# response = requests.put(url=update_url, json=params_update, headers=heads)
# print(response.text)
#
# response = requests.delete(url=update_url,headers=head)
# print(response.text)