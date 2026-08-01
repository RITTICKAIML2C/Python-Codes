# 🐍 Python Question 1, Difficulty: Easy
# Topic: any() and all()
# Question : Check if all numbers in a list are positive.
# Example : Input : nums = [2, 5, 8, 10]
# Output : True
nums = [2, 5, 8, 10]
print(all(num > 0 for num in nums))

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: List Comprehension
# Question : Create a list containing the squares of even numbers from 1 to 10.
# Example : Output : [4, 16, 36, 64, 100]
result = [x * x for x in range(1, 11) if x % 2 == 0]
print(result)
