# 🐍 Python Q1 — Count Number Frequency
# Question: Given a list, print each number and its frequency.
# Input:  [1, 2, 2, 3, 3, 3], Output: {1: 1, 2: 2, 3: 3}
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
print(dict(Counter(nums)))

# 🐍 Python Q2 — Remove Duplicates While Keeping Order
# Question: Remove duplicate elements without changing their original order.
# Input:  [4, 2, 4, 1, 2, 3], Output: [4, 2, 1, 3]
nums = [4, 2, 4, 1, 2, 3]
seen = set()
result = []
for x in nums:
    if x not in seen:
        result.append(x)
        seen.add(x)
print(result)
