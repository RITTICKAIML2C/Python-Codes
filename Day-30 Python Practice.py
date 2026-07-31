# 🐍 Python 1 — enumerate(), Difficulty: Easy
# Topic: enumerate()
# Question : Given a list of names, print each name along with its index.
# Example : Input: ["Rahul", "Aman", "Riya"], Output: 0 Rahul 1 Aman 2 Riya
names = ["Rahul", "Aman", "Riya"]
for index, name in enumerate(names):
    print(index, name)

# 🐍 Python 2 — zip(), Difficulty: Easy–Medium
# Topic: zip() + Dictionaries
# Question : Given two lists containing student names and marks, create a dictionary connecting each student to their marks.
# Example : names = ["A", "B", "C"], marks = [80, 90, 75]
# Output: {"A": 80, "B": 90, "C": 75}
names = ["A", "B", "C"]
marks = [80, 90, 75]
result = dict(zip(names, marks))
print(result)
