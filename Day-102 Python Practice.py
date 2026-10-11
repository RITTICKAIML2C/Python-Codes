# 🐍 Q1 — Python: Find Elements Appearing Exactly Once
# Task: Return elements that appear exactly once.
# Input: [1, 2, 2, 3, 4, 4, 5], Output: [1, 3, 5]
from collections import Counter
nums = [1, 2, 2, 3, 4, 4, 5]
freq = Counter(nums)
print([x for x in nums if freq[x] == 1])

# 🐍 Q2 — Python: Sort a Dictionary by Value (Descending)
# Task: Sort a dictionary from highest to lowest value.
# Input: {"A": 30, "B": 10, "C": 20}, Output: [('A', 30), ('C', 20), ('B', 10)]
data = {"A": 30, "B": 10, "C": 20}
print(sorted(data.items(), key=lambda x: x[1], reverse=True))
