# Modules in Python
# single py file 

# create a module mymodule.py file 
# use mymodule file

import Mymodule
Mymodule.say_hello('Madhav')
Mymodule.say_bye('Rishabh')

# import/use specific part of code
from Mymodule import person1
print(person1['age'])

# Package : collection modules/py files + __init__.py

# library : collection of modules and packages 
# inbuilt library
import math

A = 16
print(math.sqrt(A))

# import specific function from library 
# from math import factorial
B = 4
print(factorial(B))

# installed new modules/library
# pip install <library_name>
import seaborn as sb

