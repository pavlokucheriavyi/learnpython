'''
   Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
        Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
        Очікуваний результат, якщо введено "100":
        Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
'''


my_int = input("Enter your number or string: ")
start_list = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
last_list = []

for i in start_list:
    my_list = list(i)
    my_list[-1] = my_int
    last_list.append(tuple(my_list))

print(last_list)