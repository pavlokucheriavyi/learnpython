class Figure(object):
    color = 'white'

    def change(self, new_color):
        self.color = new_color

class Oval(Figure):
    def __init__(self, S, P):
        self.s = S
        self.p = P

    def print_sizes(self):
        return f'The area of the figure = {self.s}. The perimeter of the figure = {self.p}. The color of the figure - {self.color}.'

class Square(Figure):
    def __init__(self, S, P):
        self.s = S
        self.p = P

    def print_sizes(self):
        return f'The area of the figure = {self.s}. The perimeter of the figure = {self.p}. The color of the figure - {self.color}.'


obj_2 = Oval(20, 18)
obj_2.change('Yellow')

obj_1 = Square(11, 11)

print(obj_2.print_sizes())
print(obj_1.print_sizes())