'''
Write a script which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
    Sample data : 1, 5, 7, 23
    Output :
    List : [‘1', ' 5', ' 7', ' 23']
    Tuple : (‘1', ' 5', ' 7', ' 23')
'''


my_var = input("Enter your set of numbers, example(1, 3, 5, ...):").split(",")
my_list = list(my_var)
my_tuple = tuple(my_var)

print("List :", my_list)
print("Tuple :", my_tuple)
