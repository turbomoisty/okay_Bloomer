from flask import Blueprint, render_template, request, redirect, session, flash, url_for

views = Blueprint('views', __name__)


@views.route('/')  # Same routing for displaying the main page
@views.route(
    '/main_page')  # app decorator for index route so the browser doesn't shit itself when trying to access files
# Don't forget to add the url string parameter for the route.
def main_page():
    return render_template('main_page.html')


@views.route('/about_us')
def about_us():
    return render_template('about_us.html')


@views.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


@views.route('/watering_schedules')
def watering_schedules():
    if not session.get('logged_in'):
        flash("Please log in to access these features")
        return redirect(url_for('auth.login_page'))
    return render_template('watering_schedules.html')


@views.route('/plant_journal')
def plant_journal():
    return render_template('plant_journal.html')


@views.route('/under_construction')
def under_construction():
    return render_template('under_construction.html')
