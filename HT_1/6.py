'''
Write a script to check whether a specified value is contained in a group of values.
    Test Data :
    3 -> [1, 5, 8, 3] : True
    -1 -> (1, 5, 8, 3) : False
'''


my_char = int(input("Enter your number: "))
my_input = map(int, input("Enter your numbers for comparison, example(2, 3, 4, 10, ...): ").split(','))

last_list = list(my_input)
result = my_char in last_list

print(my_char, "-->", last_list, ":", result)
