'''
Написати функцію < square > ,
яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
'''

import math

my_var = int(input("Enter your side of the square: "))

def square(param):
    p = param * 4
    s = param ** 2
    d = param * math.sqrt(2)
    return p, s, float('%.2f' % d)

print(square(my_var))
