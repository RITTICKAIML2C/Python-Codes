# 🐍 Python 1 — Remove Duplicates While Preserving Order
nums = [3, 1, 3, 2, 1, 4]
result = list(dict.fromkeys(nums))
print(result)

# 🐍 Python 2 — Find Common Elements in 3 Lists
a = [1, 2, 3, 4]
b = [2, 3, 5]
c = [2, 3, 6]
result = list(set(a) & set(b) & set(c))
print(result)

