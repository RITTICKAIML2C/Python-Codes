# 🐍 Q1 — Python: Find Common Elements
# Task: Find the unique elements common to two lists.
# Input: [1, 2, 3, 4], [3, 4, 5, 6], Output: {3, 4}
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(set(a) & set(b))

# 🐍 Q2 — Python: Sort a List of Tuples by Second Value
# Task: Sort tuples by their second element.
# Input: [(1, 5), (2, 3), (4, 1)], Output: [(4, 1), (2, 3), (1, 5)]
data = [(1, 5), (2, 3), (4, 1)]
print(sorted(data, key=lambda x: x[1]))
