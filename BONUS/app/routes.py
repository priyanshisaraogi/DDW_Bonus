from flask import render_template, flash, session
from .forms import DataForm
from app import application
import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from app.library import library
import os

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='AgriEcon Predictor')

@application.route('/about_us')
def aboutus():
    return render_template('about_us.html', title='About Us')

@application.route('/predictor', methods=['GET', 'POST'])
def predictor():
    
    #chooses a data size! e.g. if 0.2 input, we only use 0.2 of the data
    dataForm = DataForm()
    if dataForm.validate_on_submit():
        ddw = pd.read_csv("app/library/DDW.csv")
        predictors = ["Health Index","Poverty","Malnourished Children"]
        predicted = ["GNI"]
        x = library.select_columns(ddw,predictors)
        y = library.select_columns(ddw,predicted)
        if dataForm.dataSize.data == 1:
            x_train = x
            y_train = y
        else:
            x_train, x_test, y_train, y_test = library.splitData(x,y,dataForm.dataSize.data)
        x_train_scaled,means,stds = library.normalize_z(x_train)
        coefficients, intercept, model = library.MultipleLinearRegression(x_train_scaled, y_train)

        #normalize the input data!
        health = (dataForm.health_index.data-means["Health Index"])/stds["Health Index"]
        poverty = (dataForm.poverty.data-means["Poverty"])/stds["Poverty"]
        mC = (dataForm.malnourished_children.data-means["Malnourished Children"])/stds["Malnourished Children"]
        predictedY = intercept[0] + (coefficients[0][0]*health) + (coefficients[0][1]*poverty) + (coefficients[0][2]*mC)

        #plotting an image out! saves image into library folder
        plt.scatter(model.predict(x_train_scaled), y_train)
        plt.xlabel('Y predicted')
        plt.ylabel('Y actual')
        plt.title('Accuracy of Current Model')

        img_path = os.path.join(os.path.dirname(__file__), 'static', f'scatter_plot.png')
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        plt.savefig(img_path, format='png')
        plt.close()
        scatterPlot=True

        #get RMSE of train values
        trainr2, trainRMSE = library.testModel(x_train_scaled,y_train,model)

        #get RMSE of test values for your current model!
        if dataForm.dataSize.data != 1:
            x_test_scaled = library.normalize_z(x_test,means,stds)[0]
            r2, RMSE = library.testModel(x_test_scaled,y_test,model)
            return render_template('predictor.html', trainr2=trainr2, trainRMSE=trainRMSE, boxPlot=True, scatterPlot=True,r2=r2,RMSE=RMSE,dataForm=dataForm,coefficients=coefficients,intercept=intercept,predictedY=predictedY,title='Predict Subsidies')
        
        #no test data to get RMSE on new data
        elif dataForm.dataSize.data == 1:
            return render_template('predictor.html',trainr2=trainr2, trainRMSE=trainRMSE, boxPlot=True, scatterPlot=True,dataForm=dataForm,coefficients=coefficients,intercept=intercept,predictedY=predictedY,title='Predict Subsidies')
        
    return render_template('predictor.html', dataForm=dataForm,title='Modelling and Analysis')