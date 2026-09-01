# 🐍 Python 1 — Check if Two Strings Are Anagrams, Difficulty: Easy
# Topic: Dictionary / Counter
# Question : Check whether two strings contain the same characters with the same frequency.
# Input: s = "listen", t = "silent", Output: True
from collections import Counter
s = "listen"
t = "silent"
print(Counter(s) == Counter(t))

# 🐍 Python 2 — Merge Overlapping Intervals, Difficulty: Medium
# Topic: Sorting + Lists
# Question : Merge all overlapping intervals.
# Input; [[1,3], [2,6], [8,10], [15,18]], Output: [[1,6], [8,10], [15,18]]
intervals = [[1,3], [2,6], [8,10], [15,18]]
intervals.sort()
result = []
for start, end in intervals:
    if not result or start > result[-1][1]:
        result.append([start, end])
    else:
        result[-1][1] = max(result[-1][1], end)
print(result)
