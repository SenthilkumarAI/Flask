### 1. Integrate HTML with FLASK
### 2. HTTP verb GET and POST

from flask import Flask # To create WSGI application
from flask import redirect, url_for
# redirect -> to redirect to success page or to fail page
# url_for  -> To create url dynamically.
from flask import render_template # used to render html page
from flask import request # To read POST values on the web page


# create WSGI application
# WSGI application is a standard, that is used to communicate between the web server and the web application that we are trying to create.
app = Flask(__name__)

@app.route("/") # This app.route is a decorator where we will be creating our url. Here our route url "/"
def welcome():
    return render_template("forms.html")


# This is one kind of building url dynamically
# Building Url dynamically
@app.route("/success/<int:score>") # if a datatype is not mentioned it will be treated as string.
# the above is a route decorator which is having /success as the url and i want to append some values, so that i will able to retrieve these values
def success(score):
    res = ""
    if score >=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template("result.html", result=res)
    

@app.route("/fail/<int:score>")
def fail(score):
    return "The Person has failed and the marks is " + str(score)


# i want to create a different page for a person who has passed and different page for a person who has failed.
# How do we do that ?
@app.route("/results/<int:marks>")
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,score=marks))

### Result checker html page
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score = (science + maths + c + data_science)/4
    # res = ""
    # if total_score >=50:
    #     res = "success" # To redirect to success page (2nd function)
    # else:
    #     res = "fail" # To redirect to fail page (3rd function)

    # return redirect(url_for("res",score=total_score))        
    return redirect(url_for("success",score=total_score))        


if __name__ == "__main__":
    app.run(debug=True)

