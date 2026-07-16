# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Functions as Arguments
# Problem Statement : Write a program where one function is passed as an argument to another function. Create a function greet() that prints "Good Morning!". Create another function message(func) that calls the function passed to it.
# Example Output - Good Morning!
def greet():
    print("Good Morning!")
def message(func):
    func()
message(greet)

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Decorators
# Problem Statement : Create a decorator that prints: Before Function before executing a function and After Function after executing the function.
# Use it with a function that prints: Welcome to Python
# Expected Output : Before Function - Welcome to Python, After Function
def decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper
@decorator
def display():
    print("Welcome to Python")
display()
