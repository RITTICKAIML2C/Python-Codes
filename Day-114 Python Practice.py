# 🐍 Q1. Python — Find Elements Appearing More Than Once
# Input: [1, 2, 3, 2, 4, 1, 5]
# Output: [1, 2]
nums = [1, 2, 3, 2, 4, 1, 5]
duplicates = sorted({x for x in nums if nums.count(x) > 1})
print(duplicates)


# 🐍 Q2. Python — Find the Longest Consecutive Sequence
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4  (sequence: 1, 2, 3, 4)
nums = [100, 4, 200, 1, 3, 2]
s = set(nums)
best = 0
for x in s:
  if x - 1 not in s:
    length = 1
    while x + length in s:
      length += 1
      best = max(best, length)
print(best)
