# 1. Python — Find the most frequent number
# Question: Find the number that appears most often.
nums = [2, 3, 2, 5, 3, 2, 4]
freq = {}
for n in nums:    
  freq[n] = freq.get(n, 0) + 1
  print(max(freq, key=freq.get))

# 2. Python — Merge two dictionaries and keep the maximum value
# Question: If a key exists in both dictionaries, keep its larger value.
a = {'x': 10, 'y': 20}
b = {'y': 15, 'z': 30}
result = a.copy()
for k, v in b.items():    
  result[k] = max(result.get(k, v), v)
  print(result)
