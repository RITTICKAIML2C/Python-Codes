# 🐍 Python 1 — Find Common Elements, Difficulty: Easy
# Question : Find elements that appear in both lists, without duplicates.
# Input: a = [1,2,2,3,4], b = [2,2,4,5], Output: [2,4]
a = [1,2,2,3,4]
b = [2,2,4,5]
result = list(set(a) & set(b))
print(result)

# 🐍 Python 2 — Rotate List, Difficulty: Medium
# Rotate a list to the right by k positions.
# Input: [1,2,3,4,5], k = 2, Output: [4,5,1,2,3]
nums = [1,2,3,4,5]
k = 2
k %= len(nums)
result = nums[-k:] + nums[:-k]
print(result)
