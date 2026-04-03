import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from preprocess import preprocess_data

def EDA():
    df = preprocess_data()
    train = df[:int(0.6*len(df))]
    valid = df[int(0.6*len(df)):int(0.8*len(df))]
    test = df[int(0.8*len(df)):]
    x_train = train[['month_num']]
    # print(type(x_train))
    y_train = train['amount']
    x_valid = valid[['month_num']]
    y_valid = valid['amount']
    x_test = test[['month_num']]
    y_test = test['amount']
    # print(y_train.head())

    return x_train, y_train, x_valid, y_valid, x_test, y_test