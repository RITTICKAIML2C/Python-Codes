# 🐍 Python Question 1. Difficulty: Beginner
# Topic: Lists
# Problem Statement - Write a program to find the largest number in a list without using the max() function.
# Example: Input - [12, 45, 8, 67, 23], Output - 67
numbers = list(map(int, input("Enter number seperated by spaces: ").split())
largest = numbers[0]
for num in numbers:
  if num > largest:
    largest = num
print("Largest Number:", largest)

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Functions
# Problem Statement - Write a function that checks whether a given string is a palindrome. A palindrome reads the same forwards and backwards.
# Example: Input - madam, Output - True
def is_palindrome(word):
  reverse = word[::-1]
  if word == reverse:
    return True
  else:
    return False
text = input("Enter a string: ")
print(is_palindrome(text))
