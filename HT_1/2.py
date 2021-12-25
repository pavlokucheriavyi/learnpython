'''
Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.
    Test Data :
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    Expected Output :
    {'Black', 'White'}
'''


color_list_1 = input("Write colors of first set (example: Blue, Black, White, ...): ").split(", ")
color_list_2 = input("Write colors of second set (example: Blue, Black, White, ...): ").split(", ")

set1 = set(color_list_1)
set2 = set(color_list_2)

def dif(s1, s2):
    result = s1.difference(s2)
    return result

some = dif(set1, set2)
print(some)
