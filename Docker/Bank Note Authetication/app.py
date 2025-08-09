# from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image


pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# @app.route('/')
def greet():
    return "Welcome You All"

# @app.route('/predict', methods = ["Get"])
def bank_note_auth(variance,skewness,curtosis,entropy):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted values is" + str(prediction)

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=bank_note_auth(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn and have Fun")
        st.text("Built with Streamlit")


if __name__ == "__main__":
    main()