# 🐍 Python Q1 — Find Highest-Frequency Word
# Question: Find the word that appears most frequently.
# Input:  "cat dog cat bird dog cat". Output: "cat"
from collections import Counter
s = "cat dog cat bird dog cat"
words = s.split()
print(Counter(words).most_common(1)[0][0])

# 🐍 Python Q2 — Move All Zeros to the End
# Question: Move all 0s to the end while keeping the order of other elements.
# Input:  [0, 1, 0, 3, 12], Output: [1, 3, 12, 0, 0]
nums = [0, 1, 0, 3, 12]
result = [x for x in nums if x != 0]
result += [0] * (len(nums) - len(result))
print(result)
