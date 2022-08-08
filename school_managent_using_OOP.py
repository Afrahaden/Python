# Parent class
class Person:
    # Holds details about person
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Function to show user details
    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Child class
class Student(Person):
    def __init__(self, name, age, gender, reg_no, course):
        super().__init__(name, age, gender)
        self.reg_no = reg_no
        self.course = course
        print(" ")
        print("Student details")

    def std_details(self):
        self.show_details()
        print("Registration number: ", self.reg_no)


class Teacher(Person):
    def __init__(self, name, age, gender, department, salary):
        super().__init__(name, age, gender)
        self.department = department
        self.salary = salary
        print(" ")
        print("Teacher details")

    def teacher_details(self):
        self.show_details()
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


s1 = Student("Aden", 22, "Male", "SCT221-0475/2019", "BIT")
s1.std_details()
t1 = Teacher("Abdikadir", 43, "Male", "Information Technology", 75000)
t1.teacher_details()
s2 = Student("Aisha", 19, "Female", "SCT221-0212/2020", "CS")
s1.std_details()