'''
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>)
   і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
       інакше (<silent> == <False>) - породжується виключення LoginException
'''

class LoginException(Exception):
    pass

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
user_silent_input = int(input("Enter your silent, 1 or 0: "))

def my_func(username, password, silent=False):
    input_list = [username, password]
    my_list = [["Pasha", "qwerty123"], ["Vitya", "Vitya228"], ["Natasha", "kleopatra15"], ["Maksim", "MAKSXO1998"], ["Dima", "Dimasik20"]]
    for i in my_list:
        if i == input_list:
            silent = True
            return True
    if silent == True:
        return False
    else:
        raise LoginException()

print(my_func(username_input, password_input, user_silent_input))
