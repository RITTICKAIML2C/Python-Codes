# 🐍 Q1. Python — Find the First Non-Repeating Character
# Input: "aabbcddee"
# Output: 'c'
from collections import Counter
s = "aabbcddee"
freq = Counter(s)
print(next((ch for ch in s if freq[ch] == 1), None))


# 🐍 Q2. Python — Merge Two Dictionaries and Add Common Values
# Input: a = {'x': 2, 'y': 3}, b = {'y': 4, 'z': 5}
# Output: {'x': 2, 'y': 7, 'z': 5}
a = {'x': 2, 'y': 3}
b = {'y': 4, 'z': 5}
result = a.copy()
for k, v in b.items():    
  result[k] = result.get(k, 0) + v
  print(result)
