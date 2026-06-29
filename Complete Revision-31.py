# 1. Positive, Negative or Zero
# Take a number from user and print: "Positive", "Negative", "Zero"
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print(f"{number} is Zero.")

# 2. Even or Odd
Take an integer and print: "Even" or "Odd"
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

# 3. Largest of Two Numbers
Take two numbers and print the larger one.
If equal, print: "Both are equal"
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
if number1 > number2:
    print(f"{number1} is larger than {number2}")
elif number2 > number1: 
    print(f"{number2} is larger than {number1}")
else: 
    print(f"{number1} and {number2} both are equal")

# 4. Voting Eligibility
Take age as input.
If age ≥ 18 → Eligible, Else → Not Eligible
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are eligible to vote!!")
else:
    print("You are not eligible to vote!!")

# 5. Divisibility Check
# Take a number.
# Print: "Divisible by 3", "Divisible by 5", "Divisible by both", "Not divisible by 3 or 5"
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisble by both 3 and 5.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3.")
elif number % 5 == 0:
    print(f"{number} is by 5")
else: 
    print(f"{number} is not divisible by 3 or 5.")

# 6. Grade Calculator. Take marks (0–100).
# Print grade: 90+ → A, 75–89 → B, 60–74 → C, 40–59 → D, Below 40 → Fail
marks = int(input("Enter your marks (out of 100): "))
if marks >= 90: 
    print("Grade A")
elif marks >= 75 and marks < 90: 
    print("Grade B")
elif marks >= 60 and marks < 75:
    print("Grade C")
elif marks >= 40 and marks < 60: 
    print("Grade D")
else: 
    print("Grade F")

# 7. Calculator
# Take: number1, operator (+, -, *, /), number2
# Perform operation using conditionals.
number1 = int(input("Enter number 1: "))
operator = input("Choose an operator (+, -, *, /): ") 
number2 = int(input("Enter number 2: "))
if operator == "+":
    print(f"Sum of {number1} and {number2} is {number1 + number2}") 
elif operator == "-":
    print(f"Difference of {number1} and {number2} is {number1 - number2}") 
elif operator == "*":
    print(f"Product of {number1} and {number2} is {number1 * number2}")
elif operator == "/":
    if number2 == 0:
        print("Division by zero not allowed")
    else:
        print(number1 / number2)
else: 
    print("Please provide correct operator.")

# 8. Character Type Checker. Take one character from user.
# Check if it is: Uppercase letter, Lowercase letter, Digit, Special character
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print("Uppercase letter")
elif 'a' <= ch <= 'z':
    print("Lowercase letter")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special character")

# 9. Triangle Validity. Take 3 angles. Check whether triangle is valid.
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))
if angle1 > 0 and angle2 > 0 and angle 3> 0 and (angle1 + angle2 + angle3 == 180):
    print("It is a Valid Triangle !!")
else:
    print("Not a Valid Triangle !!")

# 10. Salary Bonus System. Take salary and years of experience.
# Rules: If experience ≥ 5 years:
#           If salary < 50000 → 10% bonus
#           Else → 5% bonus
#        Else:
#            No bonus
# Print final salary.
salary = int(input("Enter your salary: "))
experience = int(input("Enter you experience: "))
if experience >= 5: 
    if salary < 50000:
        print(f"10% bonus on {salary} with {experience} year experience i,e {(0.1*salary) + salary}")
    else: 
        print(f"5% bonus on {salary} with {experience} year experience i,e {(0.05*salary) + salary}")
else:
    print("No bonus for you!!")

# 11. Electricity Bill. Units consumed:
# First 100 units → ₹5 per unit
# Next 100 → ₹7 per unit
# Above 200 → ₹10 per unit
# Calculate total bill.
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
print("Total bill:", bill)


# 12. Admission System (Improved Version)
# Take: Maths, Physics, Chemistry
# Rules: Minimum criteria: 60 in each subject
# Total ≥ 200 OR (Math + Physics ≥ 150)
# Check eligibility correctly using proper grouping.
math_marks = int(input("Enter marks in Maths (out of 100): "))
phy_marks = int(input("Enter marks in Physics (out of 100): "))
chem_marks = int(input("Enter marks in Chemistry (out of 100): "))
total_marks = math_marks + phy_marks + chem_marks
if ((math_marks >= 60 and phy_marks >= 60 and chem_marks >= 60) and total_marks >= 200) or (math_marks + phy_marks >= 150):
   print("Eligible for admission!!")
else: 
    print("Not eligible for admission !!") 
