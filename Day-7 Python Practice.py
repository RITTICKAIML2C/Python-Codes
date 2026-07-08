# 🐍 Python Question 1, Difficulty: Beginner
# Topic: OOP (Classes & Objects)
# Problem Statement - Create a class named Student.
# Create two attributes: name, marks. Create a method display() that prints the student's name and marks.
# Example : Input - Name = Rohan, Marks = 92, Output - Student Name: Rohan, Marks: 92
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
name = input("Enter name: ")
marks = int(input("Enter marks: "))
student1 = Student(name, marks)
student1.display()

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: OOP (Methods)
# Problem Statement - Create a class named Rectangle. Input length and width. Create a method to calculate the area. Print the area.
# Example: Input - Length = 10, Width = 5, Output - Area = 50
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length = int(input("Enter length: "))
width = int(input("Enter width: "))
rect = Rectangle(length, width)
print("Area =", rect.area())
