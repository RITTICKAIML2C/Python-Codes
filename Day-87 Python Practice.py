# 🐍 Python Q1 — Sort Dictionary by Key
# Question: Sort a dictionary by its keys.
# Input:  {3: "c", 1: "a", 2: "b"}, Output: {1: "a", 2: "b", 3: "c"}
data = {3: "c", 1: "a", 2: "b"}
result = dict(sorted(data.items()))
print(result)

# 🐍 Python Q2 — Find Two Numbers With Closest Sum to Target
# Question: Find the pair whose sum is closest to the target.
# Input:  [1, 4, 7, 10], target = 12, Output: (1, 10)
nums = [1, 4, 7, 10]
target = 12
nums.sort()
left, right = 0, len(nums) - 1
best = (nums[left], nums[right])
while left < right:
    if abs(nums[left] + nums[right] - target) < abs(best[0] + best[1] - target):
        best = (nums[left], nums[right])
    if nums[left] + nums[right] < target:
        left += 1
    else:
        right -= 1
print(best)
