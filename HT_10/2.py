import requests
import json
from datetime import timedelta, date, datetime



flag = True
while flag == True:
    cur = input('Enter Currence (example: EUR, USD, RUB, GBP, PLN): ')

<<<<<<< HEAD
    now = datetime.now()
    current_datetime = now
=======
    current_datetime = datetime.now()
>>>>>>> 7821665e52f5cb62f85bd5153fbcad3f37da43f7
    date_format = '%d.%m.%Y'
    m = current_datetime.strftime(date_format)

    URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + m
    r = requests.get(URL)
    str_json = r.text
    data = json.loads(str_json)
    my_list = []

    for i in data['exchangeRate']:
        for k, v in i.items():
            if v == cur:
                my_list.append(v)

    if len(my_list) == 0:
        print('This currency does not exist, please try again - (example: EUR, USD, RUB, GBP, PLN)')
    else:
        flag = False



def check_date():
    flag = True
    while flag == True:
        try:
            date = input('Enter date "day"."monat"."year", (example: 2.4.2021): ')



            date_format = "%d.%m.%Y"

            start = datetime.strptime(date, date_format)
            now = datetime.now()

            list1 = date.split('.')

            if start > now:
                print('Your date in the future, please enter again')
            else:
                return int(list1[0]), int(list1[1]), int(list1[2])
        except ValueError:
            print('You entered the wrong date, perhaps this day is not on the calendar. Please repeat again. Example(12.11.2021)')


something = check_date()
year = something[2]
month = something[1]
day = something[0]



def daterange(start_date, end_date):
    for i in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(i)

start_date = date(year, month, day)
end_date = datetime.now().date()

print('Currency:' + cur)
some = 0

for single_date in daterange(start_date, end_date):
    m = single_date.strftime("%d.%m.%Y")
    URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + m
    r = requests.get(URL)
    str_json = r.text
    data = json.loads(str_json)



    for i in data['exchangeRate']:
        for k, v in i.items():
            if v == cur:
                result_dif = '------'
                if some == 0:
                    some = i['purchaseRateNB']
                    print('Date:', m)
                    print('NBU:', i['purchaseRateNB'], '    ', result_dif)
                elif some != 0 and some != i['purchaseRateNB']:
                    result_dif = i['purchaseRateNB'] - some
                    some = i['purchaseRateNB']
                    print('Date:', m)
                    print('NBU:', i['purchaseRateNB'], '    ', '%.4f' % result_dif)
                elif some != 0 and some == i['purchaseRateNB']:
                    result_dif = '------'
                    some = i['purchaseRateNB']
                    print('Date:', m)
                    print('NBU:', i['purchaseRateNB'], '    ', result_dif)
