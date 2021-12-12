import json


class ExceptionValue(Exception):
    def __init__(self, text):
        self.text = text

class MyTypeError(Exception):
    def __init__(self, text):
        self.text = text

class StripingTypeError(Exception):
    def __init__(self, text):
        self.text = text
class CheckTypeError(Exception):
    def __init__(self, text):
        self.text = text


with open('usernames.json', 'r+') as file_1:
    data_usernames = json.load(file_1)

def get_money_func(num):
    first_var = num
    with open('money_data.json', 'r+') as my_file:
        data_money = json.load(my_file)

    result_data = dict()

    for s1, s2 in data_money.items():
        result_data[int(s1)] = s2

    my_dict = dict()
    min_dict = min(result_data.keys())

    flag = 0

    for k, v in result_data.items():
        if (num >= k and num % k >= min_dict) or num % k == 0:

            if num == 0:
                break
            my_dict[k] = num // k
            result_data[k] = result_data[k] - my_dict[k]
            num = num % k


    # перший варіант
    sum1 = 0
    for k, v in my_dict.items():
        sum1 = sum1 + (k * v)
    if sum1 == first_var:
        flag = 1

    # другий варіант
    sum2 = 0
    for key, value in my_dict.items():
        sum2 = sum2 + (key * value)
    if sum2 != first_var:
        flag = 2

    # третій варіант
    for some in result_data.values():
        if some < 0:
            flag = 3
            break

    return flag, my_dict, result_data

def check_usernames():
    for i in range(2, -1, -1):
        my_input1 = input("Enter your login: ")
        my_input2 = input("Enter your password: ")
        if my_input1 in data_usernames['users'] and my_input2 == data_usernames['users'][my_input1]:
            return my_input1
        elif my_input1 in data_usernames['admins'] and my_input2 == data_usernames['admins'][my_input1]:
            return my_input1
        elif i == 0:
            x = "Thank you! Good luck :)"
            return x

        else:
            print(f"Wrong login or password. Enter again, you have {i} attempt left! ")


def check_balance(user):
    with open(f'{user}_balance_data.json', 'r+') as my_file:
        data_balance = json.load(my_file)
    flag = True
    while flag == True:
        try:
            result = data_balance[user]
            print(f"Your balance of money is {result}$")
            back = int(input("Press '1' if you want to exit, '2' if you want to return to the main menu: "))
            if back == 1:
                print('Thank you! Good luck :)')
                flag = False
            elif back == 2:
                flag = False
                return main_func(user)
            elif back < 1 or back > 2:
                raise MyTypeError('number')

        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')


def append_balance(user):
    with open(f'{user}_balance_data.json', 'r+') as my_file1:
        data_balance = json.load(my_file1)
    with open(f'{user}_transactions_data.json', 'r+') as my_file2:
        data_trans = json.load(my_file2)

    flag = True
    while flag == True:
        try:
            summ = input("Enter the amount of money you wish to deposit into the account, example(300): ")
            if int(summ) <= 0:
                print('You must enter a positive number')
                continue
            old_value = data_balance[user]
            new_value = old_value + int(summ)
            data_balance[user] = new_value
            with open(f'{user}_balance_data.json', 'w') as f:
                json.dump(data_balance, f, indent = 2)

            append_trans = f'The client {user} has replenished the sum of money of ${int(summ)}. The rest of money - {new_value}'
            data_trans[user].append(append_trans)
            with open(f'{user}_transactions_data.json', 'w') as big:
                json.dump(data_trans, big, indent = 2)

            result = f"Your account is funded by ${int(summ)}, the rest of money is {new_value}$"
            print(result)
            flag_2 = True
            while flag_2 == True:
                try:
                    back = int(input("Press '1' if you want to exit, '2' if you want to return to the main menu: "))
                    if back == 1:
                        print('Thank you! Good luck :)')
                        flag_2 = False
                        flag = False
                    elif back == 2:
                        flag = False
                        return main_func(user)
                    elif back < 1 or back > 2:
                        raise MyTypeError('number')
                except MyTypeError as Mte:
                    print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
                except:
                    print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
        except:
            print('You must enter a number')

