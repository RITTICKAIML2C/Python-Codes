# 🐍 Python Question 1, Difficulty: Easy
# Topic: collections.deque
# Question : Implement a queue using deque and perform the following operations: Insert 10, 20, 30, Remove one element from the front 
# Example : Output : Removed: 10, Queue: [20, 30]
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("Removed:", queue.popleft())
print("Queue:", list(queue))

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: deque
# Question : Reverse a string using a stack implemented with deque.
# Example : Input : Python, Output : nohtyP
from collections import deque
s = "Python"
stack = deque(s)
while stack:
    print(stack.pop(), end="")
