# 1. Python — Find the first non-repeating number
# Question: Find the first number that appears exactly once.
nums = [4, 5, 1, 2, 1, 4, 5, 7]
freq = {}
for x in nums:
  freq[x] = freq.get(x, 0) + 1
  for x in nums:
    if freq[x] == 1:
      print(x)
      break

# 2. Python — Sort a dictionary by key length
# Question: Sort dictionary entries according to the length of their keys.
data = {"banana": 3, "fig": 5, "apple": 2, "kiwi": 4}
result = dict(sorted(data.items(), key=lambda x: len(x[0])))
print(result)
