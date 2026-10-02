# 🐍 Python Q1 — Merge Two Dictionaries
# Question: Merge two dictionaries. If a key exists in both, add their values.
# Input: a = {"a": 10, "b": 20}, b = {"b": 5, "c": 15}, Output: {"a": 10, "b": 25, "c": 15}
a = {"a": 10, "b": 20}
b = {"b": 5, "c": 15}
result = a.copy()
for key, value in b.items():
    result[key] = result.get(key, 0) + value
print(result)

# 🐍 Python Q2 — Remove Duplicates While Preserving Order
# Question: Remove duplicate elements without changing their original order.
# Input:  [4, 2, 4, 1, 2, 3, 1], Output: [4, 2, 1, 3]
nums = [4, 2, 4, 1, 2, 3, 1]
seen = set()
result = []
for x in nums:
    if x not in seen:
        seen.add(x)
        result.append(x)
print(result)
