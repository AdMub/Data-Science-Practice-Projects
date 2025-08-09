from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def greet():
    return "Welcome You All"

@app.route('/predict')
def bank_note_auth():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted values is" + str(prediction)

@app.route('/predict_file', methods = ["POST"])
def bank_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)

    return f"The predicted values for the csv files is {[int(x) for x in prediction]}" 


if __name__ == "__main__":
    app.run(debug=True)