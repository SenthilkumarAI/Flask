from flask import Flask

# create WSGI application
# WSGI application is a standard that is used to communicate between the web server and the web application that we are trying to create.
app = Flask(__name__)


# decorator with 2 parameters 1. rule, 2. options
@app.route("/") # 1. rule : it is going to have a string value which will specify the url that i am going to go to that specific webpage
def welcome():
    return "My name is senthilkumar. Hi, Hello please subscribe to me"

# lines 7,8,9 denotes like whenever a decorator is defined like (line : 7) and a function is defined beneath this(line : 8 and 9)
# that basically means that whenever i go into this particular page ("/") mentioned in the decorator, the below defined function will be triggered automatically.


@app.route("/members")
def re_welcome():
    return "My first flask app"


if __name__ == "__main__":
    app.run(debug=True)