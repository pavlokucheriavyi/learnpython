class MyClass(object):
    count_obj = 0

    def __init__(self):
        simlpe_var = MyClass.count_obj + 1
        MyClass.count_obj = simlpe_var

obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
obj_4 = MyClass()
obj_5 = MyClass()
obj_6 = MyClass()
obj_7 = MyClass()
obj_8 = MyClass()

print(MyClass.count_obj)
