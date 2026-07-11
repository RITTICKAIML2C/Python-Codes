# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Encapsulation (Private Variables)
# Problem Statement : Create a class Student, Create a private variable __marks, Create a method set_marks() to assign marks, Create a method get_marks() to display the marks.
# Example : Input - 95, Output - Marks: 95
class Student:
    def __init__(self):
        self.__marks = 0
    def set_marks(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
student = Student()
marks = int(input("Enter marks: "))
student.set_marks(marks)
print("Marks:", student.get_marks())

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Encapsulation + Methods
# Problem Statement : Create a class BankAccount., Private variable __balance, Method deposit(amount), Method withdraw(amount), Method show_balance(), If the withdrawal amount is greater than the balance, print: Insufficient Balance
# Example : Input - Deposit = 5000, Withdraw = 1500
# Output - Balance = 3500
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")
    def show_balance(self):
        print("Balance =", self.__balance)
account = BankAccount()
deposit = int(input("Enter deposit amount: "))
account.deposit(deposit)
withdraw = int(input("Enter withdraw amount: "))
account.withdraw(withdraw)
account.show_balance()
