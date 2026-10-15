# 🐍 Q1 — Python: Move All Zeros to the End
# Task: Move all zeros to the end while preserving the order of non-zero elements.
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
nums = [0, 1, 0, 3, 12]
result = [x for x in nums if x != 0]
result += [0] * (len(nums) - len(result))
print(result)


# 🐍 Q2 — Python: Group Words by Their First Letter
# Task: Group words that begin with the same letter.
# Input: ["apple", "ant", "bat", "ball", "cat"]
# Output: {'a': ['apple', 'ant'], 'b': ['bat', 'ball'], 'c': ['cat']}
from collections import default
dictwords = ["apple", "ant", "bat", "ball", "cat"]
groups = defaultdict(list)
for word in words:    
  groups[word[0]].append(word)print(dict(groups))
