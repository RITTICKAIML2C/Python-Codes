# 🐍 Python 1 — enumerate(), Difficulty: Easy
# Topic: enumerate()
# Question : Print the index and value of every even number.
# Input: [10, 15, 20, 25, 30], Output: 0 10, 2 20, 4 30
nums = [10, 15, 20, 25, 30]
for i, num in enumerate(nums):
    if num % 2 == 0:
        print(i, num)

# 🐍 Python 2 — Valid Parentheses Checker, Difficulty: Medium
# Topic: Stack
# Question : Check whether brackets are balanced.
# Input: "({[]})", Output: True, Input: "([)]", Output: False
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack
print(is_valid("({[]})"))
