import pandas as pd
import os

os.makedirs("data", exist_ok=True)

data = {
    "Name": [
        "Vanshika",
        "Rahul",
        "Priya",
        "Aman",
        "Neha",
        "Karan",
        "Simran",
        "Arjun",
        "Kashish",
        "Riya"
    ],

    "Course": ["MCA"] * 10,

    "Semester": [1] * 10,

    "Marks": [88, 72, 94, 55, 46, 81, 67, 91, 76, 62],

    "Attendance": [92, 82, 96, 65, 58, 88, 74, 95, 85, 70],

    "Study_Hours": [5, 3, 6, 2, 1, 4, 3, 5, 4, 2],

    "Assignment": [90, 75, 96, 60, 48, 85, 70, 94, 80, 65],

    "Practical": [92, 78, 97, 62, 50, 88, 72, 95, 82, 68],

    "Python_Skill": [92, 70, 95, 50, 40, 85, 65, 90, 78, 60],

    "SQL_Skill": [88, 75, 92, 55, 42, 82, 60, 94, 80, 65],

    "Communication_Skill": [85, 80, 90, 55, 48, 88, 72, 91, 84, 65]
}

df = pd.DataFrame(data)

file_path = "data/students.xlsx"

df.to_excel(file_path, index=False)

print("Excel dataset created successfully!")
print()
print(df)