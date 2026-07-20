# 🐍 Python Question 1, Topic: datetime
# Difficulty: Beginner
# Question : Write a program to print the current date and time.
from datetime import datetime
now = datetime.now()
print("Date:", now.date())
print("Time:", now.time().replace(microsecond=0))

# 🐍 Python Question 2, Topic: random
# Difficulty: Beginner
# Question : Generate a random number between 1 and 100.
import random
num = random.randint(1, 100)
print(num)
