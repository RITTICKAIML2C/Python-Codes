# 1. Python — Find elements that appear in exactly one list
# Question: Find elements that appear in either list, but not both.
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = sorted(set(a) ^ set(b))
print(result)

# 2. Python — Count words starting with each letter
# Question: Group words by their first character and count them.
words = ["apple", "ant", "ball", "bat", "cat"]
result = {}
for word in words:
  key = word[0]
  result[key] = result.get(key, 0) + 1
  print(result)

