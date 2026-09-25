# 🐍 Python Q1 — Count Duplicate Words
# Question: Find all words that appear more than once.
# Input:  ["apple", "banana", "apple", "orange", "banana", "apple"], Output: ["apple", "banana"]
from collections import Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = Counter(words)
print([word for word, count in freq.items() if count > 1])

# 🐍 Python Q2 — Longest Consecutive Sequence
# Question: Find the length of the longest consecutive sequence.
# Input:  [100, 4, 200, 1, 3, 2], Output: 4
nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
longest = 0
for x in s:
    if x - 1 not in s:
        length = 1
        while x + length in s:
            length += 1
        longest = max(longest, length)
print(longest)
