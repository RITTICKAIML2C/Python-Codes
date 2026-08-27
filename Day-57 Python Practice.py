# 🐍 Python 1 — defaultdict, Difficulty: Easy
# Topic: Dictionary
# Question : Group numbers by whether they are even or odd.
# Input:  [1,2,3,4,5,6], Output: {"even": [2,4,6],"odd": [1,3,5]}
from collections import defaultdict
nums = [1,2,3,4,5,6]
result = defaultdict(list)
for num in nums:
    key = "even" if num % 2 == 0 else "odd"
    result[key].append(num)
print(dict(result))

# 🐍 Python 2 — Second Largest Number, Difficulty: Medium
# Topic: Lists + Sets
# Question : Find the second largest unique number.
# Input:  [10, 5, 8, 10, 3], Output: 8
nums = [10, 5, 8, 10, 3]
nums = list(set(nums))
nums.sort()
print(nums[-2])
