# 🐍 Python 1 — Find the First Non-Repeating Character
from collections import Counter
s = "swiss"
count = Counter(s)
for ch in s:
    if count[ch] == 1:
        print(ch)
        break

# 🐍 Python 2 — Merge Two Lists and Remove Duplicates
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = list(set(a + b))
print(result)
