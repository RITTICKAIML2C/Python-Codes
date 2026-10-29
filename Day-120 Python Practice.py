# 🐍 Q1. Python — Find Numbers Appearing Exactly Once
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 3, 5]
from collections import Counter
nums = [1, 2, 2, 3, 4, 4, 5]
freq = Counter(nums)
print([x for x in nums if freq[x] == 1])


# 🐍 Q2. Python — Sort Words by Length
# Input: ["banana", "fig", "apple", "kiwi"]
# Output: ["fig", "kiwi", "apple", "banana"]
words = ["banana", "fig", "apple", "kiwi"]
print(sorted(words, key=len))
