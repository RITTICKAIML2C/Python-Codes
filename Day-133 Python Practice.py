# 1. Python — Find all pairs with a given sum
# Question: Find all unique pairs in a list whose sum equals the target.
nums = [1, 2, 3, 4, 5, 6]
target = 7
seen = set()
pairs = []
for x in nums:
  complement = target - x
  if complement in seen:
    pairs.append((complement, x))
    seen.add(x)print(pairs)

# 2. Python — Flatten a nested list
# Question: Convert a 2D list into a single flat list.
matrix = [[1, 2], [3, 4], [5, 6]]
result = [x for row in matrix for x in row]
print(result)
