'''
Write a script to convert decimal to hexadecimal
    Sample decimal number: 30, 4
    Expected output: 1e, 04
'''


decimal_list = map(int, input("Enter your decimal numbers, example(30, 4, 221, ...): ").split(", "))
hex_list = []

for i in decimal_list:
    hex_list.append(hex(i)[2:])

print("Your hexadecimal numbers are:", ", ".join(hex_list))
