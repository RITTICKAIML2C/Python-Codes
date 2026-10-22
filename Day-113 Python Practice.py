# 🐍 Q1. Python — Find Common Elements in Two Lists
# Input: [1, 2, 3, 4], [3, 4, 5, 6]
# Output: [3, 4]
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(list(set(a) & set(b)))


# 🐍 Q2. Python — Sort a Dictionary by Value
# Input: {'a': 3, 'b': 1, 'c': 2}
# Output: {'b': 1, 'c': 2, 'a': 3}
d = {'a': 3, 'b': 1, 'c': 2}
print(dict(sorted(d.items(), key=lambda x: x[1])))
