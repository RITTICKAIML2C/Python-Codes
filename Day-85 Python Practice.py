# 🐍 Python Q1 — Find Unique Elements
# Question: Print elements that appear exactly once.
# Input:  [1, 2, 2, 3, 4, 4, 5], Output: [1, 3, 5]
from collections import Counter
nums = [1, 2, 2, 3, 4, 4, 5]
freq = Counter(nums)
print([x for x in nums if freq[x] == 1])

# 🐍 Python Q2 — Longest Word Without Repeating Characters
# Question: Given a string, find the length of the longest substring without duplicate characters.
# Input:  "abcabcbb", Output: 3
s = "abcabcbb"
seen = set()
left = 0
ans = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    ans = max(ans, right - left + 1)
print(ans)
