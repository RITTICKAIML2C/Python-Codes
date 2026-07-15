# 🐍 Python Question 1, Difficulty: Beginner
# Topic: Generators
# Problem Statement : Write a generator function that prints numbers from 1 to n using the yield keyword.
# Example : Input - 5, Output - 1, 2, 3, 4, 5
def numbers(n):
    for i in range(1, n + 1):
        yield i
n = int(input("Enter a number: "))
for value in numbers(n):
    print(value)

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: Iterators
# Problem Statement : Create an iterator from a list and print each element using the next() function.
# Example : Input - 10 20 30, Output - 10, 20, 30
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
