# Parent class
class User:
    # Holds details about user
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Function to show user details
    def show_details(self):
        print("Personal details")
        print("-----------------")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    # Function to allow deposit
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Account balance has been updated: ${self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"Insufficient funds | Balance available is: ${self.balance}")
        else:
            self.balance = self.balance - self.amount
            print(f"Account balance has been updated: ${self.balance}")

    def view_balance(self):
        self.show_details()
        print(f"Account balance is: ${self.balance}")


user1 = Bank("Afrah", 25, "Male")
user1.show_details()
user1.deposit(200)
user1.withdraw(50)
user1.withdraw(100)
user1.view_balance()

