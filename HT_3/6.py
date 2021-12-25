'''
Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
-> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
'''


my_string = input("Enter your string: ")

def func_1(param_1):
    if len(param_1) >= 30 and len(param_1) <= 50:
        sum_count_of_letters = 0
        sum_count_of_digits = 0
        for i in param_1:
            if i.isalpha():
                sum_count_of_letters += 1
            elif i.isdigit():
                sum_count_of_digits += 1
        print("Lengt:", len(param_1),";", "number of letters:", sum_count_of_letters, ";", "number of digits:", sum_count_of_digits)

    elif len(param_1) < 30:
        result_sum = 0
        last_string = ""
        for j in param_1:
            if j.isdigit():
                result_sum += int(j)
            elif j.isalpha():
                last_string += j
        print("Sum of digits:", result_sum)
        print(last_string)

    else:
        big_ryadok = ''
        for k in param_1:
            if k.isalpha():
                big_ryadok += k.upper()
        print(big_ryadok)

    return

func_1(my_string)
