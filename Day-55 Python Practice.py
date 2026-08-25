# 🐍 Python 1 — Counter Practice, Difficulty: Easy
# Topic: Counter
# Question : Find the most frequent number in a list.
# Input:  [1,2,2,3,3,3,4], Output: 3
from collections import Counter
nums = [1,2,2,3,3,3,4]
print(Counter(nums).most_common(1)[0][0])

# 🐍 Python 2 — Rotate a List, Difficulty: Medium
# Topic: Lists
# Question : Rotate a list to the right by k positions.
# Input : [1,2,3,4,5], k = 2, Output: [4,5,1,2,3]
nums = [1,2,3,4,5]
k = 2
k %= len(nums)
result = nums[-k:] + nums[:-k]
print(result)
