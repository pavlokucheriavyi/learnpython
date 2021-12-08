import json

class ExceptionValue(Exception):
    def __init__(self, text):
        self.text = text

class MyTypeError(Exception):
    def __init__(self, text):
        self.text = text

with open('username_transactions.json', 'r+') as file_3:
    data_trans = json.load(file_3)

with open('usernames.json', 'r+') as file_1:
    data_usernames = json.load(file_1)


def check_usernames():
    for i in range(2, -1, -1):
        my_input1 = input("Enter your login: ")
        my_input2 = input("Enter your password: ")
        key, value = my_input1, my_input2
        if key in data_usernames and value == data_usernames[key]:
            print("Welcome :)".center(30, ' '))
            return my_input1
        elif i == 0:
            l = "Thank you! Good luck :)"
            return l
        else:
            print(f"Wrong login or password. Enter again, you have {i} attempt left! ")

with open('usernames_balance.json', 'r+') as file_2:
    data_balance = json.load(file_2)

def check_balance(user):
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
    flag = True
    while flag == True:
        try:
            summ = int(input("Enter the amount of money you wish to deposit into the account, example(300): "))
            old_value = data_balance[user]
            new_value = old_value + summ
            data_balance[user] = new_value
            with open('usernames_balance.json', 'w') as f:
                json.dump(data_balance, f, indent = 2)

            append_trans = f'The client {user} has replenished the sum of money of ${summ}. The rest of money - {new_value}'
            data_trans[user].append(append_trans)
            with open('username_transactions.json', 'w') as big:
                json.dump(data_trans, big, indent = 2)

            result = f"Your account is funded by ${summ}, the rest of money is {new_value}$"
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
            print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')

def cash_out_func(user):
    flag = True
    while flag == True:
        for i in range(6):
            if i == 5:
                print("Thank you! Good luck :)")
                break
            try:
                summ = int(input("How much money do you want to withdraw from your account? Example(300): "))
                old_money = data_balance[user]
                if summ > old_money:
                    raise ExceptionValue(summ)
                else:
                    old_value = data_balance[user]
                    new_value = old_value - summ
                    data_balance[user] = new_value
                    with open('usernames_balance.json', 'w') as f:
                        json.dump(data_balance, f, indent = 2)

                    append_trans = f'The client {user} withdrew ${summ} from the account. The rest of money - {new_value}'
                    data_trans[user].append(append_trans)
                    with open('username_transactions.json', 'w') as big:
                        json.dump(data_trans, big, indent = 2)

                    result = f"${new_value} left in your account"
                    print(result)
                    flag_2 = True
                    while flag_2 == True:
                        try:
                            back = int(input("Press '1' if you want to exit, '2' if you want to return to the main menu: "))
                            if back == 1:
                                print("Thank you! Good luck :)")
                                flag_2 = False
                                return
                            elif back == 2:
                                flag_2 = False
                                flag = False
                                return main_func(user)
                            elif back < 1 or back > 2:
                                raise MyTypeError('number')

                        except MyTypeError as Mte:
                            print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
                        except:
                            print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')


            except ExceptionValue as ExV:
                print(f"You cannot get - {ExV.text}. The amount you want to withdraw is higher than your balance. Try again")

                flag = True
                while flag == True:
                    try:
                        x = input("Do you want to see your balance? 'Y' - yes, 'N' - no: ")
                        if x == 'Y':
                            print(f"Your balance of money is {data_balance[user]}$")
                            flag = False
                        elif x == 'N':
                            break
                        elif x != 'Y':
                            raise MyTypeError('Y')
                    except MyTypeError as Mte:
                        print(f"Please enter {Mte.text} or N ")

def trans_func(user):
    flag = True
    while flag == True:
        try:
            print("Your transactions: ")
            for i in data_trans[user]:
                print((data_trans[user].index(i))+1, ')', ' ', i)
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



def main_func(result=check_usernames()):
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
            print(f'Enter a {Mte.text} in the range from 1 to 4, example(3)')
        except:
            print(f"You must choose a number. Please enter from 1 to 4, example(3)")



main_func()
