# 🐍 Python Q1 — Find Duplicate Values
# Return all values that appear more than once.
# Input:  [1,2,3,2,4,1,5], Output: [1,2]
nums = [1,2,3,2,4,1,5]
seen = set()
duplicates = set()
for x in nums:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)
print(list(duplicates))

# 🐍 Python Q2 — Sort Dictionary by Value
# Input:  {"a": 5, "b": 2, "c": 8}
# Output: {"b": 2, "a": 5, "c": 8}
data = {"a": 5, "b": 2, "c": 8}
result = dict(sorted(data.items(), key=lambda x: x[1]))
print(result)
