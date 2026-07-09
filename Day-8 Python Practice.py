# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Inheritance
# Problem Statement : Create a class Animal with a method sound() that prints "Animals make sounds.". Create another class Dog that inherits from Animal and has a method bark() that prints "Dog barks.". Create an object of the Dog class and call both methods.
# Example Output - Animals make sounds, Dog barks.
class Animal:
    def sound(self):
        print("Animals make sounds.")
class Dog(Animal):
    def bark(self):
        print("Dog barks.")
dog = Dog()
dog.sound()
dog.bark()

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Inheritance + Constructors
# Problem Statement - Create a class Person with attributes name and age. Create a class Student that inherits from Person and adds one more attribute course. Print all three details.
# Example : Input - Name = Rahul, Age = 20, Course = Python
# Output - Name: Rahul, Age: 20 Course: Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
student = Student(name, age, course)
student.display()
