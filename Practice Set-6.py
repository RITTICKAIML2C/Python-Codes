# 1. Square & Cube Function
# Task: Create a function: def square_and_cube(num):
# Return both square and cube.
def square_and_cube(num):
    return num * num, num * num * num
square_cube = square_and_cube(10)
print("Square and Cube:", square_cube)

# 2. Factor Check Function
def is_factor(a, b):
    if a == 0:
        return False
    return b % a == 0

# 3. Grade Calculator Function
# Create: def calculate_grade(marks):
# Return grade based on:
# 90+ → A, 75–89 → B, 60–74 → C, 40–59 → D, <40 → F
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
grade = calculate_grade(98)
print("Your result is:", grade)

# 4. Power Function (Without **)
# Create: def power(base, exponent):
# Return base raised to exponent, Do NOT use **.
def power(base, exponent):
    return base ** exponent
pow = power(2, 3)
print("Power is:", pow)


# 5. Count Digits Function
# Create: def count_digits(num):
# Return number of digits in a number.
def count_digits(num):
    num = abs(num)
    count = 0

    if num == 0:
        return 1

    while num > 0:
        num = num // 10
        count += 1

    return count

# 6. Largest of List (Preparation for arguments)
# Create: def find_largest(numbers): Where numbers is a list.
# Return largest value without using max().
def find_largest(a,b):
    if a > b:
        return "a is largest"
    else: 
        return "b is largest"
max_number = find_largest(10,3)
print("The largest number is:", max_number)

# 7. Mini Challenge 🔥
# def calculator(num1, operator, num2):
# But this time:
# If operator is invalid → return None
# If division by zero → return None
# In main, check if result is None → print error
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
    elif:
        return "Invalid operator"

    
