# 🐍 Python 1 — Find the First Repeated Element
nums = [4, 2, 7, 2, 9, 4]
seen = set()
for num in nums:
    if num in seen:
        print(num)
        break
    seen.add(num)

# 🐍 Python 2 — Sort Words by Length
words = ["python", "is", "very", "powerful"]
result = sorted(words, key=len)
print(result)
