from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reset',methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/process',methods=['POST'])
def userinput():
    session['name']=request.form.get("name")
    session['city']=request.form.get("city")
    session['language']=request.form.get("language")
    session['comments']=request.form.get("comments")
    return redirect('/results')

@app.route('/results')
def display():
    return render_template('index2.html')




if __name__ == "__main__":
    app.run(debug=True)