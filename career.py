def recommend_career(
    python_skill,
    sql_skill,
    communication_skill
):

    careers = []

    if python_skill >= 75 and sql_skill >= 70:
        careers.append(
            "Data Analyst"
        )

    if python_skill >= 80:
        careers.append(
            "Python Developer"
        )

    if sql_skill >= 80:
        careers.append(
            "Database Developer"
        )

    if (
        communication_skill >= 80
        and sql_skill >= 70
    ):
        careers.append(
            "Business Analyst"
        )

    if (
        python_skill >= 75
        and communication_skill >= 70
    ):
        careers.append(
            "Data Scientist"
        )

    if not careers:
        careers.append(
            "Improve technical and communication skills"
        )

    return careers


def skill_gap(
    python_skill,
    sql_skill,
    communication_skill
):

    gaps = []

    if python_skill < 70:
        gaps.append("Python")

    if sql_skill < 70:
        gaps.append("SQL")

    if communication_skill < 70:
        gaps.append("Communication")

    return gaps