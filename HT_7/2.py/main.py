import math

with open('my_file.txt', 'r+', encoding='utf-8') as file:
    text = file.read()


class MyTypeError(Exception):
    def __init__(self, text):
        self.text = text

class MyZeroError(Exception):
    def __init__(self, text):
        self.text = text



def my_func(text, num):                                          #якщо кількість символа або символів передані в функцію
    try:                                                         #не можуть знаходитись симетрично по центру,
        if num >= len(text) / 2:                                 #то виконується зсув на одну позицію вліво
            raise MyTypeError(num)
        elif num <= 0:
            raise MyZeroError('number')
        result_list = []
        # реалізуємо знаходження центральних елементів файлу
        first_str = '1' * num
        second_str = first_str.center(len(text), 'b')
        x = math.floor(second_str.count('b') / 2)
        result_center = text[x : x + num]
        #----------------------------------------------------

        result_1 = text[:num]
        result_2 = text[-num:]

        result_list.append(result_1)
        result_list.append(result_center)
        result_list.append(result_2)

        return result_list
        
    except MyTypeError as Mye:
        x = f"for this number of characters - {Mye.text}, the length of content in the file is too short, increase the length of content in the file, or decrease the number of characters"
        return x
    except MyZeroError as Mze:
        y = f"you must specify a positive {Mze.text} that is greater than zero"
        return y

print(my_func(text, 2))
