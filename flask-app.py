#          Import some packages               #
###############################################

from flask import Flask, render_template, request, redirect, url_for
from app.forms import signupForm


###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'dev fao football app'


###############################################
#       Render Contact page                   #
###############################################
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/signup', methods=["GET", "POST"])
def home():
    cform = signupForm()
    if cform.validate_on_submit():
        print(f"Name:{cform.name.data}, E-mail:{cform.email.data}, message: {cform.message.data}")
    return render_template("signup.html", form=cform)


###############################################
#                Run app                      #
###############################################

if __name__ == '__main__':
    app.run(debug=True)