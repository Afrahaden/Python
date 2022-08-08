class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        self.name = input("Enter your name: ")


class Student(Person):
    def __init__(self, name, age, gender, reg_no, course):
        super().__init__(name, age, gender)
        self.reg_no = reg_no
        self.course = course


class Teacher(Person):
    def __init__(self, name, age, gender, department, no_courses):
        super().__init__(name, age, gender)
        self.department = department
        self.no_course = no_courses

