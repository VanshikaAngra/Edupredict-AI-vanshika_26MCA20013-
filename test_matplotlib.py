import matplotlib.pyplot as plt

students = [
    "Vanshika",
    "Rahul",
    "Priya",
    "Aman",
    "Neha"
]

marks = [
    88,
    72,
    94,
    55,
    46
]

plt.figure(figsize=(8, 5))

plt.bar(
    students,
    marks
)

plt.title(
    "Student Marks"
)

plt.xlabel(
    "Students"
)

plt.ylabel(
    "Marks"
)

plt.ylim(0, 100)

plt.grid(
    axis="y",
    linestyle="--"
)

plt.tight_layout()

plt.savefig(
    "static/charts/test_chart.png"
)

plt.close()

print(
    "Matplotlib chart created successfully!"
)