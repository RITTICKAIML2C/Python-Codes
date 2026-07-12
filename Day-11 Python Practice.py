# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Lambda Function
# Problem Statement : Write a program using a lambda function to find the square of a number.
# Example : Input - 6, Output- 36
square = lambda x: x * x
number = int(input("Enter a number: "))
print("Square =", square(number))

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: map() and filter()
# Problem Statement - Given a list of numbers, Use map() to create a new list containing the square of each number, Use filter() to create another list containing only the even numbers.
# Example : Input - 1 2 3 4 5, Output - Squared List = [1, 4, 9, 16, 25], Even Numbers = [2, 4]
numbers = list(map(int, input("Enter numbers: ").split()))
square_list = list(map(lambda x: x * x, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Squared List =", square_list)
print("Even Numbers =", even_numbers)
