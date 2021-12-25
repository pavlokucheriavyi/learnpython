'''
Вводиться число.
Якщо це число додатне, знайти його квадрат, якщо від'ємне,
збільшити його на 100, якщо дорівнює 0, не змінювати.
'''

my_var = int(input("Enter your number: "))

def check(num):
    if num > 0:
        res_1 = print("Result:", num**2)
        return res_1
    elif num < 0:
        res_2 = print("Result:", num + 100)
        return res_2
    else:
        res_3 = print("Result:", num)
        return res_3

check(my_var)
