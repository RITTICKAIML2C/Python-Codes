# 🐍 Q1. Python — Find Common Dictionary Keys
# Input: a = {'x': 1, 'y': 2}, b = {'y': 5, 'z': 3}
# Output: ['y']
a = {'x': 1, 'y': 2}
b = {'y': 5, 'z': 3}
print(list(a.keys() & b.keys()))


# 🐍 Q2. Python — Find the Second-Largest Unique Number
# Input: [5, 2, 8, 8, 3]
# Output: 5
nums = [5, 2, 8, 8, 3]
unique = sorted(set(nums))
print(unique[-2] if len(unique) >= 2 else None)
