'''
    Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор,
    який буде вертати значення з цієї послідовності,
    при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
'''

my_list = [1, 2, 3, 4, 5, 6]

def my_func(some_list):
    my_gen = (x for x in some_list)
    some = True
    try:
        while some == True:
            print(next(my_gen))
    except:
        return

def generator(list_1):
    while True:
        my_func(list_1)

generator(my_list)
