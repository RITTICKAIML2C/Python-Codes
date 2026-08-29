# 🐍 Python 1 — Counter + Sorting, Difficulty: Easy
# Topic: Dictionary / Counter
# Question : Return the frequency of each character, sorted from most frequent to least frequent.
# Input: "banana", Output: [('a', 3), ('n', 2), ('b', 1)]
from collections import Counter
s = "banana"
result = sorted(
    Counter(s).items(),
    key=lambda x: x[1],
    reverse=True
)
print(result)

# 🐍 Python 2 — Find Missing Number, Difficulty: Medium
# Topic: Lists + Problem Solving
# Question : The list contains numbers from 1 to n, but one number is missing. Find it.
# Input: [1, 2, 4, 5], Output: 3
nums = [1, 2, 4, 5]
n = len(nums) + 1
expected = n * (n + 1) // 2
actual = sum(nums)
print(expected - actual)
