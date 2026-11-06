# 1. Python — Find the smallest missing positive number
# Question: Find the smallest positive integer missing from a list.
nums = [3, 4, -1, 1]
seen = set(nums)
i = 1
while i in seen:
  i += 1
  print(i)

# 2. Python — Merge lists into a dictionary
# Question: Given two lists, use the first as keys and the second as values.
keys = ["name", "age", "city"]
values = ["Alex", 21, "Delhi"]
result = dict(zip(keys, values))
print(result)
