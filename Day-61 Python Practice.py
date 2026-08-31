# 🐍 Python 1 — First Non-Repeating Character, Difficulty: Easy
# Topic: Dictionary
# Find the first character that appears only once. 
# Input: "aabbcde", Output: "c"
from collections import Counter
s = "aabbcde"
count = Counter(s)
for ch in s:
    if count[ch] == 1:
        print(ch)
        break

# 🐍 Python 2 — Maximum Sum Subarray of Size K, Difficulty: Medium
# Topic: Sliding Window
# Question : Find the maximum sum of any k consecutive elements.
# Input: nums = [2,1,5,1,3,2], k = 3, Output: 9
nums = [2,1,5,1,3,2]
k = 3
window = sum(nums[:k])
best = window
for i in range(k, len(nums)):
    window += nums[i] - nums[i-k]
    best = max(best, window)
print(best)
