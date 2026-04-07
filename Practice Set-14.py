# 1. Print first and last character of a string.
code = "Python"
print(code[0], code[-1])

# 2. Print character at even index.
code = "Python"
print(code[0:5:2])

code = "Python"
for i in range(0, len(code), 2):
    print(code[i], end = " ")

# 3. Reverse a string 
code = "Python"
print(code[::-1])

code = "Python"
reverse = ""
for i in range(len(code)-1, -1, -1):
    reverse = reverse + code[i]
print(reverse)

# 4. Count Vowels in a string.
code = "Education"
char = "aeiouAEIOU"
count = 0
for char in code:
    if char in "aeiouAEIOU":
        count += 1
print(count)

# 5. Check palindrome string 
code = "madam"
reverse = code[::-1]
if code == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# 6. Count how many time a character appears 
string = "Programming"
char = "g"
count = 0
for c in string:
    if c == char:
        count += 1
print(count)

# 7. Remove spaces from string 
string = "Hello World Python"
print(string.replace(" ", ""))

# 8. Capitalize first letter of every word
string = "i love python"
print(string.title())

# 9. Find length without using length
string = "Programming"
count = 0
for char in string:
        count += 1
print(count)

# 10. Gym Log Formatter
exercise = "Chest Press"
sets = 4
reps = 10
print(f'''Workout Summary
Exercise : {exercise}
Sets     : {sets}
Reps     : {reps}''')
