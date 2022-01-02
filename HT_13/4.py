class Figure(object):
    def __init__(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, color, s, p):
        super().__init__(color)
        self.s = s
        self.p = p

    def print_info(self):
        return f'Color of figure is {self.color}. The area of the figure: {self.s}. The perimeter of the figure: {self.p}.'


class Square(Figure):
    def __init__(self, color, s, p):
        super().__init__(color)
        self.s = s
        self.p = p

    def print_info(self):
        return f'Color of figure is {self.color}.The area of the figure: {self.s}. The perimeter of the figure: {self.p}.'


obj_1 = Oval('Red', 20, 228)

result_var = obj_1.print_info()

print(result_var)
