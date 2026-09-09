# 🐍 Python 1 — Check if a List is Sorted
nums = [1, 2, 3, 4, 5]
is_sorted = all(
    nums[i] <= nums[i + 1]
    for i in range(len(nums) - 1)
)
print(is_sorted)

# 🐍 Python 2 — Group Numbers by Even and Odd
nums = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even:", even)
print("Odd:", odd)
