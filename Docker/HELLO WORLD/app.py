## flask app from hello world

# Import the Flask class from the flask module
from flask import Flask
import os

# Create an instance of the Flask class
app = Flask(__name__)     # __name__ helps Flask know where to look for resources like static files and templates.

@app.route('/', methods=['GET'])
def home():
    return "Hello World from Docker!"

if __name__== "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)