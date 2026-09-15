# 🐍 Python 1 — Find Elements Present in One List but Not Another
a = [1, 2, 3, 4, 5]
b = [2, 4, 6]
result = list(set(a) - set(b))
print(result)

# 🐍 Python 2 — Find the Longest Word in a Sentence
sentence = "Python makes coding very interesting"
words = sentence.split()
result = max(words, key=len)
print(result)
