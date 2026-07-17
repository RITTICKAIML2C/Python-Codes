# 🐍 Python Question 1, Difficulty: Beginner
# Topic: *arg
# Problem Statement : Write a function that accepts any number of integers using *args and returns their sum.
# Example : Input - 10 20 30 40, Output - 100
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_numbers(10, 20, 30, 40))

# 🐍 Python Question 2, Difficulty: Beginner
# Topic: **kwargs
# Problem Statement - Write a function that accepts student details using **kwargs and prints each key-value pair.
# Example : Input - name = Rahul, age = 20, course = Python
# Output : name : Rahul, age : 20, course : Python
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_details(
    name="Rahul",
    age=20,
    course="Python"
)
