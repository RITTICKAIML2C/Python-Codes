# 🐍 Python 1 — Counter.most_common(), Difficulty: Easy
# Topic: Counter
# Question : Find the 2 most frequent elements in a list.
# Example : Input:  [1,2,2,3,3,3,4], Output: [(3,3), (2,2)]
from collections import Counter
nums = [1,2,2,3,3,3,4]
print(Counter(nums).most_common(2))

# 🐍 Python 2 — Nested Dictionary, Difficulty: Easy–Medium
# Topic: Dictionaries
# Question : Create a dictionary storing each student's marks in 3 subjects and calculate their total.
# Example : Input: students = {"Rahul": {"math": 80, "science": 90, "english": 70}}
# Output : Rahul: 240
students = {
    "Rahul": {"math": 80, "science": 90, "english": 70}
}
for name, marks in students.items():
    total = sum(marks.values())
    print(name, total)
