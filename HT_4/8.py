'''
Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
Тобто, функція приймає два аргументи: список і величину зсуву
(якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
'''

start_list = [1, 2, 3, 4, 5, 8, 10]

def result(result_list, shift):
    if shift > 0:
        x = 0
        while x < shift:
            delete_symbol_1 = result_list.pop(-1)
            result_list.insert(0, delete_symbol_1)
            x += 1
        return result_list

    elif shift < 0:
        y = 0
        while y > shift:
            delete_symbol_2 = result_list.pop(0)
            result_list.append(delete_symbol_2)
            y -= 1
        return result_list

    else:
        return result_list

print(result(start_list, -2))
