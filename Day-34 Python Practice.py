# 🐍 Python Question 1, Difficulty: Easy
# Topic: reduce()
# Question : Find the product of all numbers in a list using reduce().
# Example : Input : nums = [2, 3, 4], Output : 24
from functools import reduce
nums = [2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: itertools.product()
# Question : Print all possible pairs from two lists.
# Example : Input : A = [1, 2], B = ["A", "B"], Output : (1, 'A') (1, 'B') (2, 'A') (2, 'B')
from itertools import product
A = [1, 2]
B = ["A", "B"]
for pair in product(A, B):
    print(pair)
