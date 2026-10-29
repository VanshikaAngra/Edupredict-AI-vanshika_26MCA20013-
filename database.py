import sqlite3
import os


DATABASE = "database/edupredict.db"


def get_connection():

    return sqlite3.connect(DATABASE)


def create_database():

    os.makedirs(
        "database",
        exist_ok=True
    )

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            age INTEGER NOT NULL,

            course TEXT NOT NULL,

            semester INTEGER NOT NULL,

            marks REAL NOT NULL,

            attendance REAL NOT NULL,

            study_hours REAL NOT NULL,

            assignment_score REAL NOT NULL,

            practical_score REAL NOT NULL,

            python_skill REAL NOT NULL,

            sql_skill REAL NOT NULL,

            communication_skill REAL NOT NULL
        )
    """)

    conn.commit()

    conn.close()


def add_student(data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (

            name,
            age,
            course,
            semester,
            marks,
            attendance,
            study_hours,
            assignment_score,
            practical_score,
            python_skill,
            sql_skill,
            communication_skill

        )

        VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, data)

    conn.commit()

    conn.close()


def get_students():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students ORDER BY id DESC"
    )

    students = cursor.fetchall()

    conn.close()

    return students


def get_student(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    return student


def get_student_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count


def delete_student(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    conn.close()