# 1. Python — Find the most common word
# Question: Find the most frequent word in a sentence, ignoring uppercase/lowercase.
from collections import Counter
text = "Python is great and python is powerful"
words = text.lower().split()
print(Counter(words).most_common(1)[0][0])

# 2. Python — Remove all occurrences of an element
# Question: Remove every occurrence of x from a list.
nums = [1, 2, 3, 2, 4, 2, 5]
x = 2
result = [n for n in nums if n != x]
print(result)
