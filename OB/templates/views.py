from flask import Blueprint, render_template

#
views = Blueprint('views', __name__)


@views.route('/')  # app decorator for index route so the browser doesn't shit itself when trying to access files
# Don't forget to add the url string parameter for the route.
def main_page():
    return render_template('main_page.html')


# ##########REMEMBER TO LINK THIS IN THE HTML FILE AT LINE 17: main_page.html########
#
@views.route('/about_us')
def about_us():
    return render_template('about_us.html')


@views.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


@views.route('/watering_schedules')
def watering_schedules():
    return render_template('watering_schedules.html')


@views.route('/plant_journal')
def plant_journal():
    return render_template('plant_journal.html')

# just templates('/')


# db = SQLAlchemy(app)
# class plantJournal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(250), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.now())
#
#     def __repr__(self):
#         return '<Journal %r>' % self.id

# def check_login(f):
#     @wraps(f)
#     def dec_functions(*args, **kwargs):
#         if 'user_id' not in session:
#             flash("Sorry, you must be logged in to use this functionality", "danger")
#             return redirect(url_for('login_page'))
#         return f(*args, **kwargs)
#
#     return dec_functions
