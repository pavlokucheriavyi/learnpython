'''
Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте, и False - якщо ні.
'''

my_var = int(input("Enter your number from 0 to 1000: "))

def is_prime(par):
    if par == 0 or par == 1:
        return "It is not a prime number or a composite number"

    else:
        my_list = []
        for i in range(1001):
            if i == 0 or i == 1:
                continue
            elif par % i == 0:
                my_list.append(par)
        if len(my_list) == 1:
            return True
        else:
            return False

print(is_prime(my_var))