def cash_out_func(user):
    with open(f'{user}_balance_data.json', 'r+') as my_file1:
        data_balance = json.load(my_file1)
    with open(f'{user}_transactions_data.json', 'r+') as my_file2:
        data_trans = json.load(my_file2)
    with open('money_data.json', 'r+') as my_file3:
        data_money = json.load(my_file3)

    flag = True
    while flag == True:
        try:
            print('Banknotes are available: ')
            for k, v in data_money.items():
                if data_money[k] == 0:
                    continue
                print(k, end = ' | ')
            old_money = data_balance[user]
            summ = input("\nHow much money do you want to withdraw from your account? Example(300): ")
            if int(summ) > old_money:
                print(f'Error: You cannot get - {int(summ)}. The amount you want to withdraw is higher than your balance! ')
                some = input("Please press 'Y' to check balance of money, 'N' if not: ")
                if some == 'Y':
                    print("Your balance is: ", old_money, "$")
                    continue
                elif some == 'N':
                    continue
                else:
                    raise ExceptionValue("You")
            elif int(summ) <= 0:
                print('Error: You must enter a positive number!')
                continue
            else:
                result_get = get_money_func(int(summ))

                if result_get[0] == 1:
                    print("Take your money please: ")
                    for k, v in result_get[1].items():
                        print(k, '-', v, 'unit/units.')
                    append_data = dict()
                    for key, value in result_get[2].items():
                        append_data[str(key)] = value
                    with open('money_data.json', 'w') as f:
                        json.dump(append_data, f, indent = 2)
                    new_value = old_money - int(summ)
                    data_balance[user] = new_value

                    append_trans = f'The client {user} withdrew ${int(summ)} from the account. The rest of money - {new_value}'
                    data_trans[user].append(append_trans)
                    with open(f'{user}_transactions_data.json', 'w') as big:
                        json.dump(data_trans, big, indent = 2)

                    result = f"${new_value} left in your account"
                    print(' ')
                    print(result)

                    with open(f'{user}_balance_data.json', 'w') as f:
                        json.dump(data_balance, f, indent = 2)
                    try:
                        back = int(input("Press '1' if you want to exit, '2' if you want to return to the main menu: "))
                        if back == 1:
                            return
                        elif back == 2:
                            return main_func(user)
                        elif back < 1 or back > 2:
                            raise MyTypeError('number')

                    except MyTypeError as Mte:
                        print(f'Error: Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu!')

                elif result_get[0] == 2:
                    print("Error: We can't give you that amount, we don't have the banknotes you need!")

                elif result_get[0] == 3:
                    print("Error: Sorry we ran out of banknotes, try another amount!")


        except ExceptionValue as ExV:
            print(f"Error: {ExV.text} must enter 'Y' or 'N'. ")
        except:
            print(f'Error: You must enter a positive number!')




def trans_func(user):
    with open(f'{user}_transactions_data.json', 'r+') as my_file:
        data_trans = json.load(my_file)
    flag = True
    while flag == True:
        try:
            print("Your transactions: ")
            for i in data_trans[user]:
                print((data_trans[user].index(i))+1, ')', ' ', i)
            back = int(input("Press '1' if you want to exit, '2' if you want return to the main menu: "))
            if back == 1:
                print('Thank you! Good luck :)')
                flag = False
            elif back == 2:
                flag = False
                return main_func(user)
            elif back < 1 or back > 2:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
        except:
            print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')




def main_func(result):
    with open(f'{result}_balance_data.json', 'r+') as my_file:
        data_balance = json.load(my_file)
    if result in data_balance:
        print('Main menu'.center(30, ' '))
        print('1. Check your balance')
        print('2. Cash in')
        print('3. Cash out')
        print('4. Check your last transaktions')
        print('5. Exit')
        flag = True
        while flag == True:
            try:
                main_input = int(input("Select the desired operation. Enter from 1 to 5: "))
                fast_list = [x for x in range(1, 6)]
                if main_input < 1 or main_input > 5:
                    raise MyTypeError('number')

                flag = False
                if main_input == 1:
                    check_balance(result)
                elif main_input == 2:
                    append_balance(result)
                elif main_input == 3:
                    cash_out_func(result)
                elif main_input == 4:
                    trans_func(result)
                elif main_input == 5:
                    print('Thank you! Good luck :)')


            except MyTypeError as Mte:
                print(f'Error: Enter a {Mte.text} in the range from 1 to 5, example(3)!')
            except:
                print(f"Error: You must choose a number. Please enter from 1 to 5, example(3)!")
    else:
        print("Thank you! Good luck :)")


def ink_main_func(result):
    print('Admin menu'.center(30, ' '))
    print('1. Check balance of money')
    print('2. Cash in')
    print('3. Cash out')
    print('4. Check users last transaktions')
    print('5. Exit')
    ink_flag = True
    while ink_flag == True:
        try:
            ink_main_input = int(input("Select the desired operation. Enter from 1 to 5: "))
            ink_fast_list = [x for x in range(1, 6)]
            if ink_main_input < 1 or ink_main_input > 5:
                raise MyTypeError('number')
            ink_flag = False

            if ink_main_input == 1:
                ink_check_balance()
            elif ink_main_input == 2:
                ink_cashin_money(result)
            elif ink_main_input == 3:
                ink_cashout_money(result)
            elif ink_main_input == 4:
                ink_transactions(result)
            elif ink_main_input == 5:
                return

        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 5, example(3)')

def ink_check_balance():
    with open('money_data.json', 'r+') as my_file:
        money_data = json.load(my_file)
    for k, v in money_data.items():
        print(k, '-', v, 'units.')
    x = int(input("If you wish exit '1', if return to the main menu press '2': "))
    flag2 = True
    while flag2 == True:
        try:
            if x == 1:
                return
            if x == 2:
                ink_main_func(result)
            flag2 = False
            if x < 1 or x > 2:
                raise MyTypeError('number')
        except MyTypeError as Mte:
            print(f'Error: Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu!')


