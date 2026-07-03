# 🐍 Python Question 1
# Difficulty: Beginner, Topic: Dictionaries
# Problem Statement : Write a program to count how many times each character appears in a given string.
# Example : Input - apple, Output - {'a': 1, 'p': 2, 'l': 1, 'e': 1}
text = input("Enter a string: ")
count = {}
for letter in text:
  if letter in count: 
    count[letter] = count[letter] + 1
  else:
    count[letter] = 1
print(count)

# 🐍 Python Question 2
# Difficulty: Beginner–Intermediate, Topic: Functions
# Problem Statement : Write a function that takes a number as input and returns True if it is a prime number; otherwise, return False.
# Example : Input - 7, Output - True
def is_prime(number):
  if number <= 1:
    return False
  for i in range(2, number):
    if number % i == 0:
      return False
  return True
num = int(input("Enter a number: "))
print(is_prime(num))
    
