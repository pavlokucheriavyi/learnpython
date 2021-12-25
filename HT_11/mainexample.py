import requests
import json
import random

class MyTypeError(Exception):
    def __init__(self, text):
        self.text = text

r = requests.get('https://jsonplaceholder.typicode.com/users')
str_json = r.text

data_json = json.loads(str_json)

def check_info():
    for i in data_json:
        for k, v in i.items():
            if k == 'id':
                print(k + ':', v)
            elif k == 'name':
                print(k + ':', v)
            elif k == 'username':
                print(k + ':', v)
        print('-----------------------------------')
    while True:
        try:
            main_input = int(input('If you want exit enter "1", if you want return to the main menu enter "2": '))
            if main_input == 1:
                return
            elif main_input == 2:
                return main_func()
            elif main_input < 1 or main_input > 2:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')

def main_func():
    print('Main menu'.center(40, ' '))
    print('1. Check brief information about clients')
    print('2. More information about a specific client')
    print('3. Exit')

    flag = True
    while flag == True:
        try:
            main_input = int(input("Select the desired operation. Enter from 1 to 3: "))

            if main_input < 1 or main_input > 3:
                raise MyTypeError('number')

            flag = False
            if main_input == 1:
                check_info()
            elif main_input == 2:
                flag_second = True
                while flag_second == True:
                    try:
                        client_input = int(input('10 users. Please enter id of user in the range (1 - 10), example(4): '))

                        if client_input > 10 or client_input < 1:
                            raise MyTypeError('Users')

                        flag_second = False

                        menu_info_about_client(client_input)

                    except MyTypeError as Mte:
                        print(f'{Mte.text} in total 10. The number must be in the range from 1 to 10')
                    except ValueError:
                        print('Error: Please enter a positive number in range from 1 to 10!')

            elif main_input == 3:
                return

        except MyTypeError as Mte:
            print(f'Error: Enter a {Mte.text} in the range from 1 to 3, example(3)!')
        except ValueError:
           print(f"Error: You must choose a number. Please enter from 1 to 3, example(3)!")

def full_info_about_user(client):
    for i in data_json:
        if client in i.values():
            for k, v in i.items():
                if k == 'address' or k == 'company':
                    continue
                print(k + ':', v)


    print('Address'.center(60, '-'))

    for i in data_json:
        if client in i.values():
            for k, v in i.items():
                if k == 'address':
                    for key, value in v.items():
                        if key == 'geo':
                            continue
                        print(key + ':', value)

    print('geo: ')

    for i in data_json:
        if client in i.values():
            for k, v in i.items():
                if k == 'address':
                    for key, value in v.items():
                        if key == 'geo':
                            for key1, value1 in value.items():
                                print(key1 + ':', value1, end = '; ')


    print('\n')
    print('Company'.center(60, '-'))

    for i in data_json:
        if client in i.values():
            for k, v in i.items():
                if k == 'company':
                    for key, value in v.items():
                        print(key + ':', value)

    while True:
        try:
            main_input = int(input('If you want exit enter "1", if you want return to the menu of client enter "2", if you want return to the main menu enter "3": '))
            if main_input == 1:
                return
            elif main_input == 2:
                return menu_info_about_client(client)
            elif main_input == 3:
                return main_func()
            elif main_input < 1 or main_input > 3:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 3, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 3, example(1) if you want exit')

def more_post(id_of_post, id_of_user):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    str_json = response.text

    data_dict = json.loads(str_json)

    for i in data_dict:
        for k, v in i.items():
            if i['id'] == id_of_post:
                print('ID:', i['id'])
                print('title:', i['title'])
                print('text:', i['body'])
                break

    response_comments = requests.get('https://jsonplaceholder.typicode.com/comments')
    str_json = response_comments.text

    data_comments = json.loads(str_json)

    my_list = []

    for i in data_comments:
        for key, value in i.items():
            if i['postId'] == id_of_post:
                my_list.append(i['id'])
                break

    print('Count comment:', len(my_list))
    print('Comments id:')
    for j in my_list:
        print('id ' + '-->', j)

    while True:
        try:
            main_input = int(input('If you want exit enter "1", if you want return to the menu of client enter "2", if you want return to the main menu enter "3": '))
            if main_input == 1:
                return
            elif main_input == 2:
                return menu_info_about_client(id_of_user)
            elif main_input == 3:
                return main_func()
            elif main_input < 1 or main_input > 3:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 3, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 3, example(1) if you want exit')


