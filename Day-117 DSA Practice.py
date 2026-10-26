# 🐍 Q1. Python — Find Missing Numbers in a Range
# Task: Find numbers missing from 1 to n.
# Input: nums = [1, 2, 4, 6], n = 6
# Output: [3, 5]
nums = [1, 2, 4, 6]
n = 6
print(sorted(set(range(1, n + 1)) - set(nums)))


# 🐍 Q2. Python — Group Words by Their Length
# Input: ["hi", "cat", "go", "apple"]
# Output: {2: ["hi", "go"], 3: ["cat"], 5: ["apple"]}
from collections import defaultdict
words = ["hi", "cat", "go", "apple"]
groups = defaultdict(list)
for word in words:    
  groups[len(word)].append(word)
print(dict(groups))
