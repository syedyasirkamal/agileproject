from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField,  SelectField
from wtforms.validators import DataRequired
from app.classes import Email, Date_Time, Name_Validation
from wtforms.fields import DateTimeField

class signupForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Name_Validation.validate_name])
    email = StringField(label='Email', validators=[
        DataRequired(), Email(granular_message=True)])
    submit = SubmitField(label="Join our mailing list")
class trialForm(FlaskForm):
    myChoices = ('','Uriel', 'Flor', 'Gabriel')
    tutor = SelectField('Tutor', choices=myChoices, validators=[DataRequired()])
    firstname = StringField(label='First Name', validators=[DataRequired(), Name_Validation.validate_name])
    lastname = StringField(label='Last Name', validators=[DataRequired(), Name_Validation.validate_name])
    email = StringField(label='Email', validators=[
        DataRequired(), Email(granular_message=True)])
    datetime = DateTimeField(id="datepick", validators=[DataRequired(), Date_Time.validate_date])
    submit = SubmitField(label="Sign up for Trial Lesson")
