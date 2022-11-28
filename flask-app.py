#          Import some packages               #
###############################################
import os
from flask import Flask, render_template, request, redirect, url_for
from app.forms import signupForm, trialForm
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_mail import Mail, Message


###############################################
#          Define flask app                   #from flask-app import db, Contact
###############################################

app = Flask(__name__,template_folder='templates')
app.secret_key = 'the random string'
Bootstrap(app)
datepicker(app)


###############################################
#         Database connection info
###############################################


app.config['MYSQL_HOST'] = 'db-mysql-nyc1-60644-do-user-12947735-0.b.db.ondigitalocean.com'
app.config['MYSQL_USER'] = 'doadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_DYDcrmshVEp0wf2PtRu'
app.config['MYSQL_PORT'] = 25060
app.config['MYSQL_DB'] = 'defaultdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

###############################################
#         Flask Mail App
###############################################

mail = Mail(app)  # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chidopromos@gmail.com'
app.config['MAIL_PASSWORD'] = 'onzzqwzrobdsmcna'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/createdatabase')
def createdatabase():
    # Creating a connection cursor
    cursor = mysql.connection.cursor()

    # Executing SQL Statements
    #cursor.execute('''CREATE TABLE contact (id INTEGER, name VARCHAR(50), email VARCHAR(100), message VARCHAR(2000), date_created TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL, PRIMARY KEY (id))''')
    cursor.execute('''CREATE TABLE trial (id INTEGER, firstname VARCHAR(50), lastname VARCHAR(50), email VARCHAR(100), tutor VARCHAR(100), datetime  DATETIME, date_created TIMESTAMP  DEFAULT CURRENT_TIMESTAMP NOT NULL, PRIMARY KEY (id))''')

    # Saving the Actions performed on the DB
    mysql.connection.commit()

    # Closing the cursor
    cursor.close()
    return 'done!'


###############################################
#       Render Contact page                   #
###############################################
@app.route('/', methods=['GET'])
def index():
    return render_template("main-container.html")

@app.route('/trial', methods=["GET", "POST"])
def trial():
    cform = trialForm()
    return render_template("trial.html", form=cform)

@app.route('/signup', methods=["GET", "POST"])
def home():
    cform = signupForm()
    return render_template("signup.html", form=cform)


@app.route('/signup/submit', methods=['POST', 'GET'])
def signupsubmit():
    if request.method == 'GET':
        return "Login via the login Form"
    cform = signupForm()
    if cform.validate_on_submit():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            cursor = mysql.connection.cursor()
            database = "INSERT INTO contact (name, email) VALUES (%s, %s)"
            val = (name, email)
            cursor.execute(database,val)
            mysql.connection.commit()
            cursor.close()

            msg = Message(
                'Thank you for joining ChidoLingo Promos Mailing List',
                sender='chidopromos@gmail.com',
                recipients=[email]
            )
            msg.html = render_template(template_name_or_list="email-maillist.html")
            mail.send(msg)
            return render_template("signupconfirmation.html", name=name, email=email)

    else:
        return render_template("signup.html", form=cform)


@app.route('/trial/submit', methods=['POST', 'GET'])
def trialsubmit():
    if request.method == 'GET':
        return "Login via the login Form"
    cform = trialForm()
    if cform.validate_on_submit():
        if request.method == 'POST':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            tutor = request.form['tutor']
            datetime = request.form['datetime']
            cursor = mysql.connection.cursor()
            database = "INSERT INTO trial (firstname, lastname, email, tutor, datetime) VALUES (%s, %s, %s, %s, %s)"
            val = (firstname, lastname, email, tutor, datetime)
            cursor.execute(database,val)
            mysql.connection.commit()
            cursor.close()
            return render_template("trialconfirmation.html", name=firstname, tutor=tutor, datetime=datetime)
    else:
        return render_template("trial.html", form=cform)


###############################################
#                Run app                      #
###############################################

if __name__ == '__main__':
    app.debug = True
    app.run()