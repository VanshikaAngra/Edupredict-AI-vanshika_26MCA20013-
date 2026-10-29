import numpy as np

from sklearn.ensemble import RandomForestRegressor


def train_model():

    X = np.array([

        [95, 98, 6, 95, 96],
        [90, 95, 5, 90, 92],
        [85, 90, 4, 85, 88],
        [80, 88, 4, 80, 85],
        [75, 85, 3, 75, 80],
        [70, 80, 3, 70, 75],
        [65, 75, 2, 65, 70],
        [60, 70, 2, 60, 65],
        [55, 65, 1, 55, 60],
        [45, 55, 1, 45, 50],
        [40, 50, 1, 40, 45]

    ])

    y = np.array([
        97,
        94,
        89,
        85,
        80,
        75,
        69,
        64,
        59,
        48,
        43
    ])

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X,
        y
    )

    return model


def predict_performance(
    marks,
    attendance,
    study_hours,
    assignment_score,
    practical_score
):

    model = train_model()

    data = np.array([[
        marks,
        attendance,
        study_hours,
        assignment_score,
        practical_score
    ]])

    prediction = model.predict(data)

    return round(
        float(prediction[0]),
        2
    )