import requests
import json
from datetime import datetime

def check_cur(main_input):
    flag = True
    while flag == True:
        current_datetime = datetime.now()

        m = str(current_datetime.day) + '.' + str(current_datetime.month) + '.' + str(current_datetime.year)
        URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + m
        r = requests.get(URL)
        str_json = r.text
        data = json.loads(str_json)
        my_list = []

        for i in data['exchangeRate']:
            for k, v in i.items():
                if v == main_input:
                    my_list.append(v)

        if len(my_list) == 0:
            print('This currency does not exist, please try again - (example: EUR, USD, RUB, GBP, PLN)')
            return False
        else:
            return True

flag = True
while flag == True:
    my_input1 = input('Enter first currency (example EUR, USD, RUB, GBP, PLN): ')
    some = check_cur(my_input1)
    if some == False:
        continue
    my_input2 = input('Enter second currency (example EUR, USD, RUB, GBP, PLN): ')
    some2 = check_cur(my_input2)
    if some2 == False:
        continue
    else:
        flag = False
    summ_for_sale = float(input('Enter summ of money (example: 1340): '))


current_datetime = datetime.now()
date_format = '%d.%m.%Y'
m = current_datetime.strftime(date_format)


URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + m
r = requests.get(URL)
str_json = r.text
data = json.loads(str_json)

if len(data) == 0:
    date_format = '%d.%m.%Y'
    tomorrow = current_datetime - timedelta(days=1)
    last_tomorrow = tomorrow.strftime(date_format)
    URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=' + last_tomorrow
    r = requests.get(URL)
    str_json = r.text
    data = json.loads(str_json)

    def konv(cur1, cur2, summ):
        result_summ = 0

        if cur1 == 'UAH':
            for i in data['exchangeRate']:
                for k, v in i.items():
                    if v == my_input2:
                        result_summ = summ / i['saleRate']
                        return result_summ
        elif cur2 == 'UAH':
            for i in data['exchangeRate']:
                for k, v in i.items():
                    if v == my_input1:
                        result_summ = summ * i['purchaseRate']
                        return result_summ

        for i in data['exchangeRate']:
            for k, v in i.items():
                if v == my_input1:
                    result_summ = summ * i['purchaseRate']

        for j in data['exchangeRate']:
            for key, value in j.items():
                if value == my_input2:
                    result_summ = result_summ / j['saleRate']

        return result_summ

    res = konv(my_input1, my_input2, summ_for_sale)
    print('%.2f' % res, my_input2)

else:
    def konv(cur1, cur2, summ):
        result_summ = 0

        if cur1 == 'UAH':
            for i in data['exchangeRate']:
                for k, v in i.items():
                    if v == my_input2:
                        result_summ = summ / i['saleRate']
                        return result_summ
        elif cur2 == 'UAH':
            for i in data['exchangeRate']:
                for k, v in i.items():
                    if v == my_input1:
                        result_summ = summ * i['purchaseRate']
                        return result_summ

        for i in data['exchangeRate']:
            for k, v in i.items():
                if v == my_input1:
                    result_summ = summ * i['purchaseRate']

        for j in data['exchangeRate']:
            for key, value in j.items():
                if value == my_input2:
                    result_summ = result_summ / j['saleRate']

        return result_summ

    res = konv(my_input1, my_input2, summ_for_sale)
    print('%.2f' % res, my_input2)
