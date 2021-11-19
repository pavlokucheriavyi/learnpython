'''
Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
    Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
    Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''


start_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
finish_list = []

for i in range(0, len(start_list)):
    if len(start_list[i]) != 0:
        finish_list.append(start_list[i])

print(finish_list)
