import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt
import pandas as pd


def y_prediction(x_values):
    # Relation used : y = 2*x + 1
    mydata = pd.read_excel('my_linear_data_noisy.xlsx')

    X = mydata.drop('Y', axis = 1)
    y = mydata['Y']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

    regressor = linear_model.LinearRegression()
    regressor.fit(X_train, y_train)

    return regressor.predict(np.array([[x_values]]))

#y_prediction(x_values)
