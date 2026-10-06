# 🐍 Python Q1 — Find Common Characters
# Find characters that appear in both strings, including duplicates.
# Input:  "hello", "world", Output: ['l', 'o']
from collections import Counter
a = Counter("hello")
b = Counter("world")
result = list((a & b).elements())
print(result)

# 🐍 Python Q2 — Group Numbers by Frequency
# Input:  [1,1,2,2,2,3,4,4], Output: {3: [2], 2: [1,4], 1: [3]}
from collections import defaultdict, Counter
nums = [1,1,2,2,2,3,4,4]
freq = Counter(nums)
result = defaultdict(list)
for num, count in freq.items():
    result[count].append(num)
print(dict(result))
