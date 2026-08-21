# 🐍 Python 1 — Dictionary Inversionl, Difficulty: Easy
# Topic: Dictionaries
# Question : Swap the keys and values of a dictionary.
# Input : {"a": 1, "b": 2, "c": 3}, Output: {1: "a", 2: "b", 3: "c"}
data = {"a": 1, "b": 2, "c": 3}
result = {v: k for k, v in data.items()}
print(result)

# 🐍 Python 2 — Find Common Elements, Difficulty: Easy–Medium
# Topic: Sets
# Question : Find the elements common to two lists, without duplicates.
# Input : [1,2,3,4], [3,4,5,6], Output : [3,4]
a = [1,2,3,4]
b = [3,4,5,6]
result = list(set(a) & set(b))
print(result)
