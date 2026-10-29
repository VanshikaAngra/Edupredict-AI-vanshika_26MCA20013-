import os

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def create_performance_chart(
    marks,
    attendance,
    assignment,
    practical,
    student_id
):

    os.makedirs(
        "static/charts",
        exist_ok=True
    )

    categories = [
        "Marks",
        "Attendance",
        "Assignment",
        "Practical"
    ]

    values = [
        marks,
        attendance,
        assignment,
        practical
    ]

    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        categories,
        values,
        width=0.6
    )

    plt.title(
        "Student Performance Analysis"
    )

    plt.xlabel(
        "Performance Parameters"
    )

    plt.ylabel(
        "Score"
    )

    plt.ylim(0, 100)

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.4
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() +
            bar.get_width() / 2,
            height + 1,
            f"{height:.0f}",
            ha="center"
        )

    plt.tight_layout()

    filename = (
        f"static/charts/"
        f"student_{student_id}.png"
    )

    plt.savefig(filename)

    plt.close()

    return filename


def create_skill_chart(
    python_skill,
    sql_skill,
    communication_skill,
    student_id
):

    os.makedirs(
        "static/charts",
        exist_ok=True
    )

    skills = [
        "Python",
        "SQL",
        "Communication"
    ]

    values = [
        python_skill,
        sql_skill,
        communication_skill
    ]

    plt.figure(figsize=(8, 5))

    bars = plt.bar(
        skills,
        values,
        width=0.6
    )

    plt.title(
        "Technical Skill Analysis"
    )

    plt.xlabel(
        "Skills"
    )

    plt.ylabel(
        "Skill Level"
    )

    plt.ylim(0, 100)

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.4
    )

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() +
            bar.get_width() / 2,
            height + 1,
            f"{height:.0f}",
            ha="center"
        )

    plt.tight_layout()

    filename = (
        f"static/charts/"
        f"skills_{student_id}.png"
    )

    plt.savefig(filename)

    plt.close()

    return filename