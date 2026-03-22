# 1. Write a program to input student name and marks of 3 subject and print name and percentage
name = input("Enter students name: ")
marks_maths = input("Enter marks in Maths (out of 100): ")
marks_physics = input("Enter marks in Physics (out of 100): ")
marks_chemistry = input("Enter marks in Chemistry (of out 100): ")
percentage_student = ((int(marks_maths) + int(marks_physics) + int(marks_chemistry)) / 300) * 100
print(f"Student name is: {name} and percentage is: {percentage_student} %.")

# 2. Write a python program that collects multiple type of data from user input, store them in a dictionary and print out the collected data.
user_data = {}

user_data['name'] = input("Enter you name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter you height in cm: "))
user_data['student'] = input("Are you a student (yes/no): ")

print(user_data)