def ink_cashin_money(result):
    with open('money_data.json', 'r+') as my_file:
        ink_append_data = json.load(my_file)
    flag = True
    while flag == True:
        try:
            banknote = input("Enter one of this banknotes: 1000, 500, 200, 100, 50, 20, 10. (example: 500): ")
            if (banknote in ink_append_data) == False:
                raise MyTypeError('banknote')
            quantity = int(input("Enter a quatity of banknotes, (example: 120): "))
            first_quantity = ink_append_data[banknote]
            result_quantity = first_quantity + quantity
            ink_append_data[banknote] = result_quantity
            with open('money_data.json', 'w') as f:
                json.dump(ink_append_data, f, indent = 2)
            x = int(input("If you wish to continue press '1', if to exit to the main menu press '2': "))
            flag2 = True
            while flag2 == True:
                try:
                    if x == 1:
                        ink_cashin_money(result)
                    if x == 2:
                        ink_main_func(result)
                    flag2 = False


                    if x < 1 or x > 2:
                        raise MyTypeError('number')
                except MyTypeError as Mte:
                    print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')

            flag = False

        except MyTypeError as Mte:
            print(f'Error: You have entered the wrong {Mte.text}. Try again ')
        except ValueError:
            print(f'Error: Enter how many banknotes you wish to deposit, example(50)')

def ink_cashout_money(result):
    with open('money_data.json', 'r+') as my_file:
        ink_append_data = json.load(my_file)
    flag = True
    while flag == True:
        try:
            banknote = input("Enter one of these notes you wish to withdraw: 1000, 500, 200, 100, 50, 20, 10. (example: 500): ")

            if (banknote in ink_append_data) == False:
                some = input("Error: Now we don't have that banknote at our ATM. Please press 'Y' to check balance of money, 'N' if not: ")
                if some == 'Y':
                    with open('money_data.json', 'r+') as my_file:
                        money_data = json.load(my_file)
                    for k, v in money_data.items():
                        print(k, '-', v, 'units.')
                    continue
                elif some == 'N':
                    continue
                else:
                    continue


            quantity = int(input("Enter a quatity of banknotes (example: 120): "))

            first_quantity = ink_append_data[banknote]
            if quantity > first_quantity:
                some = input("Error: You cannot withdraw more than your balance. Please press 'Y' to check balance of money, 'N' if not: ")
                if some == 'Y':
                    with open('money_data.json', 'r+') as my_file:
                        money_data = json.load(my_file)
                    for k, v in money_data.items():
                        print(k, '-', v, 'units.')
                    continue
                elif some == 'N':
                    continue
                else:
                    continue

            elif quantity <= 0:
                raise ExceptionValue('Quantity')

            result_quantity = first_quantity - quantity
            ink_append_data[banknote] = result_quantity
            with open('money_data.json', 'w') as f:
                json.dump(ink_append_data, f, indent = 2)

            flag2 = True
            while flag2 == True:
                try:
                    x = int(input("If you wish to continue press '1', if to exit to the main menu press '2': "))
                    if x == 1:
                        ink_cashout_money(result)
                    elif x == 2:
                        ink_main_func(result)
                    elif x < 1 or x > 2:
                        raise MyTypeError('number')
                    flag2 = False

                except MyTypeError as Mte:
                    print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
                except ValueError:
                    print(f'Enter a number in the range from 1 to 2, example(2) if you want return to the main menu')
                except StripingTypeError as Ste:
                    print(f'There are fewer notes on the {Ste.text} than you want to withdraw. Try again')

            flag = False

        except MyTypeError as Mte:
            print(f'Error: You have entered the wrong {Mte.text}. Try again ')
        except ExceptionValue as Ev:
            print(f'Error: {Ev.text} of banknotes must be positiv digit!')
        except ValueError:
            print(f'Error: Enter how many banknotes you wish to deposit, example(50)')

def ink_transactions(result):
    with open('usernames.json', 'r+') as my_file:
        check_data = json.load(my_file)

    for k, v  in check_data['users'].items():
        with open(f'{k}_transactions_data.json') as file_1:
            ink_trans_date = json.load(file_1)
        print(k, ':')
        m = 1
        for j in ink_trans_date[k]:
            print(m, ')', ' ', j)
            m += 1
        print('-------------------------------------------------------------------------------------------')


    flag2 = True
    while flag2 == True:
        try:
            x = int(input("If you wish exit press '1', if return to the main menu press '2': "))
            if x == 1:
                return
            if x == 2:
                ink_main_func(result)



            if x < 1 or x > 2:
                raise MyTypeError('number')
            flag2 = False
        except MyTypeError as Mte:
            print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
        except ValueError:
            print(f'Enter a number in the range from 1 to 2, example(2) if you want return to the main menu')




result = check_usernames()
if result in data_usernames['users']:
    main_func(result)
else:
    ink_main_func(result)
