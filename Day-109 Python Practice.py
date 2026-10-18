# 🐍 Q1 — Python: Rotate a List to the Right
# Task: Rotate a list to the right by k positions.
# Input: nums = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
nums = [1, 2, 3, 4, 5]
k = 2k %= len(nums)
result = nums[-k:] + nums[:-k] if k else nums
print(result)


# 🐍 Q2 — Python: Group Words by Length
# Task: Group words according to their length.
# Input: ["cat", "hi", "dog", "sun", "hello"]
# Output: {3: ['cat', 'dog', 'sun'], 2: ['hi'], 5: ['hello']}
from collections import default
dictwords = ["cat", "hi", "dog", "sun", "hello"]
groups = defaultdict(list)
for word in words:    
  groups[len(word)].append(word)
print(dict(groups))
