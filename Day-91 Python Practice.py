# 🐍 Python Q1 — Flatten a Nested List
# Question: Convert a list containing nested lists into one flat list.
# Input:  [1, [2, 3], [4, [5, 6]]], Output: [1, 2, 3, 4, 5, 6]
def flatten(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# 🐍 Python Q2 — Find the Top 2 Most Frequent Numbers
# Question: Return the two numbers with the highest frequencies.
# Input:  [1,1,1,2,2,3,3,3,3,4], Output: [3,1]
from collections import Counter
nums = [1,1,1,2,2,3,3,3,3,4]
freq = Counter(nums)
result = [x for x, count in freq.most_common(2)]
print(result)
