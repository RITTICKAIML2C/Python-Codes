# 🐍 Python Question 1. Difficulty: Beginner
# Topic: Strings
# Problem Statement
# Write a function that takes a string and returns the number of vowels (a, e, i, o, u) present in it. Both uppercase and lowercase vowels should be counted.
# Example: Input - "Hello World"
# Output - 3
def count_vowels(s):
  vowels = "aeiouAEIOU"
  count = 0
  for ch in s:
    if ch in vowels:
      count += 1
  return count 
text = input("Enter a string: ")
print(count_vowels(text))

# 🐍 Python Question 2. Difficulty: Easy–Intermediate
# Topic: Lists
# Problem Statement
# Given a list of integers, return a new list containing only the even numbers while preserving their order.
# Example: Input - [2, 5, 8, 7, 10]
# Output - [2, 8, 10]
def even_numbers(lst):
    result = []
    for num in lst:
      if num % 2 == 0:
        result.append(num)
    return result
numbers = list(map(int, input().split()))
print(even_numbers(numbers))
