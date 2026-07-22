# 🐍 Python Question 1, Topic: JSON Module
# Difficulty: Beginner
# Question : Convert a Python dictionary into a JSON string.
import json
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}
json_data = json.dumps(student)
print(json_data)

# 🐍 Python Question 2, Topic: CSV File Handling
# Difficulty: Beginner
# Question : Write student data into a CSV file and read it back.
import csv
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Rahul", 20])
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
