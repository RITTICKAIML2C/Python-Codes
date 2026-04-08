# 1. User Info Formatter.
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")
print(f"""User Profile
-------------
Name : {name}
Age  : {age}
City : {city}""")

# 2. Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else: 
    print(f"{num} is Odd.")

# 3. Multiplication Table Generator
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 4. Reverse a string 
code = "Python"
reverse = ""
for i in range(len(code)-1, -1, -1):
    reverse = reverse + code[i]
print(reverse)

# 5. Count vowels in a Sentence
code = "I love Python Programming"
char = "aeiouAEIOU"
count = 0
for char in code:
    if char in "aeiouAEIOU":
        count += 1
print(count)

# 6. Palindrome checker
code = "racecar"
reverse = code[::-1]
if reverse == code:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7. Remove all spaces from a string 
code = "I love Python"
print(code.replace(" ", ""))

# 8. Character Frequency Counter
string = "Programming"
char = "g"
count = 0
for c in string:
    if c == char:
        count += 1
print(f"{char} appears {count} times")

# 9. Longest word in string.
s = input("Enter a sentence: ")
words = s.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

# 10. Gym Workout Logger
exercise = input("Exercise performed: ")
sets = int(input("Number of sets performed: "))
reps = int(input("Reps performed: "))
weight = int(input("Weight you lifted: "))
print(f"""Workout Log
--------------
Exercise : {exercise}
Sets     : {sets}
Reps     : {reps}
Weight   : {weight} kg""")
