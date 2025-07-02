## Integrate HTML with Flask
## HTTP verb GET and POST

## Jinja2 template engine
"""
{%...%} conditions, for loops statements
{{   }} expressions to print output
{#...#} this is for comments
"""


# Import necessary functions from the Flask library
from flask import Flask, redirect, url_for, render_template, request

# Create an instance of the Flask application
# This initializes the Flask app
app = Flask(__name__)

# This is the home route. When a user visits the root URL ('/'), this function is triggered.
@app.route('/')
def welcome():
    # It renders the index.html file located inside the 'templates' folder
    return render_template("index.html")

# This route is called when a user is redirected to a "success" page with a score.
# The '<int:score>' means this route accepts an integer value from the URL.
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res ="PASS"
    else:
        res = "FAIL"    
    exp = {"score": score, "res":res}
    return render_template("result.html", result=exp)
    # res = ""
    # # Check if the score is 50 or more
    # if score >= 50:
    #     res = "PASS"  # If score is 50 or more, return PASS
    # else:
    #     res = "FAIL"  # If score is below 50, return FAIL

    # # Render result.html and pass the result (PASS or FAIL) into the template
    # return render_template("result.html", result=res)

# This route is called when a user fails (score < 50)
@app.route('/fail/<int:score>')
def fail(score):
    # Simply returns a message showing the score and that the person failed
    return "The Person has failed the exam and the mark is " + str(score)

# This route decides whether the result is "pass" or "fail"
# It receives the score as a parameter and redirects to either the /success or /fail route
@app.route('/results/<int:marks>')
def results(marks):
    if marks < 50:
        result = "fail"      # If marks are below 50, redirect to the 'fail' route
    else:
        result = "success"   # If marks are 50 or above, redirect to the 'success' route

    # Redirects to the appropriate route by calling url_for with the name of the route and passing score
    return redirect(url_for(result, score=marks))

# This route handles the HTML form submission
# It accepts both GET and POST requests
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0  # Initialize total score

    # Only process the form if it's a POST request (form submitted)
    if request.method == 'POST':
        # Retrieve values from the form fields and convert them to float
        science = float(request.form["science"])
        math = float(request.form["maths"])
        c = float(request.form["c"])
        data_science = float(request.form["datascience"])
        civil_engr = float(request.form["civilengineer"])

        # Calculate average score from the 5 subjects
        total_score = (science + math + c + data_science + civil_engr) / 5

    # Alternative approach: You had this commented code that also redirects based on score

    # res = ""
    # if total_score >= 50:
    #     res = "success"     # If score is 50 or more, set res to 'success'
    # else:
    #     res = "fail"        # Otherwise, set res to 'fail'

    # This line below would dynamically redirect based on the result (success or fail)
    # return redirect(url_for(res, score=int(total_score)))  ❌ This version works only if score is int

    # ✅ Final working version: Always redirect to 'success' route (you can improve it later to include fail)
    return redirect(url_for('success', score=total_score))  # score can be float; it still works

# This block ensures the app runs only if this script is executed directly
if __name__ == '__main__':
    # debug=True gives helpful error messages and auto-reloads the server on code changes
    app.run(debug=True)
