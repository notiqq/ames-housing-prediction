import numpy as np
import scipy
import matplotlib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import csv
import os

class Model:

    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, train_file_name = "/train.csv" ):
        self.train_file_name = self.path + train_file_name

    def predict(self):
        ## Select the predictors that will be used
        # predictors = ["YearBuilt"]  (Model 1)
        predictors = ["YearBuilt", "YearRemodAdd", "YrSold", "SaleType"] # Model 2

        ## Make Training Data
        train = pd.read_csv(self.train_file_name)
        y = np.array(train['SalePrice'])  # extract response variable

        train = train[predictors]
        train = pd.get_dummies(train)
        x = np.array(train)#.reshape((-1, 1))  # predictors

        ## Make Testing Data
        test = pd.read_csv(self.path + "/test.csv")
        ids = test['Id']
        test = test[predictors]
        test = pd.get_dummies(test)

        ## Calculate Baseline Metric
        null_rmse = np.sqrt(np.mean((np.mean(y) - y)**2))

        ## Fit Random Forest Model
        rf_mdl = RandomForestRegressor(n_estimators = 1000, random_state = 42)
        rf_mdl.fit(x, y)

        ## Caculate the training RMSE
        train_pred = rf_mdl.predict(x)
        train_rmse = np.sqrt(np.mean((train_pred - y)**2))

        ## Predict the response with the testin data
        test_data = np.array(test)#.reshape((-1, 1))
        test_pred = rf_mdl.predict(test_data)

        results = []

        for id in range(len(test_pred)):
            results.append([ids[id], test_pred[id]])

        return results