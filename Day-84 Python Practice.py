# 🐍 Python Q1 — Sort Words Alphabetically
# Question: Sort a list of words alphabetically without changing the original list.
# Input:  ["banana", "apple", "cherry"], Output: ["apple", "banana", "cherry"]
words = ["banana", "apple", "cherry"]
result = sorted(words)
print(result)

# 🐍 Python Q2 — Find the Most Frequent Number
# Question: Find the number that occurs most frequently.
# Input:  [4, 2, 4, 3, 2, 4, 5], Output: 4
from collections import Counter
nums = [4, 2, 4, 3, 2, 4, 5]
print(Counter(nums).most_common(1)[0][0])
