'''
Ну і традиційно -> калькулятор :)
повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
'''


def my_function():
    some = True
    while some == True:
        try:
            my_string = input("Enter two numbers and one of the operations: +, -, /, //, *, %. Example(12 % 3) ").split(" ")
            if my_string[1] == '+':
                return int(my_string[0]) + int(my_string[2])
            elif my_string[1] == '-':
                return int(my_string[0]) - int(my_string[2])
            elif my_string[1] == '/':
                return int(my_string[0]) / int(my_string[2])
            elif my_string[1] == '//':
                return int(my_string[0]) // int(my_string[2])
            elif my_string[1] == '*':
                return int(my_string[0]) * int(my_string[2])
            else:
                return int(my_string[0]) % int(my_string[2])
            some = False
        except ZeroDivisionError:
            print("You cannot divide by zero, try again!!!")


result = my_function()
print(result)
