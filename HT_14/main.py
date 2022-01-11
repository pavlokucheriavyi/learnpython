import requests
import create_tables as ct
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


class ExchangeRates(object):
    def check_kurs(self):
        r = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
        str_json = r.text

        data = json.loads(str_json)

        for i in data:
            for k, v in i.items():
                if k == 'ccy':
                    print(v + ':')
                elif k == 'base_ccy':
                    continue
                elif k == 'buy':
                    print(k + ':', '%.2f' % float(v), 'UAH')
                else:
                    print(k + ':', '%.2f' % float(v), 'UAH')
            print('--------------------------------------')
        flag = True
        while flag == True:
            try:
                back = int(input("Press '1' if you want to exit, '2' if you want to return to the main menu: "))
                if back == 1:
                    print('Thank you! Good luck :)')
                    flag = False
                elif back == 2:
                    flag = False
                    if isinstance(self, SimpleUser):
                        new_obj = SimpleUser(self.login)
                        return new_obj
                    elif isinstance(self, MainAdmin):
                        new_obj_admin = MainAdmin(self.login)
                        return new_obj_admin

                elif back < 1 or back > 2:
                    raise MyTypeError('number')

            except MyTypeError as Mte:
                print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
            except:
                print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')

class SimpleUser(ExchangeRates):
    def __init__(self, login):
        self.login = login

        self.__main_func(self.login)

    def __main_func(self, result):
        print('Main menu'.center(30, ' '))
        print('1. Check your balance')
        print('2. Cash in')
        print('3. Cash out')
        print('4. Check your last transaktions')
        print('5. See the current exchange rate')
        print('6. Exit')
        flag = True
        while flag == True:
            try:
                main_input = int(input("Select the desired operation. Enter from 1 to 5: "))
                if main_input < 1 or main_input > 6:
                    raise MyTypeError('number')

                flag = False
                if main_input == 1:
                    self.__check_balance(result)
                elif main_input == 2:
                    self.__append_balance(result)
                elif main_input == 3:
                    self.__cash_out_func(result)
                elif main_input == 4:
                    self.__trans_func(result)
                elif main_input == 5:
                    self.check_kurs()
                elif main_input == 6:
                    print('Thank you! Good luck :)')


            except MyTypeError as Mte:
                print(f'Error: Enter a {Mte.text} in the range from 1 to 5, example(3)!')
            except:
                print(f"Error: You must choose a number. Please enter from 1 to 5, example(3)!")

    def __get_money_func(self, num):
        same_list = []

        with ct.con:
            cur = ct.con.cursor()
            cur.execute("SELECT * FROM inkasator_check")
            rows = cur.fetchall()

            for row in rows:
                same_list.append(row)

        result_dict = dict()

        for i in same_list:
            result_dict[i[0]] = i[1]

        first_var = num

        result_data = dict()

        for s1, s2 in result_dict.items():
            result_data[int(s1)] = s2

        my_dict = dict()
        new_dict = dict()

        for k, v in result_data.items():
            if v == 0:
                continue
            new_dict[k] = v

        min_dict = min(new_dict.keys())

        flag = 0

        for k, v in result_data.items():
            if (num >= k and num % k >= min_dict) or num % k == 0:
                if result_data[k] == 0:
                    continue

                if num == 0:
                    break
                if num // k > result_data[k]:
                    some = k * result_data[k]
                    num = num - some
                    my_dict[k] = result_data[k]
                    result_data[k] = result_data[k] - result_data[k]
                    continue
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

        return flag, my_dict, result_data


    def __check_balance(self, user):
        flag = True
        while flag == True:
            try:
                result = ct.result_dict_balance[user]
                print(f"Your balance of money is {result}$")
                back = int(input("Press '1' if you want to exit, '2' if you want to return to the main menu: "))
                if back == 1:
                    print('Thank you! Good luck :)')
                    flag = False
                elif back == 2:
                    flag = False
                    return self.__main_func(user)
                elif back < 1 or back > 2:
                    raise MyTypeError('number')

            except MyTypeError as Mte:
                print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
            except:
                print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')


    def __append_balance(self, user):
        something = user

        flag = True
        while flag == True:
            try:
                summ = input("Enter the amount of money you wish to deposit into the account, example(300): ")
                if int(summ) <= 0:
                    print('You must enter a positive number')
                    continue
                old_value = ct.result_dict_balance[user]
                new_value = old_value + int(summ)
                ct.result_dict_balance[user] = new_value

                user_balance_result_list = []
                for k, v in ct.result_dict_balance.items():
                    t = k, v
                    user_balance_result_list.append(t)

                ct.cur.execute('DELETE FROM users_balance;', )

                for user in user_balance_result_list:
                    exists = ct.cur.execute('''SELECT username, balance FROM users_balance WHERE username=?''',
                                         (user[0],)).fetchone()
                    if not exists:
                        ct.cur.execute('''INSERT INTO users_balance VALUES (?, ?) ''', user)

                ct.con.commit()

                append_trans = f'The client {something} has replenished the sum of money of ${int(summ)}. The rest of money - {new_value}\n'

                for i in ct.same_dict_trans:
                    if i[0] == something:
                        i[1] = i[1] + append_trans

                for j in ct.same_dict_trans:
                    ct.result_trans_list.append(tuple(j))

                ct.cur.execute('DELETE FROM transactions;', )

                for user in ct.same_dict_trans:
                    exists = ct.cur.execute('''SELECT username, trans FROM transactions WHERE username=?''',
                                         (user[0],)).fetchone()
                    if not exists:
                        ct.cur.execute('''INSERT INTO transactions VALUES (?, ?) ''', user)

                ct.con.commit()

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
                            return self.__main_func(something)
                        elif back < 1 or back > 2:
                            raise MyTypeError('number')
                    except MyTypeError as Mte:
                        print(
                            f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
                    except:
                        print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')
            except MyTypeError as Mte:
                print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
            except:
                print('You must enter a number')


    def __cash_out_func(self, user):
        something = user

        flag = True
        while flag == True:
            try:
                print('Banknotes are available: ')
                for k, v in ct.result_dict.items():
                    if ct.result_dict[k] == 0:
                        continue
                    print(k, end=' | ')
                old_money = ct.result_dict_balance[user]
                summ = input("\nHow much money do you want to withdraw from your account? Example(300): ")
                if int(summ) > old_money:
                    print(
                        f'Error: You cannot get - {int(summ)}. The amount you want to withdraw is higher than your balance! ')
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
                    result_get = self.__get_money_func(int(summ))
                    if result_get[0] == 1:
                        print("Take your money please: ")
                        for k, v in result_get[1].items():
                            print(k, '-', v, 'unit/units.')
                        append_data = dict()
                        for key, value in result_get[2].items():
                            append_data[str(key)] = value
                        new_value = old_money - int(summ)
                        ct.result_dict_balance[user] = new_value

                        ct.cur.execute('DELETE FROM inkasator_check;', )

                        result_list = []
                        for k, v in append_data.items():
                            t = k, v
                            result_list.append(t)

                        for user in result_list:
                            exists = ct.cur.execute('''SELECT banknotes, quantity FROM inkasator_check WHERE banknotes=?''',
                                                 (user[0],)).fetchone()
                            if not exists:
                                ct.cur.execute('''INSERT INTO inkasator_check VALUES (?, ?) ''', user)

                        ct.con.commit()

                        append_trans = f'The client {something} withdrew ${int(summ)} from the account. The rest of money - {new_value}\n'
                        for i in ct.same_dict_trans:
                            if i[0] == something:
                                i[1] = i[1] + append_trans

                        for j in ct.same_dict_trans:
                            ct.result_trans_list.append(tuple(j))

                        ct.cur.execute('DELETE FROM transactions;', )

                        for user in ct.same_dict_trans:
                            exists = ct.cur.execute('''SELECT username, trans FROM transactions WHERE username=?''',
                                                 (user[0],)).fetchone()
                            if not exists:
                                ct.cur.execute('''INSERT INTO transactions VALUES (?, ?) ''', user)

                        ct.con.commit()

                        result = f"${new_value} left in your account"
                        print(' ')
                        print(result)

                        user_balance_result_list = []
                        for k, v in ct.result_dict_balance.items():
                            t = k, v
                            user_balance_result_list.append(t)

                        ct.cur.execute('DELETE FROM users_balance;', )

                        for user in user_balance_result_list:
                            exists = ct.cur.execute('''SELECT username, balance FROM users_balance WHERE username=?''',
                                                 (user[0],)).fetchone()
                            if not exists:
                                ct.cur.execute('''INSERT INTO users_balance VALUES (?, ?) ''', user)

                        ct.con.commit()
                        flag_main = True
                        while flag_main == True:
                            try:
                                back = int(
                                    input("Press '1' if you want to exit, '2' if you want to return to the main menu: "))
                                if back == 1:
                                    flag_main = False
                                    return
                                elif back == 2:
                                    flag_main = False
                                    return self.__main_func(something)
                                elif back < 1 or back > 2:
                                    raise MyTypeError('number')
                            except MyTypeError as Mte:
                                print(
                                    f'Error: Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu!')
                            except:
                                print(
                                    'Error: Enter a number in the range from 1 to 2, example(2) if you want return to the main menu!')

                    elif result_get[0] == 2:
                        print(
                            "Error: We can't give you that amount, we don't have the banknotes you need, try another amount!")

            except ExceptionValue as ExV:
                print(f"Error: {ExV.text} must enter 'Y' or 'N'. ")
            except:
                print(f'Error: You must enter a positive number!')


    def __trans_func(self, user):
        flag = True
        while flag == True:
            try:
                print("Your transactions: ")
                if len(ct.result_trans_list) == 0:
                    for i in ct.same_list_transactions:
                        if i[0] == user:
                            print(i[1])
                elif len(ct.result_trans_list) != 0:
                    for i in ct.result_trans_list:
                        if i[0] == user:
                            print(i[1])

                back = int(input("Press '1' if you want to exit, '2' if you want return to the main menu: "))
                if back == 1:
                    print('Thank you! Good luck :)')
                    flag = False
                elif back == 2:
                    flag = False
                    return self.__main_func(user)
                elif back < 1 or back > 2:
                    raise MyTypeError('number')
            except MyTypeError as Mte:
                print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
            except:
                print('You must choose a number. Please enter 1 or 2, example(1) if you want exit')

class MainAdmin(ExchangeRates):
    def __init__(self, login):
        self.login = login

        self.__ink_main_func(self.login)

    def __ink_main_func(self, result):
        print('Admin menu'.center(30, ' '))
        print('1. Check balance of money')
        print('2. Cash in')
        print('3. Cash out')
        print('4. Check users last transaktions')
        print('5. See the current exchange rate')
        print('6. Exit')
        ink_flag = True
        while ink_flag == True:
            try:
                ink_main_input = int(input("Select the desired operation. Enter from 1 to 5: "))
                if ink_main_input < 1 or ink_main_input > 6:
                    raise MyTypeError('number')
                ink_flag = False

                if ink_main_input == 1:
                    self.__ink_check_balance()
                elif ink_main_input == 2:
                    self.__ink_cashin_money(result)
                elif ink_main_input == 3:
                    self.__ink_cashout_money(result)
                elif ink_main_input == 4:
                    self.__ink_transactions(result)
                elif ink_main_input == 5:
                    self.check_kurs()
                elif ink_main_input == 6:
                    return

            except MyTypeError as Mte:
                print(f'Enter a {Mte.text} in the range from 1 to 5, example(3)')

    def __ink_check_balance(self):
        for k, v in ct.result_dict.items():
            print(k, '-', v, 'units.')
        x = int(input("If you wish exit '1', if return to the main menu press '2': "))
        flag2 = True
        while flag2 == True:
            try:
                if x == 1:
                    return
                if x == 2:
                    self.__ink_main_func(self.login)
                flag2 = False
                if x < 1 or x > 2:
                    raise MyTypeError('number')
            except MyTypeError as Mte:
                print(
                    f'Error: Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu!')


    def __ink_cashin_money(self, result):
        something = result
        flag = True
        while flag == True:
            try:
                banknote = input("Enter one of this banknotes: 1000, 500, 200, 100, 50, 20, 10. (example: 500): ")
                if (banknote in ct.result_dict) == False:
                    raise MyTypeError('banknote')
                quantity = int(input("Enter a quatity of banknotes, (example: 120): "))
                first_quantity = ct.result_dict[banknote]
                result_quantity = first_quantity + quantity
                ct.result_dict[banknote] = result_quantity

                result_list = []
                for k, v in ct.result_dict.items():
                    t = k, v
                    result_list.append(t)

                ct.cur.execute('DELETE FROM inkasator_check;', )

                for user in result_list:
                    exists = ct.cur.execute('''SELECT banknotes, quantity FROM inkasator_check WHERE banknotes=?''',
                                         (user[0],)).fetchone()
                    if not exists:
                        ct.cur.execute('''INSERT INTO inkasator_check VALUES (?, ?) ''', user)

                ct.con.commit()

                x = int(input("If you wish to continue press '1', if to exit to the main menu press '2': "))
                flag2 = True
                while flag2 == True:
                    try:
                        if x == 1:
                            self.__ink_cashin_money(result)
                        if x == 2:
                            self.__ink_main_func(something)
                        flag2 = False

                        if x < 1 or x > 2:
                            raise MyTypeError('number')
                    except MyTypeError as Mte:
                        print(
                            f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')

                flag = False

            except MyTypeError as Mte:
                print(f'Error: You have entered the wrong {Mte.text}. Try again ')
            except ValueError:
                print(f'Error: Enter how many banknotes you wish to deposit, example(50)')


    def __ink_cashout_money(self, result):
        flag = True
        while flag == True:
            try:
                banknote = input(
                    "Enter one of these notes you wish to withdraw: 1000, 500, 200, 100, 50, 20, 10. (example: 500): ")

                if (banknote in ct.result_dict) == False:
                    some = input(
                        "Error: Now we don't have that banknote at our ATM. Please press 'Y' to check balance of money, 'N' if not: ")
                    if some == 'Y':

                        for k, v in ct.result_dict.items():
                            print(k, '-', v, 'units.')
                        continue
                    elif some == 'N':
                        continue
                    else:
                        continue

                quantity = int(input("Enter a quatity of banknotes (example: 120): "))

                first_quantity = ct.result_dict[banknote]
                if quantity > first_quantity:
                    some = input(
                        "Error: You cannot withdraw more than your balance. Please press 'Y' to check balance of money, 'N' if not: ")
                    if some == 'Y':
                        for k, v in ct.result_dict.items():
                            print(k, '-', v, 'units.')
                        continue
                    elif some == 'N':
                        continue
                    else:
                        continue

                elif quantity <= 0:
                    raise ExceptionValue('Quantity')

                result_quantity = first_quantity - quantity
                ct.result_dict[banknote] = result_quantity

                result_list = []
                for k, v in ct.result_dict.items():
                    t = k, v
                    result_list.append(t)

                ct.cur.execute('DELETE FROM inkasator_check;', )

                for user in result_list:
                    exists = ct.cur.execute('''SELECT banknotes, quantity FROM inkasator_check WHERE banknotes=?''',
                                         (user[0],)).fetchone()
                    if not exists:
                        ct.cur.execute('''INSERT INTO inkasator_check VALUES (?, ?) ''', user)

                ct.con.commit()

                flag2 = True
                while flag2 == True:
                    try:
                        x = int(input("If you wish to continue press '1', if to exit to the main menu press '2': "))
                        if x == 1:
                            self.__ink_cashout_money(result)
                        elif x == 2:
                            self.__ink_main_func(result)
                        elif x < 1 or x > 2:
                            raise MyTypeError('number')
                        flag2 = False

                    except MyTypeError as Mte:
                        print(
                            f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
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


    def __ink_transactions(self, result):
        for i in range(len(ct.same_list_transactions)):
            print(ct.same_list_transactions[i][0])
            print(ct.same_list_transactions[i][1])
            print('---------------------------------------------------------------------------')

        flag2 = True
        while flag2 == True:
            try:
                x = int(input("If you wish exit press '1', if return to the main menu press '2': "))
                if x == 1:
                    return
                if x == 2:
                    self.__ink_main_func(result)

                if x < 1 or x > 2:
                    raise MyTypeError('number')
                flag2 = False
            except MyTypeError as Mte:
                print(f'Enter a {Mte.text} in the range from 1 to 2, example(2) if you want return to the main menu')
            except ValueError:
                print(f'Enter a number in the range from 1 to 2, example(2) if you want return to the main menu')

class SignIn(object):
    @classmethod
    def check_usernames(self):
        for i in range(2, -1, -1):
            my_input1 = input("Enter your login: ")
            my_input2 = input("Enter your password: ")

            for j in ct.same_list_users:
                if j[0] == my_input1 and j[1] == my_input2:
                    return my_input1, j[2]
            if i == 0:
                x = "Thank you! Good luck :)"
                return x
            else:
                print(f"Wrong login or password. Enter again, you have {i} attempt left! ")


def start_project():
    main_result = SignIn.check_usernames()
    for i in ct.same_list_users:
        if main_result[0] == i[0] and main_result[1] == 0:
            user_object = SimpleUser(main_result[0])

        elif main_result[0] == i[0] and main_result[1] == 1:
            admin_object = MainAdmin(main_result[0])

start_project()


