# 🐍 Q1 — Python: Count Word Frequency
# Task: Count how often each word appears, ignoring capitalization.
# Input: "Python is fun and python is powerful", Output: {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}
from collections import Counter
text = "Python is fun and python is powerful"
freq = Counter(text.lower().split())
print(dict(freq))

# 🐍 Q2 — Python: Group Anagrams
# Task: Group words that contain the same letters.
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"], Output: Groups containing ["eat", "tea", "ate"], ["tan", "nat"], and ["bat"].
from collections import defaultdict
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
for word in words:
    groups["".join(sorted(word))].append(word)
print(list(groups.values()))
