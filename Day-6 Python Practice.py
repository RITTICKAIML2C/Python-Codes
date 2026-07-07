# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Exception Handling
# Problem Statement - Write a program that asks the user to enter two numbers and prints their division. If the second number is 0, print "Cannot divide by zero." instead of showing an error.
# Example 1 : Input - 10, 2, Output - 5.0
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Answer =", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Modules
# Problem Statement - Write a program that uses the math module to find: Square root of a number, Power of a number
# Example: Input - 25, 2, 5, Output - Square Root = 5.0, Power = 32.0
import math
number = int(input("Enter a number: "))
print("Square Root =", math.sqrt(number))
base = int(input("Enter base: "))
power = int(input("Enter power: "))
print("Power =", math.pow(base, power))
