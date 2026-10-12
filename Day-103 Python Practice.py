# 🐍 Q1 — Python: Find the Missing Numbers
# Task: Given numbers from 1 to n, find all missing numbers.
# Input: nums = [1, 2, 4, 6], n = 6
# Output: [3, 5]
nums = [1, 2, 4, 6]
n = 6
print([x for x in range(1, n + 1) if x not in nums])

# 🐍 Q2 — Python: Invert a Dictionary
# Task: Swap dictionary keys and values. Assume all values are unique.
# Input: {"a": 1, "b": 2, "c": 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}
data = {"a": 1, "b": 2, "c": 3}
result = {v: k for k, v in data.items()}
print(result)
