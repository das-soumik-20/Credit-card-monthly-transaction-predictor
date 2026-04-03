from model import predict
from sklearn.metrics import mean_absolute_percentage_error as mape , mean_absolute_error as mae

model, x_test, y_test = predict()
y_pred = model.predict(x_test)
error = mae(y_test, y_pred)
percent_error = mape(y_test, y_pred)

print(f"Perecentage error on test data set is {percent_error * 100:.2f}%")