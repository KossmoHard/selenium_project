# class Person:
#     name = "Vlad"
#     age = 20
#     gender = "M"
#
#     def __init__(self, name):
#         self.name = name
#
#     def set(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "Name: {}".format(self.name)
#
#
# class Student(Person):
#     course = 1
#
#     # Переопределение метода set
#     def set(self, name, course):
#         self.name = name
#         self.course = course
#
#     # Переопределение магического метода __str__
#     def __str__(self):
#         return "Name: {} \nCourse: {}".format(self.name, self.course)
#
#
# person1 = Person("Andrey")
# print(person1)
# print("-------------")
#
# person1.set("Alex")
# print(person1)
# print("-------------")
#
# person2 = Student("Andrey")
# print(person2)
# print("-------------")
#
# person2.set("Artur", 3)
# print(person2)
# print("-------------")
# def simple_generator(val):
#    while val > 0:
#        val -= 1
#        yield val
#
# gen_iter = simple_generator(5)
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))

# sample_list = [x * x for x in range(10) if x % 3 == 0]
# # print(sample_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def f(t, x={}, *args, **kwargs):
    return t, x, args, kwargs


print(f(10, {'test': 'test'}, 10, ts="tst"))
