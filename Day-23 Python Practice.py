# 🐍 Python Question 1, Topic: Anagram
# Difficulty: Easy
# Question : Write a program to check whether two strings are anagrams.
# Example : Input - listen, silent , Output : True
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(sorted(s1) == sorted(s2))

# 🐍 Python Question 2, Topic: List Rotation
# Difficulty: Easy
# Question : Rotate a list to the right by k positions.
# Example : Input - nums = [1,2,3,4,5], k = 2, Output - [4,5,1,2,3]
nums = [1,2,3,4,5]
k = 2
k %= len(nums)
nums = nums[-k:] + nums[:-k]
print(nums)
