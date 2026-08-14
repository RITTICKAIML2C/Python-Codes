# 🐍 Python 1 — Counter + most_common(), Difficulty: Easy
# Topic: Counter
# Question : Find the 3 most common words in a list.
# Example : Input: ["python", "java", "python", "c", "java", "python"], Output: [("python", 3), ("java", 2), ("c", 1)]
from collections import Counter
words = ["python", "java", "python", "c", "java", "python"]
print(Counter(words).most_common(3))

# 🐍 Python 2 — Recursive String Reversal, Difficulty: Easy–Medium
# Topic: Recursion
# Question : Reverse a string using recursion.
# Example : Input: "hello", Output: "olleh"
def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]
print(reverse("hello"))
