'''
Користувачем вводиться початковий і кінцевий рік.
Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
'''


first_year = int(input("Enter your first year: "))
second_year = int(input("Enter your second year: "))

for i in range(first_year, second_year + 1):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        print(i)
