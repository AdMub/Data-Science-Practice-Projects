# Tutorial 1
# msg = "welcome to AdMub page"
# print(msg) 
# print("What is your name")

# # Tutorial 2 (Sample Flask Web Application Skeleton)
# # Import flask library
# from flask import Flask  

# #  WSGI Application (Standard to communicate btw web server and application)
# app = Flask(__name__)     # Initilize flask

# # Create decorator coming along with function
# @app.route('/')   # specify url that I am actually going into webpage
# def welcome():
#     return "Welcome To AdMub Page. Please, Please Introduce yourself"

# # Function should not be the same along decorator or url so that it won't get confuse
# @app.route('/members')   # specify url that I am actually going into webpage
# def members():
#     return "Welcome To AdMub Page."


# if __name__=="__main__":
#     app.run(debug=True)


# Tutorial 3 (Building Url Dynamically)
## Flask Variable Rules and URL Building

# # Import necessary functions from the Flask library
# from flask import Flask, redirect, url_for

# # Create an instance of the Flask application
# app = Flask(__name__)

# # This is the home route. When a user visits the root URL ('/'), this function is called.
# @app.route('/')
# def welcome():
#     return "Welcome To AdMub Page"

# # This route is triggered when the result is a pass (score >= 50).
# # '<int:score>' allows dynamic input from the URL (only integers).
# @app.route('/success/<int:score>')
# def success(score):
#     return "The Person has passed the exam and the mark is " + str(score)

# # This route is triggered when the result is a fail (score < 50).
# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The Person has failed the exam and the mark is " + str(score)

# # This route checks the result and redirects to the appropriate route (pass or fail)
# @app.route('/results/<int:marks>')
# def results(marks):
#     if marks < 50:
#         result = "fail"     # If marks are below 50, redirect to the 'fail' route
#     else:
#         result = "success"  # If marks are 50 or more, redirect to the 'success' route

#     # This line redirects to the selected route with the marks as a parameter
#     return redirect(url_for(result, score=marks))

# # This tells Python to run the app in debug mode when executing this file
# if __name__ == '__main__':
#     app.run(debug=True)
