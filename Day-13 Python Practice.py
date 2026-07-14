# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Dictionary Comprehension
# Problem Statement : Create a dictionary where: The keys are numbers from 1 to 5. The values are the square of each number. Use dictionary comprehension.
# Example : Output - {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
square_dict = {num: num * num for num in range(1, 6)}
print(square_dict)

# 🐍 Python Question 2, ,Difficulty: Beginner
# Topic: Set Comprehension
# Problem Statement : Create a set containing the squares of numbers from 1 to 10 using set comprehension.
# Example : Output - {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}
square_set = {num * num for num in range(1, 11)}
print(square_set)
