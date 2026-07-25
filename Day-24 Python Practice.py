# 🐍 Python Question 1 Topic: Remove Duplicates from a List
# Difficulty: Easy
# Question : Write a program to remove duplicate elements from a list while keeping the original order.
# Example : Input - [1, 2, 2, 3, 4, 3, 5], Output - [1, 2, 3, 4, 5]
nums = [1, 2, 2, 3, 4, 3, 5]
result = []
for num in nums:
    if num not in result:
        result.append(num)
print(result)

# 🐍 Python Question 2, Topic: Second Largest Element
# Difficulty: Easy
# Question : Find the second largest number in a list.
# Example : Input - [10, 20, 5, 40, 30], Output - 30
nums = [10, 20, 5, 40, 30]
nums = list(set(nums))
nums.sort()
print(nums[-2])
