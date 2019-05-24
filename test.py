class Person:
    name = "Vlad"
    age = 20
    gender = "M"

    def __init__(self, name):
        self.name = name

    def set(self, name):
        self.name = name

    def __str__(self):
        return "Name: {}".format(self.name)


class Student(Person):
    course = 1

    # Переопределение метода set
    def set(self, name, course):
        self.name = name
        self.course = course

    # Переопределение магического метода __str__
    def __str__(self):
        return "Name: {} \nCourse: {}".format(self.name, self.course)


person1 = Person("Andrey")
print(person1)
print("-------------")

person1.set("Alex")
print(person1)
print("-------------")

person2 = Student("Andrey")
print(person2)
print("-------------")

person2.set("Artur", 3)
print(person2)
print("-------------")

