# 🐍 Python 1 — namedtuple, Difficulty: Easy
# Topic: collections.namedtuple
# Question : Store a student's name and marks using namedtuple.
# Example : Input: Name = Rahul, Marks = 90, Output: Rahul 90
from collections import namedtuple
Student = namedtuple("Student", ["name", "marks"])
s = Student("Rahul", 90)
print(s.name, s.marks)

# 🐍 Python 2 — deque.rotate(), Difficulty: Easy–Medium
# Topic: deque
# Question : Rotate a queue 2 positions to the right, Example : Input : [1, 2, 3, 4, 5], Output: [4, 5, 1, 2, 3]
from collections import deque
q = deque([1, 2, 3, 4, 5])
q.rotate(2)
print(list(q))
