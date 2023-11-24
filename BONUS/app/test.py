import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from library import library



ddw = pd.read_csv("library/DDW.csv")
predictors = ["Health Index","Poverty","Malnourished Children"]
predicted = ["GNI"]
x = library.select_columns(ddw,predictors)
y = library.select_columns(ddw,predicted)
x_train, x_test, y_train, y_test = library.splitData(x,y,0.3)
x_train_scaled,means,stds = library.normalize_z(x_train)
coefficients, intercept = library.MultipleLinearRegression(x_train_scaled, y_train)