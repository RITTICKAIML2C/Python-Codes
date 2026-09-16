# 🐍 Python 1 — Count Words in a Sentence
from collections import Counter
sentence = "python is easy and python is powerful"
count = Counter(sentence.split())
print(count)

# 🐍 Python 2 — Find the Second Most Frequent Character
from collections import Counter
s = "programming"
count = Counter(s)
result = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(result[1][0])