def posts(id_of_user):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    str_json = response.text

    data_dict = json.loads(str_json)

    my_list = []

    for i in data_dict:
        for k, v in i.items():
            if i['userId'] == id_of_user:
                my_list.append(i['id'])
                print('id:', i['id'])
                print('title:', '"' + i['title'] + '"')
                print('--------------------------------------------------------------')
                break


    flag = True
    while flag == True:
        try:
            x = input('If you want to know detailed information about one post of this user press "Y", if not press "N": ')
            if x == 'Y':
                second_flag = True
                while second_flag == True:
                    try:
                        some = int(input('Please enter id of post: '))
                        if some < my_list[0] or some > my_list[-1]:
                            raise MyTypeError('Id')
                        second_flag = False
                    except MyTypeError as Mte:
                        print(f'Error: {Mte.text} must be in a range from {my_list[0]} to {my_list[-1]}. Try again please')
                    except ValueError:
                        print(f'Error: Please enter positive number of id in a range from {my_list[0]} to {my_list[-1]}')
                more_post(some, id_of_user)

            elif x == 'N':
                menu_info_about_client(id_of_user)
            elif x != 'Y' or x != 'N':
                raise MyTypeError('Please')
            flag = False

        except MyTypeError as Mte:
            print(f'Error: {Mte.text} enter a large \'Y\' if you want to know more information about a client\'s post, if not enter a large \'N\'')

def tasks_menu(id_of_user):
    for i in data_json:
        for k, v in i.items():
            if v == id_of_user:
                name = i['name']
    print(f'"{name}" menu'.center(40, ' '))
    print('1. Done tasks ')
    print('2. Not done tasks ')

    client_input = int(input("Select the desired operation. Enter from 1 to 2: "))

    if client_input == 1:
        tasks_func_true(id_of_user)
    elif client_input == 2:
        tasks_func_false(id_of_user)

def tasks_func_true(id_of_user):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    str_json = response.text

    last_data = json.loads(str_json)

    for i in last_data:
        for k, v in i.items():
            if i['userId'] == id_of_user and i['completed'] == True:
                print('id:', i['id'])
                print('title:', i['title'])
                print('------------------------------------------')
                break

    while True:
        try:
            main_input = int(input('If you want exit enter "1", if you want return to the menu of client enter "2", if you want return to the main menu enter "3": '))
            if main_input == 1:
                return
            elif main_input == 2:
                return menu_info_about_client(id_of_user)
            elif main_input == 3:
                return main_func()
            elif main_input < 1 or main_input > 3:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 3, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 3, example(1) if you want exit')

def tasks_func_false(id_of_user):
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    str_json = response.text

    last_data = json.loads(str_json)

    for i in last_data:
        for k, v in i.items():
            if i['userId'] == id_of_user and i['completed'] == False:
                print('id:', i['id'])
                print('title:', i['title'])
                print('------------------------------------------')
                break

    while True:
        try:
            main_input = int(input('If you want exit enter "1", if you want return to the menu of client enter "2", if you want return to the main menu enter "3": '))
            if main_input == 1:
                return
            elif main_input == 2:
                return menu_info_about_client(id_of_user)
            elif main_input == 3:
                return main_func()
            elif main_input < 1 or main_input > 3:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 3, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 3, example(1) if you want exit')


def menu_info_about_client(main_input):

    name = '-'
    id_of_user = 0

    for i in data_json:
        for k, v in i.items():
            if v == main_input:
                name = i['name']
                id_of_user = i['id']

    print(f'"{name}" menu'.center(40, ' '))
    print('1. Check more information about user ')
    print('2. Check users posts ')
    print('3. User tasks')
    print('4. User random photo')
    print('5. Return to the main menu')
    print('6. Exit')

    flag = True
    while flag == True:
        try:
            client_input = int(input("Select the desired operation. Enter from 1 to 6: "))

            if client_input < 1 or client_input > 6:
                raise MyTypeError('number')

            elif client_input == 1:
                full_info_about_user(name)
            elif client_input == 2:
                posts(id_of_user)
            elif client_input == 3:
                tasks_menu(id_of_user)
            elif client_input == 4:
                photo(id_of_user)
            elif client_input == 5:
                main_func()
            elif client_input == 6:
                return

            flag = False

        except MyTypeError as Mte:
            print(f'Error: Enter a {Mte.text} in the range from 1 to 6, example(4)!')
        except ValueError:
            print(f"Error: You must choose a number. Please enter from 1 to 6, example(2)!")


def album(id_of_user):
    response = requests.get('https://jsonplaceholder.typicode.com/albums')
    str_json = response.text

    data_dict = json.loads(str_json)
    new_list = []

    for i in data_dict:
        for k, v in i.items():
            if i['userId'] == id_of_user:
                new_list.append(i['id'])
                break

    return new_list

def photo(id_of_user):
    main_list = album(id_of_user)

    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    str_json = response.text

    data_dict = json.loads(str_json)

    result_list = []

    for i in main_list:
        for j in data_dict:
            for k, v in j.items():
                if i == j['albumId']:
                    result_list.append(j['id'])
                    break

    result_var = random.choice(result_list)

    for i in data_dict:
        for k, v in i.items():
            if i['id'] == result_var:
                print(i['url'])
                break

    while True:
        try:
            main_input = int(input('If you want exit enter "1", if you want return to the menu of client enter "2", if you want return to the main menu enter "3": '))
            if main_input == 1:
                return
            elif main_input == 2:
                return menu_info_about_client(id_of_user)
            elif main_input == 3:
                return main_func()
            elif main_input < 1 or main_input > 3:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 3, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 3, example(1) if you want exit')




main_func()