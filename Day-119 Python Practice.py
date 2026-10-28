# 🐍 Q1. Python — Find the Most Frequent Word
# Input: "cat dog cat bird dog cat"
# Output: cat
from collections import Counter
text = "cat dog cat bird dog cat"
print(Counter(text.split()).most_common(1)[0][0])


# 🐍 Q2. Python — Remove Duplicates While Preserving Order
# Input: [3, 1, 3, 2, 1, 4]
# Output: [3, 1, 2, 4]
nums = [3, 1, 3, 2, 1, 4]
print(list(dict.fromkeys(nums)))
