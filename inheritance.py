class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"May name is {self.name} and I'm {self.age} old.")


class Student(Person):
    pass


class Teacher(Person):
    pass


s1 = Student("Afrah", 25)
s1.show()
t1 = Teacher("Aden", 50)
t1.show()
