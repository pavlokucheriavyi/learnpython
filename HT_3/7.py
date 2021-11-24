'''
Ну і традиційно -> калькулятор :)
повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
'''

my_string = input("Enter two numbers and one of the operations: +, -, /, //, *, %. Example:12 % 3 ").split(" ")

def my_function(num_1, operation, num_2):
    if operation == '+':
        return int(num_1) + int(num_2)
    elif operation == '-':
        return int(num_1) - int(num_2)
    elif operation == '/':
        return int(num_1) / int(num_2)
    elif operation == '//':
        return int(num_1) // int(num_2)
    elif operation == '*':
        return int(num_1) * int(num_2)
    else:
        return int(num_1) % int(num_2)

result = my_function(my_string[0], my_string[1], my_string[2])
print(result)
