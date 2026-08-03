# 🐍 Python Question 1, Difficulty: Easy
# Topic: Lambda Functions
# Question : Use a lambda function to sort a list of tuples by the second element.
# Example : Input : students = [("Rahul", 85), ("Aman", 72), ("Priya", 91)]
# Output : [('Aman', 72), ('Rahul', 85), ('Priya', 91)]
students = [("Rahul", 85), ("Aman", 72), ("Priya", 91)]
students.sort(key=lambda x: x[1])
print(students)

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: map() and filter()
# Question : Given a list of numbers, print the square of all even numbers.
# Example : Input : nums = [1,2,3,4,5,6], Output : [4, 16, 36]
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x * x,
                  filter(lambda x: x % 2 == 0, nums)))
print(result)
