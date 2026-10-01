# 🐍 Python Q1 — Recursive Sum of Nested Numbers
# Find the sum of all numbers inside a nested list.
# Input:  [1, [2, 3], [4, [5]]], Output: 15
def nested_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total
print(nested_sum([1, [2, 3], [4, [5]]]))

# 🐍 Python Q2 — Find the Most Common Pair
# Count how many times each pair of consecutive elements occurs.
# Input:  [1, 2, 1, 2, 3, 1, 2], Output: (1, 2)
from collections import Counter
nums = [1, 2, 1, 2, 3, 1, 2]
pairs = Counter(
    (nums[i], nums[i + 1])
    for i in range(len(nums) - 1)
)
print(pairs.most_common(1)[0][0])
