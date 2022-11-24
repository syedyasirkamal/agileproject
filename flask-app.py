#          Import some packages               #
###############################################
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from app.forms import signupForm
from flask_mysqldb import MySQL

###############################################
#          Define flask app                   #from flask-app import db, Contact
###############################################



app = Flask(__name__)
app.secret_key = 'the random string'


app.config['MYSQL_HOST'] = 'db-mysql-nyc1-60644-do-user-12947735-0.b.db.ondigitalocean.com'
app.config['MYSQL_USER'] = 'doadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_DYDcrmshVEp0wf2PtRu'
app.config['MYSQL_PORT'] = 25060
app.config['MYSQL_DB'] = 'defaultdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/createdatabase')
def index():
    # Creating a connection cursor
    cursor = mysql.connection.cursor()

    # Executing SQL Statements
    #cursor.execute('''CREATE TABLE contact (id INTEGER, name VARCHAR(50), email VARCHAR(100), message VARCHAR(2000), date_created TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL, PRIMARY KEY (id))''')

    # Saving the Actions performed on the DB
    mysql.connection.commit()

    # Closing the cursor
    cursor.close()
    return 'done!'


###############################################
#       Render Contact page                   #
###############################################
@app.route('/3', methods=['GET'])
def index2():
    return render_template("index.html")


@app.route('/signup', methods=["GET", "POST"])
def home():
    cform = signupForm()
    if cform.validate_on_submit():
        print(f"Name:{cform.name.data}, E-mail:{cform.email.data}, message: {cform.message.data}")
    return render_template("signup.html", form=cform)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
    cform = signupForm()
    if cform.validate_on_submit():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            cursor = mysql.connection.cursor()
            database = "INSERT INTO contact (name, email, message) VALUES (%s, %s, %s)"
            val = (name, email, message)
            cursor.execute(database,val)
            mysql.connection.commit()
            cursor.close()
            return f"Done!!"
    else:
        return render_template("signup.html", form=cform)


###############################################
#                Run app                      #
###############################################

if __name__ == '__main__':
    app.debug = True
    app.run()