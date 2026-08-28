# 🐍 Python 1 — Recursive Sum, Difficulty: Easy
# Topic: Recursion
# Question : Find the sum of all numbers from 1 to n using recursion.
# Input: 5, Output: 15
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)
print(total(5))

# 🐍 Python 2 — Flatten a Nested List, Difficulty: Medium
# Topic: Recursion + Lists
# Question : Flatten a list that can contain nested lists.
# Input:  [1, [2, 3], [4, [5, 6]]], Output: [1, 2, 3, 4, 5, 6]
def flatten(nums):
    result = []
    for x in nums:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result
print(flatten([1, [2, 3], [4, [5, 6]]]))
