from flask import Blueprint, render_template, request, url_for, session, redirect

views = Blueprint('views', __name__)


#@views.route('/')  # Same routing for displaying the main page
@views.route(
    '/main_page')  # app decorator for index route so the browser doesn't shit itself when trying to access files
# Don't forget to add the url string parameter for the route.
def main_page():
    return render_template('main_page.html')


# When routing functions, you need to have .views as prefix
@views.route('/about_us')
def about_us():
    return render_template('about_us.html')

@views.route('/')
@views.route('/rewards')
def rewards():
    return render_template('rewards.html')


@views.route('/user_plant_profile')
def user_plant_profile():
    return render_template('user_plant_profile.html')


@views.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


# @views.route('/')
@views.route('/watering_schedules')
def watering_schedules():
    # if not session.get('logged_in'):
    #     flash("Please log in to access these features")
    #     return redirect(url_for('auth.login_page'))
    return render_template('watering_schedules.html')


# @views.route('/')
@views.route('/plant_journal', methods=['POST', 'GET'])
def plant_journal():
    if session.get == 'logged_in':
        if request.method == 'POST':
            journalTextPath = request.form['journal_text_entry']

    return render_template('plant_journal.html')


@views.route('/under_construction')
def under_construction():
    return render_template('under_construction.html')
