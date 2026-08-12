# 🐍 Python 1 — defaultdict Graph, Difficulty: Easy
# Topic: defaultdict + Graph
# Question : Create an adjacency list for an undirected graph.
# Example : Input: edges = [(1,2), (1,3), (2,4)]
# Output: {1: [2,3], 2: [1,4], 3: [1], 4: [2]}
from collections import defaultdict
edges = [(1,2), (1,3), (2,4)]
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
print(dict(graph))

# 🐍 Python 2 — Count Vowels, Difficulty: Easy–Medium
# Topic: Sets + Strings
# Question : Count the number of vowels in a string using a set.
# Example : Input: "programming", Output: 3
s = "programming"
vowels = set("aeiou")
count = sum(ch in vowels for ch in s)
print(count)
