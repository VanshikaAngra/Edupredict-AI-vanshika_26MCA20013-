from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)

from database import (
    create_database,
    add_student,
    get_students,
    get_student,
    get_student_count,
    delete_student
)

from analysis import (
    calculate_performance,
    get_performance_level,
    get_risk_level,
    get_excel_statistics
)

from prediction import predict_performance

from career import (
    recommend_career,
    skill_gap
)

from visualization import (
    create_performance_chart,
    create_skill_chart
)


app = Flask(__name__)

create_database()


@app.route("/")
def index():

    students = get_students()

    count = get_student_count()

    return render_template(
        "index.html",
        students=students,
        count=count
    )


@app.route(
    "/add",
    methods=["GET", "POST"]
)
def add():

    if request.method == "POST":

        data = (

            request.form["name"],

            int(
                request.form["age"]
            ),

            request.form["course"],

            int(
                request.form["semester"]
            ),

            float(
                request.form["marks"]
            ),

            float(
                request.form["attendance"]
            ),

            float(
                request.form["study_hours"]
            ),

            float(
                request.form[
                    "assignment_score"
                ]
            ),

            float(
                request.form[
                    "practical_score"
                ]
            ),

            float(
                request.form[
                    "python_skill"
                ]
            ),

            float(
                request.form[
                    "sql_skill"
                ]
            ),

            float(
                request.form[
                    "communication_skill"
                ]
            )
        )

        add_student(data)

        return redirect(
            url_for("index")
        )

    return render_template(
        "add_student.html"
    )


@app.route(
    "/student/<int:student_id>"
)
def student(student_id):

    student_data = get_student(
        student_id
    )

    if student_data is None:

        return (
            "Student not found",
            404
        )

    score = calculate_performance(

        student_data[5],
        student_data[6],
        student_data[7],
        student_data[8],
        student_data[9]
    )

    level = get_performance_level(
        score
    )

    risk = get_risk_level(

        student_data[5],
        student_data[6],
        student_data[7]
    )

    predicted_score = predict_performance(

        student_data[5],
        student_data[6],
        student_data[7],
        student_data[8],
        student_data[9]
    )

    careers = recommend_career(

        student_data[10],
        student_data[11],
        student_data[12]
    )

    gaps = skill_gap(

        student_data[10],
        student_data[11],
        student_data[12]
    )

    create_performance_chart(

        student_data[5],
        student_data[6],
        student_data[8],
        student_data[9],
        student_id
    )

    create_skill_chart(

        student_data[10],
        student_data[11],
        student_data[12],
        student_id
    )

    return render_template(

        "student.html",

        student=student_data,

        score=score,

        level=level,

        risk=risk,

        predicted_score=predicted_score,

        careers=careers,

        gaps=gaps
    )


@app.route("/dashboard")
def dashboard():

    students = get_students()

    stats = get_excel_statistics()

    return render_template(

        "dashboard.html",

        students=students,

        stats=stats
    )


@app.route(
    "/delete/<int:student_id>"
)
def delete(student_id):

    delete_student(
        student_id
    )

    return redirect(
        url_for("index")
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )