# 🐍 Python 1 — setdefault(), Difficulty: Easy
# Topic: Dictionaries
# Question : Group words by their first letter. Input: ["apple", "ant", "bat", "ball"]
# Output: {"a": ["apple", "ant"], "b": ["bat", "ball"]}
words = ["apple", "ant", "bat", "ball"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print(groups)

# 🐍 Python 2 — Find Duplicate Numbers, Difficulty: Medium
# Topic: Sets + Problem Solving
# Question : Return all numbers that appear more than once. Input: [1, 2, 3, 2, 4, 1, 5], Output: [1, 2]
nums = [1, 2, 3, 2, 4, 1, 5]
seen = set()
duplicates = set()
for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(list(duplicates))
