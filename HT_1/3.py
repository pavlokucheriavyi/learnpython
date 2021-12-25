'''
Write a script to sum of the first n positive integers.
'''


num = int(input("Enter a positive number: "))
sum = 0

for i in range(0, num + 1):
    sum = sum + i

print(sum)
