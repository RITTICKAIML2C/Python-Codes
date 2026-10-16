# 🐍 Q1 — Python: Find Elements in One List but Not Another
# Task: Return elements present in the first list but absent from the second, preserving order.
# Input: a = [1, 2, 3, 4, 2], b = [2, 4]
# Output: [1, 3]
a = [1, 2, 3, 4, 2]
b = [2, 4]
result = [x for x in a if x not in set(b)]
print(list(dict.fromkeys(result)))


# 🐍 Q2 — Python: Check Whether Two Strings Are Anagrams
# Task: Check whether two strings contain the same characters with the same frequencies.
# Input: "listen", "silent"
# Output: True
from collections import Counter
def is_anagram(a, b):    
  return Counter(a) == Counter(b)
print(is_anagram("listen", "silent"))
