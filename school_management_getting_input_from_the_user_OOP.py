# Parent class
class Person:
    # Holds details about person
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")

    # Function to show user details
    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Child class
class Student(Person):
    def __init__(self):
        super().__init__()
        self.reg_no = input("Enter your registration number: ")
        self.course = input("Enter your the course you are pursuing: ")
        print(" ")
        print("Student details")

    def std_details(self):
        self.show_details()
        print("Registration number: ", self.reg_no)
        print(" ")


class Teacher(Person):
    def __init__(self):
        super().__init__()
        self.department = input("Enter your your department: ")
        self.salary = int(input("Enter your salary: "))
        print(" ")
        print("Teacher details")

    def teacher_details(self):
        self.show_details()
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(" ")


s1 = Student()
s1.std_details()

t1 = Teacher()
t1.teacher_details()
