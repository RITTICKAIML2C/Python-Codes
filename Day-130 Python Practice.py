# 1. Python — Find elements appearing exactly twice
# Question: Return all numbers that appear exactly twice.
nums = [1, 2, 3, 2, 4, 1, 1, 5]
from collections import Counter
freq = Counter(nums)
result = [x for x, count in freq.items() if count == 2]
print(result)

# 2. Python — Rotate a list to the left by K positions
# Question: Rotate the list left by k positions.
nums = [1, 2, 3, 4, 5]
k = 2
k %= len(nums)
result = nums[k:] + nums[:k]
print(result)

