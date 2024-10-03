# Here we going to learn about
# 1. Building url dynamically


from flask import Flask # To create WSGI application


# create WSGI application
# WSGI application is a standard, that is used to communicate between the web server and the web application that we are trying to create.
app = Flask(__name__)

@app.route("/") # This app.route is a decorator where we will be creating our url. Here our route url "/"
def welcome():
    return "Welcome to my youtube channel"


# This is one kind of building url dynamically
# Building Url dynamically
@app.route("/success/<int:score>") # if a datatype is not mentioned it will be treated as string.
# the above is a route decorator which is having /success as the url and i want to append some values, so that i will able to retrieve these values
def success(score):
    # return "The Person has passed and the marks is " + str(score)
    return "<html><body><h1>The result is passed</h1></body></html>"

@app.route("/fail/<int:score>")
def fail(score):
    return "The Person has failed and the marks is " + str(score)

# Result Checker
@app.route("/results/<int:score>")
def results(score):
    result = ""
    if score < 50:
        result = "Fail"
    else:
        result = "Pass"
    return result

# i want to create a different page for a person who has passed and different page for a person who has failed.
# How do we do that ?

from flask import redirect, url_for
# redirect -> to redirect to success page or to fail page
# url_for  -> To create url dynamically.
@app.route("/response/<int:marks>")
def response(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,score=marks))




if __name__ == "__main__":
    app.run(debug=True)