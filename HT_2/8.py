'''
    Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа,
    а значення для цих ключів - це квадрат ключа.
        Приклад виводу при введеному значенні 5 :
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''


x = int(input("Enter your number: "))
dict_1 = {}

for x in range(x + 1):
    dict_1[x] = x**2

print(dict_1)
