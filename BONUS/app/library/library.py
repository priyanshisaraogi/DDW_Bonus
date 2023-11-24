#import libraries
#from org.transcrypt.stubs.browser import *
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Selects columns from DataFrame
def select_columns(df, listColumns):
    newData = pd.DataFrame()
    #dropna() removes rows with None values
    return df.loc[:,listColumns].dropna()

#splits Data
def splitData(x,y,number=1):
    from sklearn.model_selection import train_test_split
    return train_test_split(x, y, train_size=number)

#Z-normalization, to scale the data for multiple linear regression
def normalize_z(dfin, columns_means=None, columns_stds=None):
    if columns_means is None:
        columns_means = dfin.mean(axis = 0)
    if columns_stds is None:
        columns_stds = dfin.std(axis = 0)
    dfout = (dfin - columns_means) / columns_stds
    return dfout, columns_means, columns_stds

#multiple linear regression
def MultipleLinearRegression(x,y):
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(x,y)
    return model.coef_,model.intercept_,model

#Z-normalization, to scale the data for multiple linear regression
def normalize_z(dfin, columns_means=None, columns_stds=None):
    if columns_means is None:
        columns_means = dfin.mean(axis = 0)
    if columns_stds is None:
        columns_stds = dfin.std(axis = 0)
    dfout = (dfin - columns_means) / columns_stds
    return dfout, columns_means, columns_stds

#function for testing the model: returns r2 and RMSE on test data
#xtest and ytest already have columns extracted
def testModel(x_test,y_test,model):
    from sklearn.metrics import r2_score, mean_squared_error
    predicted = model.predict(x_test)
    return r2_score(y_test, predicted), mean_squared_error(y_test,predicted)






