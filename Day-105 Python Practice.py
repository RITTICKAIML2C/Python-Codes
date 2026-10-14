# 🐍 Q1 — Python: Remove Duplicates While Preserving Order
# Task: Remove repeated elements without changing the original order.
# Input: [4, 2, 4, 3, 2, 1]
# Output: [4, 2, 3, 1]
nums = [4, 2, 4, 3, 2, 1]
result = list(dict.fromkeys(nums))
print(result)

# 🐍 Q2 — Python: Find the Most Frequent Word
# Task: Find the most frequent word, ignoring capitalization.
# Input: "Python is great and Python is easy"
# Output: "python"
from collections import Counter
text = "Python is great and Python is easy"
words = text.lower().split()
print(Counter(words).most_common(1)[0][0])
