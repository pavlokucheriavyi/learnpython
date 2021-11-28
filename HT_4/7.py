'''
Написати функцію, яка приймає на вхід список
і підраховує кількість однакових елементів у ньому.
'''

my_input = input("Enter your list, example(1, 2, 3, 4, 1, 3): ").split(", ")

def my_count(m_list):
    last_list = []

    for i in m_list:
        if i in last_list:
            continue
        else:
            last_list.append(i)

    for j in last_list:
        print(j, "-", m_list.count(j), "times")


my_count(my_input)
