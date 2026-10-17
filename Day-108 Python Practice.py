# 🐍 Q1 — Python: Find the Second Largest Unique Number
# Task: Find the second-largest distinct number in a list.
# Input: [10, 5, 8, 10, 8, 3]
# Output: 8
nums = [10, 5, 8, 10, 8, 3]
unique = sorted(set(nums), reverse=True)
print(unique[1] if len(unique) > 1 else None)

# 🐍 Q2 — Python: Group Numbers by Sign
# Task: Separate positive, negative, and zero values.
# Input: [3, -1, 0, -5, 7, 0]
nums = [3, -1, 0, -5, 7, 0]
groups = {"positive": [], "negative": [], "zero": []}
for n in nums:
    key = "positive" if n > 0 else "negative" if n < 0 else "zero"
    groups[key].append(n)
print(groups)
