## please see this instead of app.py

# creating a simple flask application

from flask import Flask,render_template,request,redirect,url_for

# object or instance intialize which will also be our entry point

app=Flask(__name__)

## whenever we want to create a webpage we create different url, homepage for that we use decorators.
@app.route('/')                   # (/) is  a homepage, @app.route is for assigining different different url
def home():
    return "Welcome to my first flask app"

@app.route('/index')
def index():
    return render_template('index.html')             ## we use for returning aa webpage so we use rendere

@app.route('/welcome')
def welcome():
    return "<h1>My flask app</h1>"                # we are also returning html

@app.route('/success/<int:score>')
def success(score):
    return "the person is passed and the score is"+str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "the person is fail and the score is"+str(score)


@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3

        result=""
        if average_marks>=50:
            result="success"
        else:
            result="fail"

        #return redirect(url_for(result,score=average_marks))     ## whenever we want to redirect in the route(in this practiceapp.py) we will use this
        return render_template('result.html', result=average_marks)  ## whenever we want to redirect to html page we will use this

        
if __name__=='__main__':             ## this the entry point(means that app is the entry point, so we initailize it ==main)
    app.run(debug=True)               # it will run the app.py,  run is the method
