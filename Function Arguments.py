# Arguments in Functions

# 1. Required Arguments (single?multiple arguments)
def greetings(name):    # name is a parameter
    print("Hello", name, "!")
greetings("Madhav")     # madhav is arguments

def intro(course_name, instructor_name):
    print("Welcome to", course_name, "course by", instructor_name)
intro("Python", "Rishabh")

# 2. Default Arguments

def greetings(name = "World"):  #"World" is a default value
    print("Hello", name, "!")
greetings()     # runs without error using default value
greetings("Rishabh")

# 3. Keyword Arguments (name arguments)

def divide(a,b):
    return a / b
result1 = divide(100,20)    # positional arguments
print(result1)

result2 = divide(b = 100, a = 20)
print(result2)

# 4. Arbitrary Argument
# Arbitrary Positional Arguments (*args)
# Stores arguments as tuples

def add_numbers(*args):
    print(type(args))
    return sum(args)
op = add_numbers(1,2,3,4)   # Variable no. of arguments
print(op)

def greetings2(*names):
    for name in names:
        print(f"Hello, {name}!")
greetings2("Madhav", "Rishabh", "Teddy")

# Arbitrary Keyword Arguments (**Kwargs)
# Stores arguments as dictionary

def print_details(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_details(name = "Madhav", age = 26, city = "Delhi")
