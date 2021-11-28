'''
Написати функцію < fibonacci >, яка приймає один аргумент
і виводить всі числа Фібоначчі, що не перевищують його.
'''

my_var = int(input("Enter your number: "))

def fib(num):
    my_list = [0, 1]
    if num == 0:
        return my_list[0]
    elif num == 1:
        return my_list
    a=0
    b=1
    for i in range(num-1):
        b=a+b
        a=b-a
        if b > num:
            break
        my_list.append(b)
    for j in my_list:
        print(j, end = ' ')

fib(my_var)
