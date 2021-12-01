'''
    Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
    P.S. Повинен вертатись генератор.
'''
class StepZeroWarningError(Exception):
    pass

def my_range(num_1, num_2, step=1):
    if step == 0:
        raise StepZeroWarningError(step)

    my_list = [num_1]
    while num_1 < num_2:
        num_1 += step
        my_list.append(num_1)
    my_gener = (x for x in my_list)
    return my_gener

list_of_range_function = my_range(1, 10, 3)
print(next(list_of_range_function))
print(list_of_range_function.__next__())
