from exploratory_data_analysis import EDA
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import  RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error as mape


def predict():
    x_train, y_train, x_valid, y_valid, x_test, y_test = EDA()
    lr = LinearRegression()
    rf = RandomForestRegressor(n_estimators=200, max_depth=5 , random_state = 42)

    lr.fit(x_train, y_train)
    rf.fit(x_train, y_train)

    y_pred1 = lr.predict(x_valid)
    y_pred2 = rf.predict(x_valid)

    error1 = mape(y_valid, y_pred1)
    error2 = mape(y_valid, y_pred2)

    print(f"Absolute error by linear regression: {error1*100:.2f}%")
    print(f"Absolute error by Random Forest regression : {error2*100:.2f}%")

    if error1>error2:
        print("Random forest regressor is better")
        best_model = rf
    else:
        print("Linear Regression is better")
        best_model = lr
    return best_model, x_test, y_test