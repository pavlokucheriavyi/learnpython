'''
    Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
    P.S. Повинен вертатись генератор.
'''

class NotEnoughError(Exception):
    def __init__(self, text):
        self.text = text

class StepZeroWarningError(Exception):
    def __init__(self, text):
        self.text = text

class TooManyElementsError(Exception):
    def __init__(self, text):
        self.text = text

def my_range(*args):
    try:
        if len(args) == 3:
            num_1 = args[0]
            num_2 = args[1]
            step = args[2]
        elif len(args) == 2:
            num_1 = args[0]
            num_2 = args[1]
            step = 1
        elif len(args) == 1:
            num_1 = 0
            num_2 = args[0]
            step = 1
        elif len(args) == 0:
            raise NotEnoughError("some")
        else:
            raise TooManyElementsError('some')


        if step == 0:
            raise StepZeroWarningError("some")


        while num_1 < num_2:
            yield num_1
            num_1 += step

    except TooManyElementsError as Tmee:
        print("TooManyElementsError: too many elements for the 'range' function. Should not be more than 3")
    except StepZeroWarningError as Szwe:
        print("StepZeroWarningError: the step of the 'range' function cannot be zero")
    except NotEnoughError as Nee:
        print("NotEnoughError: the 'range' function must accept at least one element")


list_of_range_function = my_range()
for elem in list_of_range_function:
    print(elem)
