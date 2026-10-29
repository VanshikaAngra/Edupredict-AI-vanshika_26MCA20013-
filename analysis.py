import numpy as np
import pandas as pd


def calculate_performance(
    marks,
    attendance,
    study_hours,
    assignment_score,
    practical_score
):
    study_score = min(study_hours * 20, 100)

    values = np.array([
        marks,
        attendance,
        assignment_score,
        practical_score,
        study_score
    ])

    performance_score = (
        values[0] * 0.40 +
        values[1] * 0.20 +
        values[2] * 0.10 +
        values[3] * 0.15 +
        values[4] * 0.15
    )

    return round(float(performance_score), 2)


def get_performance_level(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Needs Improvement"


def get_risk_level(
    marks,
    attendance,
    study_hours
):

    if marks < 50 and attendance < 65:
        return "High Risk"

    elif marks < 60 or attendance < 70 or study_hours < 2:
        return "Medium Risk"

    return "Low Risk"


def calculate_statistics(values):

    values = np.array(values)

    return {
        "mean": round(float(np.mean(values)), 2),
        "median": round(float(np.median(values)), 2),
        "maximum": round(float(np.max(values)), 2),
        "minimum": round(float(np.min(values)), 2),
        "std": round(float(np.std(values)), 2)
    }


def load_excel_data():

    return pd.read_excel(
        "data/students.xlsx"
    )


def get_excel_statistics():

    df = load_excel_data()

    return {
        "students": len(df),
        "average_marks": round(
            float(df["Marks"].mean()), 2
        ),
        "highest_marks": round(
            float(df["Marks"].max()), 2
        ),
        "lowest_marks": round(
            float(df["Marks"].min()), 2
        ),
        "average_attendance": round(
            float(df["Attendance"].mean()), 2
        )
    }