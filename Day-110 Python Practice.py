# 🐍 Q1 — Python: Check Whether a String Is a Pangram
# Task: Check whether a sentence contains every letter from a to z.
# Input: "The quick brown fox jumps over the lazy dog"
# Output: True
import string
s = "The quick brown fox jumps over the lazy dog"
print(set(string.ascii_lowercase) <= set(s.lower()))


# 🐍 Q2 Python: Find the Top 2 Most Frequent Numbers
# Task: Return the two most frequent numbers.
# Input: [1, 1, 2, 2, 2, 3, 3, 4]
# Output: [2, 1]
from collections import Counter
nums = [1, 1, 2, 2, 2, 3, 3, 4]
print([x for x, _ in Counter(nums).most_common(2)])
