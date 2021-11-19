'''
Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
'''


dict_1 =  {'maksim': 65, 'boris': 90, 'vitya': 64, 'dima': 65, 'natasha': 77}
dict_2 = {}
start_list = []
last_list = []

for k, v in dict_1.items():              #виводимо всі значення словника в окремий список
    start_list.append(v)

for x in start_list:                     #робимо ці значення унікальними та зберігаємо порядок послідовності,
    if x in last_list:                   #зберігаємо в новий список "last_list"
        continue
    else:
        last_list.append(x)

for some in last_list:                   #порівнюємо значення з списка "last_list" зі значеннями початкового словника,
    for key, value in dict_1.items():    #та виводимо результат в кінцевий словник "dict_2"
        if some == value:
            dict_2[key] = value
            break

print(dict_2)
