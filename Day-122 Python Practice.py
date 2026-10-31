# 🐍 Q1. Python — Find the Top 2 Most Frequent Numbers
# Input: [1, 2, 2, 3, 3, 3, 4, 4]
# Output: [3, 2]
from collections import Counter
nums = [1, 2, 2, 3, 3, 3, 4, 4]
print([x for x, _ in Counter(nums).most_common(2)])


# 🐍 Q2. Python — Group Numbers by Sign
# Input: [-2, 3, -1, 0, 5, -4]
# Output: {'positive': [3, 5], 'negative': [-2, -1, -4], 'zero': [0]}
nums = [-2, 3, -1, 0, 5, -4]
groups = {    
  "positive": [x for x in nums if x > 0],    
  "negative": [x for x in nums if x < 0],    
  "zero": [x for x in nums if x == 0]}
print(groups)
