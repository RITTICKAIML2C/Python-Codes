# 🐍 Python Q1 — Rotate a List
# Rotate a list to the right by k positions.
# Input:  [1,2,3,4,5], k = 2, Output: [4,5,1,2,3]
nums = [1, 2, 3, 4, 5]
k = 2
k %= len(nums)
result = nums[-k:] + nums[:-k]
print(result)

# 🐍 Python Q2 — Find the First Non-Repeating Character
# Input:  "aabbcdde", Output: "c"
from collections import Counter
s = "aabbcdde"
freq = Counter(s)
for ch in s:
    if freq[ch] == 1:
        print(ch)
        break
