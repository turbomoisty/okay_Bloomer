from flask import Flask, render_template, url_for, session, flash, redirect
from functools import wraps
import secrets

token_key = secrets.token_hex(16)

# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # three slashes for relative pathing
app.secret_key = token_key


# db = SQLAlchemy(app)
#
#
# class plantJournal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(250), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.now())
#
#     def __repr__(self):
#         return '<Journal %r>' % self.id

def check_login(f):
    @wraps(f)
    def dec_functions(*args, **kwargs):
        if 'user_id' not in session:
            flash("Sorry, you must be logged in to use this functionality", "danger")
            return redirect(url_for('login_page'))
        return f(*args,**kwargs)
    return dec_functions


@app.route('/main_page')  # app decorator for index route so the browser doesn't shit itself when trying to access files
# Don't forget to add the url string parameter for the route.
def main_page():
    return render_template('main_page.html')


#
#
@app.route('/login_page')
def login_page():
    return render_template('login_page.html')


#
#
# ##########REMEMBER TO LINK THIS IN THE HTML FILE AT LINE 17: main_page.html########
#
@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


# @app.route('/')
# def watering_schedules():
#     return render_template('watering_schedules.html')

@app.route('/')
def plant_journal():
    return render_template('plant_journal.html')


# just templates


if __name__ == "__main__":
    app.run(debug=True)
