import random
import pandas as pd
import datetime as dt
import smtplib

user_name = 'xyy@gmail.com'
password = 'asdfghjkl' ## App password from mail

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv('birthdays.csv')
birth_day = {(row.month, row.day):row for index, row in data.iterrows()}

if today in birth_day:
    birthday_person = birth_day[today]
    file = f'letter_templates//letter_{random.randint(1,3)}.txt'
    with open(file) as files:
        content = files.read()
        content = content.replace("[NAME]", birthday_person['name'])
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=user_name, password=password)
        connection.sendmail(from_addr=user_name, to_addrs=birthday_person['email'], msg=f'Subject: Happy Birth day\n\n {content}')
