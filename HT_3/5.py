'''
Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї),
   пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при
   нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
'''


x = int(input("Enter your 'x' number: "))
y = int(input("Enter your 'y' number: "))

def result_function(num_1, num_2):
    if num_1 > num_2:
        result_1 = print(num_1, "is greater than", num_2, "on", num_1 - num_2)
        return result_1
    elif num_1 < num_2:
        result_2 = print(num_2, "is greater than", num_1, "on", num_2 - num_1)
        return result_2
    else:
        result_3 = print(num_1, "is equal to", num_2)
        return result_3


result_function(x, y)
