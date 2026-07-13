# 🐍 Python Question 1, Difficulty: Beginner
# Topic: List Comprehension
# Problem Statement : Given a list of integers, create a new list containing the square of each number using list comprehension.
# Example : Input - 1 2 3 4 5, Output - [1, 4, 9, 16, 25]
numbers = list(map(int, input("Enter numbers: ").split()))
squares = [num * num for num in numbers]
print(squares)

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: List Comprehension with Condition
# Problem Statement : Given a list of integers, create a new list containing only the even numbers using list comprehension.
# Example : Input - 1 2 3 4 5 6 7 8
# Output - [2, 4, 6, 8]
numbers = list(map(int, input("Enter numbers: ").split()))
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
