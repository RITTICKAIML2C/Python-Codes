# 1. Number Category. Take a number and print: "Single digit", "Double digit","Triple digit", "More than 3 digits"
number = (int(input("Enter a number: ")))
num = abs(number)
if num < 10:
    print("Single digit")
elif num < 100:
    print("Double digit")
elif num < 1000:
    print("Triple digit")
else:
    print("More than 3 digits")

# 2. Smallest of Three Numbers
# Take three numbers. Print the smallest. If any two are equal, handle properly.
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))
if n1 <= n2 and n1 <= n3:
    print("n1 is smallest")
elif n2 <= n1 and n2 <= n3:
    print("n2 is smallest")
else:
    print("n3 is smallest")

# 3. Leap Year (Strict Version)
# Rewrite leap year logic but: Reject negative years, Reject year = 0, Only valid positive years allowed
year = int(input("Enter a year: "))
if year <= 0:
    print("Invalid year")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

# 4. Discount Calculator. Take purchase amount:
# ≥ 5000 → 20% discount, 3000–4999 → 10% discount, 1000–2999 → 5% discount, <1000 → No discount
# Print final amount after discount.
amount = int(input("Enter an purchase amount: "))
if amount >= 5000:
    print(f"20% discount {(amount) - (amount * 0.2)}")
elif amount >= 3000 and amount < 5000:
    print(f"10% discount {(amount) - (amount * 0.1)}")
elif amount >= 1000 and amount < 3000:
    print(f"5% discount {(amount) - (amount * 0.05)}")
else: 
    print("No discount")

# 5. ATM Withdrawal System
# Take: Account balance, Withdrawal amount
# Rules: If withdrawal > balance → "Insufficient balance", If withdrawal <= 0 → "Invalid amount", Else deduct and print remaining balance
account_balance = int(input("Enter account balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))
if withdrawal_amount > account_balance:
    print("Insufficient balance")
elif withdrawal_amount <= 0:
    print("Invalid amount")
else:
    print(f"{account_balance - withdrawal_amount} is the remaining balance")

# 6. Take number (1–7)
# Print day name: 1 → Monday, 2 → Tuesday ...7 → Sunday
# If invalid number → print "Invalid day"
number = int(input("Enter a number of days in a week: "))
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6: 
    print("Saturday")
elif number == 7:
    print("Sunday")
else: 
    print("Invalid day")

# 7. Triangle Type Checker. Take 3 sides.
# Check: Valid triangle?. If valid: Equilateral, Isosceles, Scalene
a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a valid triangle")

# 8. Exam Result System
# Take: Marks in 5 subjects
# Rules: If any subject < 35 → Fail, Else: Average ≥ 75 → Distinction, Average ≥ 60 → First Class, Average ≥ 50 → Second Class,Else → Pass
marks1 = int(input("Enter your marks1: "))
marks2 = int(input("Enter your marks2: "))
marks3 = int(input("Enter your marks3: "))
marks4 = int(input("Enter your marks4: "))
marks5 = int(input("Enter your marks5: "))
avg = (marks1 + marks2 + marks3 + marks4 + marks5) / 5
if marks1 < 35 or marks2 < 35 or marks3 < 35 or marks4 < 35 or marks5 < 35:
    print("Fail")
elif avg >= 75:
    print("Distinction")
elif avg >= 60:
    print("1st division")
elif avg >= 50:
    print("2nd division")
else: 
    print("Pass")
