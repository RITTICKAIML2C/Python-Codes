# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Recursion
# Problem Statement : Write a recursive function to calculate the factorial of a number.
# Factorial: 5! = 5 × 4 × 3 × 2 × 1 = 120
# Example : Input - 5, Output - 120
def factorial(n):
    # Base condition
    if n == 0 or n == 1:
        return 1
    # Recursive call
    return n * factorial(n - 1)
number = int(input("Enter number: "))
print(factorial(number))

# 🐍 Python Question 2 , Difficulty: Beginner
# Topic: Recursion + Global Variable
# Problem Statement : Write a recursive function to find the sum of numbers from 1 to n. Use a global variable total to store the result.
# Example - Input : 5, Output : 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15
total = 0
def calculate_sum(n):
    global total
    if n == 0:
        return
    total += n
    calculate_sum(n - 1)
number = int(input("Enter number: ")
calculate_sum(number)
print(total)
