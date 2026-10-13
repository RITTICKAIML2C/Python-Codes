# 🐍 Q1 — Python: Find the First Non-Repeating Character
# Task: Return the first character that appears only once.
# Input: "aabbcde"
# Output: 'c'
from collections import Counter
s = "aabbcde"
freq = Counter(s)
print(next((c for c in s if freq[c] == 1), None))


# 🐍 Q2 — Python: Flatten a Nested List
# Task: Flatten a list nested exactly one level.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]
nested = [[1, 2], [3, 4], [5]]
flat = [x for group in nested for x in group]
print(flat)
