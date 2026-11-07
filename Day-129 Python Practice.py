# 1. Python — Find common elements in multiple lists
# Question: Find elements that appear in all three lists.
a = [1, 2, 3, 4, 5]
b = [2, 3, 5, 6]
c = [2, 5, 7]
result = list(set(a) & set(b) & set(c))
print(sorted(result))

# 2. Python — Find the longest word without repeating characters
# Question: Find the longest word in which no character appears more than once.
words = ["apple", "world", "python", "banana"]
result = max(
  (w for w in words if len(w) == len(set(w))),    
  key=len)
print(result)
