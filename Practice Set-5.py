# 1. Even or Odd Function. Create a function:
# def check_even_odd(num): Return: "Even" or "Odd"
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
even_odd = check_even_odd(10)
print(even_odd)

# 2. Maximum of Three Numbers
# Create: def find_max(a, b, c):
# Return the largest number. No built-in max() allowed
def find_max(a, b, c):
    if (a > b and a > c):
        return "a is largest"
    elif (b > a and b > c):
        return "b is largest"
    else: 
        return "c is largest"
largest_num = find_max(1, 5, 2)
print("Largest Number is:", largest_num)

# 3. Temperature Converter
# Create two functions: def celsius_to_fahrenheit(c):, def fahrenheit_to_celsius(f):
# Return converted values.
# Formula: F = (C × 9/5) + 32
# C = (F − 32) × 5/9
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
fahrenheit = celsius_to_fahrenheit(32)
print("Celsius to Fahrenheit:", fahrenheit)
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
celsius = fahrenheit_to_celsius(122)
print("Fahrenheit to celsius:", celsius)

# 4. Simple Interest Calculator. Create: def calculate_si(principal, rate, time):
# Return simple interest.
# Formula: SI = (P × R × T) / 100
def calculate_si(principal, rate, time):
    return (principal * rate * time) / 100
simple_interest = calculate_si(10000, 2, 3)
print("Simple interest is:", simple_interest )

# 5. Number Analyzer (Function Version)
# Create separate functions: def is_positive(num):, def is_even(num):, def divisible_by_3_and_5(num):
#Each function should return True or False.
# Then call them in main and print proper messages.
# def is_positive(num):
#     if num > 0:
#         return True
#     else: 
#         return False
# positive_num = is_positive(10)
# print("Number is positive ?", positive_num)
def is_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False
even_num = is_even(10)
print("Number is even ?", even_num)
def divisible_by_3_and_5(num):
    if num % 3 == 0 and num % 5 == 0:
        return True
    else:
        return False
divisible = divisible_by_3_and_5(15)
print("Number is divisible by 3 and 5 ?", divisible)

# 6. Challenge Question
# Create a function: def calculator(num1, operator, num2):
# Inside this function: Call add, sub, multiply, divide functions, Return result, Handle invalid operator, Handle division by zero, Now your calculator becomes modular.
# This is real structure.
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b
def calculator(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return "Invalid operator"

    
