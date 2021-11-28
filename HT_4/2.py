'''
Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад
у розмірі < a > одиниць строком на < years > років під < percents > відсотків
(кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
Параметр < percents > є необов'язковим і має значення по
замовчуванню < 10 > (10%). Функція повинна принтануть і вернуть суму, яка буде на рахунку.
'''

my_summ_of_money = float(input("Enter the sum of your money: "))
my_year = int(input("Enter your year/years: "))
my_percent = input("Enter your procent, example(15%): ")

def bank(a, years, percents=10):
    percents = float(percents[:-1:])
    for i in range(years):
        a = a + a*(percents/100)
    print("Your result sum of money:", '%.2f' % a)


bank(my_summ_of_money, my_year, my_percent)
