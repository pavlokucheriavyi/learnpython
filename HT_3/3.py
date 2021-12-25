'''
Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
'''


my_var = int(input("Enter your number (1 to 12): "))

def season(num):
    if (num > 0 and num < 3) or num == 12:
        return "Winter"
    elif num >= 3 and num < 6:
        return "Spring"
    elif num >= 6 and num < 9:
        return "Summer"
    else:
        return "Autumn"

result_var = season(my_var)

print(result_var)
