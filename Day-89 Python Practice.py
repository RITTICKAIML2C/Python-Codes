# 🐍 Python Q1 — Find Missing Numbers
# Question: Given numbers from 1 to n, find all missing numbers.
# Input:  [1, 2, 4, 6, 7], n = 7, Output: [3, 5]
nums = [1, 2, 4, 6, 7]
n = 7
present = set(nums)
result = [i for i in range(1, n + 1) if i not in present]
print(result)

# 🐍 Python Q2 — Sort a List of Tuples by the Second Value
# Question: Sort the tuples based on their second element.
# Input:  [(1, 5), (2, 2), (3, 8), (4, 1)], Output: [(4, 1), (2, 2), (1, 5), (3, 8)]
data = [(1, 5), (2, 2), (3, 8), (4, 1)]
result = sorted(data, key=lambda x: x[1])
print(result)
