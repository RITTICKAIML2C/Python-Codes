# 🐍 Q1. Python — Find the Difference Between Two Lists
# Task: Return elements present in the first list but not in the second.
# Input: [1, 2, 3, 4, 5], [2, 4]
# Output: [1, 3, 5]
a = [1, 2, 3, 4, 5]
b = [2, 4]
print([x for x in a if x not in b])


# 🐍 Q2. Python — Find the Second Most Frequent Character
# Input: "success"
# Output: u (second-highest frequency)
from collections import Counter
s = "success"
freq = Counter(s)
ranked = sorted(freq.items(), key=lambda x: -x[1])
print(ranked[1][0])
