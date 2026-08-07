# 🐍 Python Question 1, Difficulty: Easy
# Topic: dict.setdefault()
# Question : Count the frequency of each character in a string using setdefault().
# Example : Input : s = "banana", Output : {'b': 1, 'a': 3, 'n': 2}
s = "banana"
freq = {}
for ch in s:
    freq.setdefault(ch, 0)
    freq[ch] += 1
print(freq)

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: OrderedDict
# Question : Store student marks in an OrderedDict and print them in the order they were inserted.
# Example : Output : Rahul : 90, Aman : 85, Priya : 95
from collections import OrderedDict
students = OrderedDict()
students["Rahul"] = 90
students["Aman"] = 85
students["Priya"] = 95
for name, marks in students.items():
    print(name, ":", marks)
