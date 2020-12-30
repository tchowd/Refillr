from flask import Flask
from flask import Flask, render_template, redirect, url_for, request, Request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, RadioField, DateField
from wtforms.validators import InputRequired, Email
from flask_wtf import CsrfProtect
import csv

app = Flask(__name__)

app.config['SECRET_KEY'] = 'btrsjbvbsay'
csrf = CsrfProtect()
csrf.init_app(app)


class DataStore:
    full_name_1 = None
    address_1 = None
    date_of_res_1 = None
    age_1 = None
    date_of_birth_1 = None
    place_of_birth_1 = None
    sex_1 = None
    status_1 = None
    parent_1_1 = None
    parent_2_1 = None

    full_name_2 = None
    address_2 = None
    date_of_res_2 = None
    age_2 = None
    date_of_birth_2 = None
    place_of_birth_2 = None
    sex_2 = None
    status_2 = None
    parent_1_2 = None
    parent_2_2 = None

    marriage_date = None
    marriage_location = None
    attorney = None


data = DataStore()


class TestForm(FlaskForm):
    full_name_1 = StringField('Full Name', validators=[InputRequired()])
    address_1 = StringField('Address', validators=[InputRequired()])
    date_of_res_1 = StringField('Living here since (DD/MM/YYYY)', validators=[InputRequired()])
    age_1 = StringField('Age', validators=[InputRequired()])
    date_of_birth_1 = StringField('Date of Birth (DD/MM/YYYY)', validators=[InputRequired()])
    place_of_birth_1 = StringField('Place of Birth (City, Country)', validators=[InputRequired()])
    sex_1 = RadioField('Sex', validators=[InputRequired()], choices=[('s1', 'M'), ('s2', 'F')])
    status_1 = RadioField('Marital Status Before Marriage', validators=[InputRequired()], choices=[('st1', 'Single'),
                                                                    ('st2', 'Divorced'), ('st3', 'Widowed/Widower')])
    parent_1_1 = StringField('Mother\'s Full Name', validators=[InputRequired()])
    parent_2_1 = StringField('Father\'s Full Name', validators=[InputRequired()])

    full_name_2 = StringField('Full Name', validators=[InputRequired()])
    address_2 = StringField('Address', validators=[InputRequired()])
    date_of_res_2 = StringField('Living here since (DD/MM/YYYY)', validators=[InputRequired()])
    date_of_birth_2 = StringField('Date of Birth (DD/MM/YYYY)', validators=[InputRequired()])
    age_2 = StringField('Age', validators=[InputRequired()])
    place_of_birth_2 = StringField('Place of Birth (City, Country)', validators=[InputRequired()])
    sex_2 = RadioField('Sex', validators=[InputRequired()], choices=[('s1', 'M'), ('s2', 'F')])
    status_2 = RadioField('Marital Status Before Marriage', validators=[InputRequired()], choices=[('st1', 'Single'),
                                                                    ('st2', 'Divorced'), ('st3','Widowed/Widower')])
    parent_1_2 = StringField('Mother\'s Full Name', validators=[InputRequired()])
    parent_2_2 = StringField('Father\'s Full Name', validators=[InputRequired()])

    marriage_date = StringField('Marriage Date (DD/MM/YYYY)', validators=[InputRequired()])
    marriage_location = StringField('Marriage Location (Country)', validators=[InputRequired()])
    attorney = StringField('Attorney\'s Full Name', validators=[InputRequired()])
    submit = SubmitField('Send!')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")


@app.route('/services')
def services():
    return render_template('services.html', title="Services")


@app.route('/divorce', methods=["POST", "GET"])
def divorce():
    form = TestForm()
    if form.validate_on_submit():
        data.full_name_1 = form.full_name_1.data
        data.address_1 = form.address_1.data
        data.date_of_res_1 = form.date_of_res_1.data
        data.date_of_birth_1 = form.date_of_birth_1.data
        data.age_1 = form.age_1.data
        data.place_of_birth_1 = form.place_of_birth_1.data
        data.sex_1 = form.sex_1.data
        data.status_1 = form.status_1.data
        data.parent_1_1 = form.parent_1_1.data
        data.parent_2_1 = form.parent_2_1.data

        data.full_name_2 = form.full_name_2.data
        data.address_2 = form.address_2.data
        data.date_of_res_2 = form.date_of_res_2.data
        data.date_of_birth_2 = form.date_of_birth_2.data
        data.age_2 = form.age_2.data
        data.place_of_birth_2 = form.place_of_birth_2.data
        data.sex_2 = form.sex_2.data
        data.status_2 = form.status_2.data
        data.parent_1_2 = form.parent_1_2.data
        data.parent_2_2 = form.parent_2_2.data

        data.marriage_date = form.marriage_date.data
        data.marriage_location = form.marriage_location.data
        data.attorney = form.attorney.data
        return redirect(url_for('end'))
    return render_template('divorce.html', form=form, title="Divorce")


@app.route('/endpage')
def end():
    full_name_1 = data.full_name_1
    address_1 = data.address_1
    date_of_res_1 = data.date_of_res_1
    date_of_birth_1 = data.date_of_birth_1
    age_1 = data.age_1
    place_of_birth_1 = data.place_of_birth_1
    sex_1 = data.sex_1
    status_1 = data.status_1
    parent_1_1 = data.parent_1_1
    parent_2_1 = data.parent_2_1

    full_name_2 = data.full_name_2
    address_2 = data.address_2
    date_of_res_2 = data.date_of_res_2
    date_of_birth_2 = data.date_of_birth_2
    age_2 = data.age_2
    place_of_birth_2 = data.place_of_birth_2
    sex_2 = data.sex_2
    status_2 = data.status_2
    parent_1_2 = data.parent_1_2
    parent_2_2 = data.parent_2_2

    marriage_date = data.marriage_date
    marriage_location = data.marriage_location
    attorney = data.attorney
    return render_template('endpage.html', title="Submission Page", full_name_1=full_name_1, address_1=address_1,
                           date_of_res_1=date_of_res_1, age_1=age_1, date_of_birth_1=date_of_birth_1, place_of_birth_1=place_of_birth_1, sex_1=sex_1,
                           status_1=status_1, parent_1_1=parent_1_1, parent_2_1=parent_2_1, full_name_2=full_name_2,
                           address_2=address_2, date_of_res_2=date_of_res_2, age_2=age_2, date_of_birth_2=date_of_birth_2,
                           place_of_birth_2=place_of_birth_2, sex_2=sex_2, status_2=status_2, parent_1_2=parent_1_2,
                           parent_2_2=parent_2_2, marriage_date=marriage_date, marriage_location=marriage_location,
                           attorney=attorney)


if __name__ == '__main__':
    app.run(debug=True)
