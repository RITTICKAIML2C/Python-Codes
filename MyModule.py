person1 = {'name' : 'Keshav', 'age' : 16}

def say_hello(name):
    return print(f"Hello, {name}, Kaise ho?")

def say_bye(name):
    return print(f"Bye {name}, Take care!")

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result += i
    return result 

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
