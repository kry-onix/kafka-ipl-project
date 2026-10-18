import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# IPL MATCH DATA 
#[Runs, Wickets, Overs, RunRate, Wickets Remaining]
x = np.array([
    [40, 0, 4, 10.0, 10],
    [55, 1, 6, 9.16, 9],
    [70, 1, 8, 8.75, 9],
    [85, 2, 10, 8.50, 8],
    [100, 2, 12, 8.33, 8],
    [115, 3, 14, 8.21, 7],
    [130, 3, 16, 8.12, 7],
    [145, 4, 18, 8.05, 6],
    [160, 5, 19, 8.42, 5],
    [175, 6, 20, 8.75, 4],

    [50, 0, 5, 10.0, 10],
    [75, 1, 9, 8.33, 9],
    [95, 2, 11, 8.63, 8],
    [110, 2, 13, 8.46, 8],
    [125, 3, 15, 8.33, 7],
    [140, 4, 17, 8.23, 6],
    [155, 5, 18, 8.61, 5],
    [170, 5, 20, 8.50, 5]
])

#Final Score
y = np.array([
    165,
    175,
    180,
    185,
    195,
    200,
    210,
    215,
    225,
    235,

    175,
    185,
    190,
    200,
    205,
    215,
    225,
    230
])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("R2 Score: ", r2_score(y_test, y_pred))
joblib.dump(model, "model.pkl")
