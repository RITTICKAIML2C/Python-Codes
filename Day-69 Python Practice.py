# 🐍 Python 1 — Check Palindrome
s = "madam"
print(s == s[::-1])

# 🐍 Python 2 — Find the Most Frequent Element
from collections import Counter
nums = [1, 3, 2, 3, 4, 3, 2]
result = Counter(nums).most_common(1)[0][0]
print(result)
