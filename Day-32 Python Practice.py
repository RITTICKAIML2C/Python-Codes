# 🐍 Python Question 1, Difficulty: Easy
# Topic: *args
# Question : Write a function that accepts any number of integers and returns their sum.
# Example : Input : sum_numbers(10, 20, 30, 40)
# Output : 100
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(10, 20, 30, 40))

# 🐍 Python Question 2, Difficulty: Easy–Medium
# Topic: **kwargs
# Question : Write a function that prints all the key-value pairs passed to it.
# Example : Input : student(name="Rahul", age=20, city="Delhi")
# Output : name : Rahul, age : 20, city : Delhi
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student(name="Rahul", age=20, city="Delhi")
