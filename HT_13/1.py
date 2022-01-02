class Calc(object):
    #ініціалізуємо атрибут класу
    last_result = None

    #ініціалізуємо методи
    def addition(self, num_1, num_2):         #метод додавання, результат функції присвоюємо атрибуту класа
        res = num_1 + num_2
        Calc.last_result = res

    def subtraction(self, num_1, num_2):      #метод віднімання, результат функції присвоюємо атрибуту класа
        res = num_1 - num_2
        Calc.last_result = res

    def multiplication(self, num_1, num_2):   #метод множення, результат функції присвоюємо атрибуту класа
        res = num_1 * num_2
        Calc.last_result = res

    def division(self, num_1, num_2):         #метод ділення, результат функції присвоюємо атрибуту класа
        res = num_1 / num_2
        Calc.last_result = res

obj_1 = Calc()
print(obj_1.last_result)

obj_1.subtraction(10, 15)
print(obj_1.last_result)
obj_1.multiplication(10, 15)
print(obj_1.last_result)
