class Person(object):
    def __init__(self, name, age, is_married):
        self.name = name
        self.age = age
        self.is_married = is_married

    def print_name(self):
        return f'User name is - {self.name}'

    def show_age(self):
        return f'User age is - {self.age}'

    def show_all_information(self):
        return f'User name is {self.name}, he is {self.age} years old'

obj_1 = Person('Viktor', 32, True)
obj_1.profession = 'Driver'

obj_2 = Person('Mark', 21, False)
obj_2.profession = 'Manager'

res_var = obj_2.show_all_information()
print(res_var)