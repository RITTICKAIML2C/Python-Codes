# Conditional statement in Python 

# 1. if statement
# if statement works only for True conditional.
a = 260
b = 108 
if b > a:
    print("b is greater than a")

age = int(input("Enter your age: "))
if age > 19:
    print("You are an adult")

# 2. if-else condtiton 
# else handles False conditions.
temp = 30 
if temp < 25:
    print("It's a cool day.")
else: 
    print("It's a hot day.")

# 3. if-elif-else condition.
# multiple conditions 
marks = int(input("Enter your marks (out of 100): "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else: 
    print("Grade: C")

# 4. Nested if-else Condition.
# if-else inside if-else statement.
# multiple conditions depend on each other.

# Q: Positive, negative and zero. Positive - even/odd
number = int(input("Enter a number: "))
if number > 0: #checking positive number
    if number % 2 == 0: 
        print("This is an even number.")
    else: 
        print("This is an odd number.")
else:
    if number == 0:
        print("The is zero.")
    else: 
        print("The is a negative number.")

# 5. Conditional Expressions (ternary operator)

age = 26 
status = "Major" if age >= 18 else "Minor"
print(status)
