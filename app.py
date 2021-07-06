
## Create an API to know the Car selling price 

## Import Libraries
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import sklearn
from car_model import car_model_selection, fuel_type_selection, seller_type_selection,trans_type_selection
import numpy as np

### App initiate
app = Flask(__name__)

## Load the rf model
model = pickle.load(open('random_forest_regression_mode.pkl','rb'))

## Create an route for Home Prediction page
@app.route('/',methods = ['GET'])
def Home():
    return render_template('index.html')


## Predict on new data
@app.route("/predict",methods = ['POST'])
def predict():

    data_array = []

    if request.method == 'POST':

        purchase_price = int(request.form["purchase_price"])
        kms_driven = int(request.form['kms_driven'])
        owners = int(request.form["owners"])
        Year = int(request.form["Year"])
        carModel = request.form["carModel"]
        fuelType = request.form["fuelType"]
        seller_type = request.form["seller_type"]
        transmission = request.form["transmission"]
        
        data_array = [purchase_price,kms_driven,owners , abs(2021-Year),]
        
        carlist = car_model_selection(carModel)
        fuelList = fuel_type_selection(fuelType)
        sellerList = seller_type_selection(seller_type)
        transList = trans_type_selection(transmission)

        data_array  = data_array + carlist + fuelList + sellerList + transList
        print(len(data_array))
        print(data_array)
        data_array = np.array([data_array])
        prediction=model.predict(data_array)
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug= True)


