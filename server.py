from flask import Flask, render_template, request, redirect, session, flash
from flask_app.config.mysqlconnection import connectToMySQL



app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location =  data['location']
        self.language = data['language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_person(cls,  data):
        query = """INSERT INTO dojos (name, location, language ) 
        VALUES (%(name)s, %(language)s, %(location)s);"""
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey_schema').query_db( query, data )

    @staticmethod
    def validate_dojo(person):
        is_valid = True # we assume this is true
        if len(person['name']) < 5:
            flash("Name must be at least 5 characters.")
            is_valid = False
        if len(person['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False
        if len(person['language']) < 0:
            flash("Language must be greater than 0 characters")
            is_valid = False
        return is_valid

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reset',methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/process',methods=['POST'])
def userinput():
    if not Dojo.validate_dojo(request.form):
        return  redirect('/')
    else:
        data = {
            'name' : request.form["name"],
            'location' : request.form["location"],
            'language' : request.form["language"],

        }
        Dojo.create_person(data)
        # session['name']=request.form.get("name")
        # session['location']=request.form.get("location")
        # session['language']=request.form.get("language")
        # session['comments']=request.form.get("comments")
        # using both session and database data storage here 
    return  redirect('/')


@app.route('/results')
def display():
    return render_template('index2.html')




if __name__ == "__main__":
    app.run(debug=True)