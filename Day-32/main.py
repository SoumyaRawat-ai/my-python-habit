import random
import datetime as dt
import smtplib


date = dt.datetime.now()
Weekday = date.weekday()
if Weekday == 1:
    with open('quotes.txt') as file:
        data = file.readlines()
    quote = random.choice(data)
    print(quote)


    my_email = 'vbnjmk6@gmail.com'
    password = 'hbnm,x'

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='ff@gmail.com',
                            msg=f'Subject:Monday quote\n\n{quote}')