class Employee:

    def __init__(self):
        self.first = input("Enter your first name: ")
        self.last = input("Enter your first name: ")
        self.pay = int(input("How much do you make per hour: "))
        self.hours = int(input("How many hours do you have: "))

    def show_details(self):
        print(f"First name: {self.first}")
        print(f"Last name: {self.last}")
        print(f"Pay per hour: {self.pay}")
        print(f"Hours you have: {self.hours}")


my_employee = Employee()
my_employee.show_details()
