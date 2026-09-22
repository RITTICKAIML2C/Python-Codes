# 🐍 Python Q1 — Character With Highest Frequency
# Question: Find the character that appears most often.
# Input:  "programming", Output: "r"
from collections import Counter
s = "programming"
print(Counter(s).most_common(1)[0][0])

# 🐍 Python Q2 — Find Pairs With Given Sum
# Question: Find all pairs whose sum equals the target.
# Input:  [2, 4, 3, 5, 7, 8, 9], target = 10, Output: [(2, 8), (3, 7)]
nums = [2, 4, 3, 5, 7, 8, 9]
target = 10
seen = set()
pairs = []
for x in nums:
    if target - x in seen:
        pairs.append((target - x, x))
    seen.add(x)
print(pairs)
