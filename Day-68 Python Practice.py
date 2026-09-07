# 🐍 Python 1 — Character Frequency
# Count the frequency of every character.
s = "programming"
frequency = {}
for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)

# 🐍 Python 2 — Find the Second Largest Number
nums = [10, 5, 8, 20, 15]
first = second = float("-inf")
for num in nums:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print(second)
