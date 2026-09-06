# 🐍 Python 1 — Find Duplicate Elements, Difficulty: Easy
nums = [1, 2, 3, 2, 4, 1, 5]
duplicates = [
    num for num in set(nums)
    if nums.count(num) > 1
]
print(duplicates)

# 🐍 Python 2 — Merge Two Dictionaries, Difficulty: Medium
# If the same key exists, the second dictionary overwrites it.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
result = dict1 | dict2
print(result)
