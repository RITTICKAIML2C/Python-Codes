# 1. What is the expected output and reason ?
value = None
if value:
    print("Value is True")
else:
    print("Value is False")
# Ans : Value is False

# 2. Write a simple program to determine if a given year is a leap year using user input
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year  % 400 == 0):
    print(f"{year} is leap year")
else: 
    print(f"{year} is not a leap year")

# 3. Login authentication using conditional statements. Assume you have a predefined username and password
# Write a program that prompt the user to enter a username and password and check whether they match.
# Provide appropriate message for following cases:
# Both username and password are correct
# Username is correct but password is incorrect.
# Username is incorrect.

# TYPE - 1
username = "Rittick@2007"
password = "rittick@2007"
user_name = input("Enter the username: ")
pass_word = input("Enter the password: ")
if (user_name == username) and (pass_word == password):
    print("Both Username and Password are correct")
elif (user_name == username) and (pass_word != password):
    print("Username is correct but password is incorrect")
else: 
    print("Username is incorrect")

# TYPE - 2
username = "Rittick@2007"
password = "rittick@2007"
user_name = input("Enter the username: ")
pass_word = input("Enter the password: ")
if user_name == username:
    if pass_word == password:
        print("Welcome! Login was successful.")
    else:
        print("Incorrect Password!")
else:
    print("Invalid Username!")

# 4. Admission Eligibilty 
# Marks in Maths >= 65, Marks in Phy >= 55, Marks in Chemistry >= 50.
# Total marks in all three subjects >= 180 OR Total marks in Maths and Phy >= 140.

math_marks = int(input("Enter you marks in Maths: "))
phy_marks = int(input("Enter you marks in Phy: "))
chem_marks = int(input("Enter you marks in Chem: "))
total_marks = math_marks + phy_marks + chem_marks
if (
    (math_marks >= 65 and phy_marks >= 55 and chem_marks >= 50) 
    and 
    (total_marks >= 180 or (math_marks + phy_marks >= 140))
):
    print("Student is eligible")
else:
    print("Student is not eligible")
