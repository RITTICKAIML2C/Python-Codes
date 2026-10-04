# 🐍 Python Q1 — Count Words by Length
# Input:  ["cat", "apple", "dog", "banana", "hi"], Output: {3: 2, 5: 1, 6: 1, 2: 1}
from collections import Counter
words = ["cat", "apple", "dog", "banana", "hi"]
result = Counter(len(word) for word in words)
print(dict(result))

# 🐍 Python Q2 — Group Numbers by Sign
# Separate positive, negative, and zero values.
# Input:  [3, -2, 0, 5, -1, 0], Output: {"positive": [3, 5],"negative": [-2, -1],"zero": [0, 0]}
nums = [3, -2, 0, 5, -1, 0]
result = {
    "positive": [],
    "negative": [],
    "zero": []
}
for x in nums:
    if x > 0:
        result["positive"].append(x)
    elif x < 0:
        result["negative"].append(x)
    else:
        result["zero"].append(x)
print(result)
