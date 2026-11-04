# 1. Python — Find the second most frequent number
# Question: Find the number with the second-highest frequency.
nums = [1, 2, 2, 3, 3, 3, 4, 4]
freq = {}
for x in nums:
  freq[x] = freq.get(x, 0) + 1
  ranked = sorted(freq, key=freq.get, reverse=True)
  print(ranked[1])

# 2. Python — Group strings by their last character
# Question: Group words that end with the same character.
words = ["cat", "bat", "dog", "log", "sun"]
groups = {}
for word in words:
  groups.setdefault(word[-1], []).append(word)
  print(groups)
