# 🐍 Python 1 — any() and all(), Difficulty: Easy
# Topic: Built-in Functions
# Question : Check whether any number is negative and whether all numbers are positive.
# Input: [2, 5, -1, 8], Output: Any negative: True, All positive: False
nums = [2, 5, -1, 8]
print(any(x < 0 for x in nums))
print(all(x > 0 for x in nums))

# 🐍 Python 2 — First Non-Repeating Character, Difficulty: Easy–Medium
# Topic: Dictionary / Counter
# Question : Find the first character that appears only once.
# Input: "aabbcdde", Output: "c"
from collections import Counter
s = "aabbcdde"
freq = Counter(s)
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
