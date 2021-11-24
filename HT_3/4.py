'''
Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
обробляє повернутий ними результат та також повертає результат.
Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
'''


def func_1(x, y):
    return x * y

def func_2(x, y):
    return x + y

def func_3(x, y):
    return x // y

def func_result():
    my_var_1 = func_1(1, 2)
    my_var_2 = func_2(10, 12)
    my_var_3 = func_3(-5, 8)

    return my_var_1 - my_var_2 - my_var_3


result_var = func_result()
print(result_var)
