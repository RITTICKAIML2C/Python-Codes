# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Sets
# Problem Statement - Write a program to remove duplicate elements from a list and print the unique elements.
# Example : Input - 1 2 3 2 4 5 1 6, Output - {1, 2, 3, 4, 5, 6}
numbers = list(map(int, input("Enter numbers: ").split()))
unique_numbers = set(numbers)
print(unique_numbers)

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Loops
# Problem Statement - Write a program to print the multiplication table of a given number from 1 to 10.
# Example : Input - 5
number = int(input("Enter a number: "))
for i in range(1, 11):
  print(number, "x", i, "=", number * i)
