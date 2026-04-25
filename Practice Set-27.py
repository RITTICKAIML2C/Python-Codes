# 1. Create a class student.
# Attribute : name, marks
# Methods : display() 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Marks", self.marks)
s1 = Student("Rittick", 85)
s1.display()

# 2. Create a class car
# Attributes : brand, speed
# Method : show_speed()
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def show_speed(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed, "km/h")
s1 = Car("Tesla", 180)
s1.show_speed()

# 3. Create Multiple Objects.
# Create 2-3 students and print their data 
class Students:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def display(self):
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("--------------")
s1 = Students("Rittick", 85)
s2 = Students("Soumya", 84)
s3 = Students("Sanya", 83)
s1.display()
s2.display()
s3.display()

# 4. Class Rectangle
# Attributes : length, width
# Methods : area(), perimeter()
class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
r1 = Rectangle(10, 5)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

# 5. Class Bank Account 
# Attributes : name, balance
# Method : deposit(amount), withdraw(amount), display_balance()
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid Deposit Amount!")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw:", amount)
        else:
            print("Insufficient balance!")
    def display_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)
acc1 = BankAccount("Rittick", 1000)
acc1.deposit(500)
acc1.withdraw(1200)
acc1.withdraw(800)
acc1.display_balance()

# 6. Class Employee
# Attributes : name, salary
# Method : increase_salary(percent)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increase_salary(self, percent):
        if percent > 0:
            increase = self.salary * (percent / 100)
            self.salary += increase
            print("Salary increased by:", percent, "%")
        else:
            print("Invalid Percentage !")
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
s1 = Employee("Rittick", 30000)
s1.increase_salary(10)
s1.display()

# 7. Class StudentResultSystem
# Attributes : name, marks
# Methods : is_pass(), grade()
class StudentResultSystem:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_pass(self):
        return self.marks >= 40
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >=75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Result:", "Pass" if self.is_pass() else "Fail")
        print("Grade:", self.grade())
s1 = StudentResultSystem("Rittick", 95)
s1.display()

# 8. Class Calculator 
# Methods: add, sub, multiply, divide
class Calculator:
    def add(self, a, b):
        return a + b
    def substract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Can't divide by zero"
calc = Calculator()
print("Add:", calc.add(10,5))
print("Sub:", calc.substract(10,5))
print("Product:", calc.multiply(10,5))
print("Division:", calc.divide(10,5))

# 9. Class Book
# Attributes : title, author, price
# Method : apply_discount(percent)
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def apply_discount(self, percent):
        if percent > 0:
            increase = self.price * (percent / 100)
            self.price -= increase
            print("Discount:", self.price)
        else:
            print("Invalid Discount")
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
b1 = Book("Python Basics", "Rittick Raj", 500)
b1.apply_discount(10)
b1.display()

# 10. Class GymMember
# Attribute : name, age, weight, height 
# Method : bmi(), category() - underweight, normal, overweight 
class GymMember:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight 
        self.height = height
    def bmi(self):
        return self.weight / (self.height ** 2)
    def category(self):
        bmivalue = self.bmi()
        if bmivalue < 18.5:
            return "Underweight"
        elif bmivalue < 25:
            return "Normal"
        else:
            return "Underweight"
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Weight:", self.weight, "kg")
        print("BMI:", self.bmi())
        print("category:", self.category())
g1 = GymMember("Rittick", 18, 69, 1.75)
g1.display()
