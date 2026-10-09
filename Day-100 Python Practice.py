# 🐍 Q1 — Python: Find the Second Most Frequent Character
# Task: Find the character with the second-highest frequency.
# Input: "banana", Output: 'n'
from collections import Counter
s = "banana"
freq = Counter(s)
print(freq.most_common(2)[1][0])

# 🐍 Q2 — Python: Merge Two Dictionaries
# Task: Merge two dictionaries, adding values when keys overlap.
# Input: a = {"apple": 3, "banana": 2}, b = {"banana": 4, "orange": 5}, Output: {'apple': 3, 'banana': 6, 'orange': 5}, 
a = {"apple": 3, "banana": 2}, b = {"banana": 4, "orange": 5}
result = a.copy()
for key, value in b.items():
    result[key] = result.get(key, 0) + value
print(result)
