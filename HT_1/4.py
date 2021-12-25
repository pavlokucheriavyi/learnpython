'''
Write a script to concatenate N strings.
'''


q = int(input("Enter the number of strings: "))
sum = ""

for i in range(0, q):
    my_str = input("Enter the string: ")
    sum = sum + my_str

print(sum)
