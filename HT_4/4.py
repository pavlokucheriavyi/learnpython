'''
Написати функцію < prime_list >,
яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона.
'''

num_1 = int(input("Enter number of start your range: "))
num_2 = int(input("Enter number of finish your range: "))

def prime_list(n1, n2):
    my_list = []
    result_list = []
    for i in range(n1, n2 + 1):
        if i == 0 or i == 1:
            continue
        for j in range(1, n2 + 1):
            if i % j == 0:
                my_list.append(i)
        if my_list.count(i) == 2:
            result_list.append(i)
    return result_list

print(prime_list(num_1, num_2))
