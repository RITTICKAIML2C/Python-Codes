#🐍 Python Q1 — Word Frequency
# Question: Given a sentence, return the frequency of each word.
# Example : Input:  "python is easy and python is powerful", Output: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
from collections import Counter
s = "python is easy and python is powerful"
print(Counter(s.split()))

# 🐍 Python Q2 — First Duplicate
# Question: Find the first element that appears twice in a list.
# Example ; Input:  [4, 2, 7, 2, 9, 4], Output: 2
nums = [4, 2, 7, 2, 9, 4]
seen = set()
for x in nums:
    if x in seen:
        print(x)
        break
    seen.add(x)
