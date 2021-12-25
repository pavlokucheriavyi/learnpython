'''
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
 '''

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

class UserException(Exception):
    def __init__(self, lenght):
        self.lenght = lenght

class PasswordExceptionIsDigit(Exception):
    def __init__(self, password_digit):
        self.digit = password_digit

class IsUpperUserNameException(Exception):
    def __init__(self, is_upper_username):
        self.username = is_upper_username


def my_func(username, password):
    list_for_isdigit = []
    try:
        if len(username) < 3 or len(username) > 50:
            raise UserException(len(username))
        if len(password) < 8:
            raise PasswordExceptionIsDigit(password)
        for i in password:
            if i.isdigit():
                list_for_isdigit.append(i)
        if len(list_for_isdigit) == 0:
            raise PasswordExceptionIsDigit(password)
        if username[0].isupper() == False:
            raise IsUpperUserNameException(username)

    except UserException as Usex:
        print(f"Your length of username = {Usex.lenght}, is not in the range of 3 to 50. Re-enter again please")
    except PasswordExceptionIsDigit as PassDigit:
        print(f'The password must be at least 8 characters long and must contain at least one number. Your password - "{PassDigit.digit}". Re-enter again please')
    except IsUpperUserNameException as Iue:
        print(f'The username must begin with a capital letter, your username is - "{Iue.username}"')
    else:
        print(f'Your username {username}')
        print(f'Your password {password}')


my_func(input_username, input_password)
