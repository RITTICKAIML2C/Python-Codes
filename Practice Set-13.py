# 1. Basic formatted Output
# Create variables: name, age, city. Print this sentence using f-string:

name = "Rittick"
age = 18
city = "Kolkata"

# F-string
print(f"My name is {name}, I am {age} years old and I live in {city}")

# % operator 
print("My name is %s and I am %d years old and I live in %s"%(name, age, city))

# .format()
print("My name is {} and I am {} years old and I live in {}".format(name, age, city))

# 2. Price formatter
item = "Protein Bar"
price = 120
quantity = 3
print(f"You bought {quantity} {item}(s). Total cost = {price * quantity}")

# 3. Escape character practice
print("Python is fun!")
print("Let's learn \"Python\" together.")
print("Path: C:\\Users\\Student\\Python")

# 4. Multi-line Gym Log
# Store your workout log in a variable and print it 
workout_log = """Workout Log
-----------
Exercise : Chest Press
Sets     : 4
Reps     : 12
"""
print(workout_log)

# 5. Temperature report
city = "Kolkata"
temp = 32.45678
print(f"Temperature in {city} is {temp:.2f}")

# 6. Alignment Problem


# 7. Percentage formatter
marks = float(input("Enter your marks: "))
total = float(input("Enter your total marks: "))
print(f"You scored {(marks / total) * 100:.2f}")

# 8. Escape Sequence Thinking 
print('''She said, "Python is amazing!"''')

# 9. Debug this 
name = "Rittick"
age = 18
print("My name is {} and I am {} years old" %(name,age)) # Instead of this - you used {} it is for .format and f-strings not for % formatting.
print(f"My name is {name} and I am {age} years old") # It should be this.

# 10. Mini Challenge
name = input("Enter name: ")
roll = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))
total = int(input("Enter total marks: "))
print(f'''Student Report
Name    : {name}
Roll    : {roll}
Score   : {marks/total}
Percent : {(marks/total) * 100}''')
