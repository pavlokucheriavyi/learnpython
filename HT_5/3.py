'''
На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except
 '''

my_list = [["Pasha", "qwerty123"], ["Vitya", "Vityayrjgfj"], ["Natasha", "kleop"], ["maksim", "MAKSXO1998"], ["Dima", "Dimasik20"], ["vovka", "asdasdfadga2"]]

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
        result_var_1 = f"Your length of username = {Usex.lenght}, is not in the range of 3 to 50. Re-enter again please"
        return result_var_1
    except PasswordExceptionIsDigit as PassDigit:
        result_var_2 = f'The password must be at least 8 characters long and must contain at least one number. Your password - "{PassDigit.digit}". Re-enter again please'
        return result_var_2
    except IsUpperUserNameException as Iue:
        result_var_3 = f'The username must begin with a capital letter, your username is - "{Iue.username}"'
        return result_var_3
    else:
        result_var_4 = 'OK'
        return result_var_4

def result_function(list_1):
    for i in list_1:
        function_result_var = my_func(i[0], i[1])
        print("Name:", i[0], "\nPassword:", i[1], "\nStatus:", function_result_var, "\n---------------")

result_function(my_list)
