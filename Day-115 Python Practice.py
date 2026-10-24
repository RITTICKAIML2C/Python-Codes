# 🐍 Q1. Python — Move Negative Numbers to the Front
# Input: [3, -1, 4, -2, 0]
# Output: [-1, -2, 3, 4, 0]
nums = [3, -1, 4, -2, 0]
result = [x for x in nums if x < 0] + [x for x in nums if x >= 0]
print(result)


# 🐍 Q2. Python — Find the Most Frequent Character
# Input: "programming"
# Output: r (one most-frequent character)
from collections import Counter
text = "programming"
print(Counter(text).most_common(1)[0][0])
