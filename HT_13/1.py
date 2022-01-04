class Calc(object):
    """
    a Class used for arithmetic operations on two numbers
    ...

    Attributes
    ----------
    last_result : NonType
        this variable is used to record the result of an arithmetic operation.
        Changes with every method call

    Methods
    ----------
    addition(num_1, num_2)
        Return the result of the sum of two numbers
    subtraction(num_1, num_2)
        Return the result of subtracting two numbers
    multiplication(num_1, num_2)
        Return the result of multiplying two numbers
    division(num_1, num_2)
        Return the result of dividing two numbers

    """
    last_result = None


    def addition(self, num_1, num_2):
        """
        Function return the result of the sum of two numbers
        :param num_1: first_number
        :param num_2: second_number
        :return: sum of 'num_1' and 'num_2'
        """
        res = num_1 + num_2
        Calc.last_result = res
        return res

    def subtraction(self, num_1, num_2):
        """
        Function return the result of subtracting two numbers
        :param num_1: first_number
        :param num_2: second_number
        :return: substraction of 'num_1' and 'num_2'
        """
        res = num_1 - num_2
        Calc.last_result = res
        return res

    def multiplication(self, num_1, num_2):
        """
        Function return the result of multiplying two numbers
        :param num_1: first_number
        :param num_2: second_number
        :return: multiplication of 'num_1' and 'num_2'
        """
        res = num_1 * num_2
        Calc.last_result = res
        return res

    def division(self, num_1, num_2):
        """
        Function return the result of dividing two numbers
        :param num_1: first_number
        :param num_2: second_number
        :return: division of 'num_1' and 'num_2'
        :raise ZeroDivisionError: if the second number is zero.
            Cannot be divided by zero

        """
        if num_2 == 0:
            raise ZeroDivisionError('You cannot divide by 0')

        res = num_1 / num_2
        Calc.last_result = res
        return res

obj_1 = Calc()

res_var = obj_1.division(15, 5)
print(res_var)

print(help(obj_1))