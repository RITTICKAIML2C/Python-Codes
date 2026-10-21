# 🐍 Q1. Python — Count Word Frequency
# Task: Count how many times each word appears.
# Input: "cat dog cat"
# Output: {'cat': 2, 'dog': 1}
from collections import Counter
text = "cat dog cat"
print(dict(Counter(text.split())))


# 🐍 Q2. Python — Find the Second-Largest Unique Number
# Input: [4, 1, 7, 7, 3]
# Output: 4
nums = [4, 1, 7, 7, 3]
unique = sorted(set(nums))
print(unique[-2] if len(unique) >= 2 else None)
