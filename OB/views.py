from flask import Blueprint, render_template, request, url_for, session, redirect
from flask_login import login_user, login_required, logout_user, current_user
from .models import bloomerUser, journalEntry, Plant, userComment, db

views = Blueprint('views', __name__)


@views.route('/')  # Same routing for displaying the main page
@views.route(
    '/main_page')  # app decorator for index route so the browser doesn't shit itself when trying to access files
# Don't forget to add the url string parameter for the route.
def main_page():
    return render_template('main_page.html')


# When routing functions, you need to have .views as prefix
@views.route('/about_us')
def about_us():
    return render_template('about_us.html')


@views.route('/rewards')
def rewards():
    return render_template('rewards.html')


@views.route('/user_plant_profile')
def user_plant_profile():
    return render_template('user_plant_profile.html')


@views.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


@views.route('/watering_schedules')
@login_required
def watering_schedules():
    plant = Plant.query.filter_by(user_id=current_user.id).all()
    comment = userComment.query.filter_by(user_id=current_user.id).all()
    return render_template('watering_schedules.html', plant=plant, comment=comment, username=current_user.userName)


# forms: add-plant, add-schedule, comment-form, image-upload(I still don't know how to add images)

@views.route('/add-plant', methods=['POST'])
@login_required
def add_plant():
    plant_name = request.form.get('plant_name')
    new_plant = Plant(name=plant_name, scheduling_interval=2, user_id=current_user.id)
    db.session.add(new_plant)
    db.session.commit()
    return redirect(url_for('views.watering_schedules'))


@views.route('/add-schedule', methods=['POST'])
@login_required
def add_schedule():
    plant_name = request.form.get('plant_name')
    schedule = int(request.form.get('add_schedule'))
    plant = Plant.query.filter_by(name=plant_name, user_id=current_user.id).first()
    if plant:
        plant.add_schedule = schedule
        db.session.commit()
        return redirect(url_for('views.watering_schedules'))


@views.route('comment-form', methods=['POST'])
@login_required
def add_comments():
    comment = request.form.get('comment')
    adding_comment = userComment(comment=comment, user_id=current_user.id)
    db.session.add(adding_comment)
    db.session.commit()
    return redirect(url_for('views.watering_schedules'))


# @views.route('/plant_journal', methods=['POST', 'GET'])
# def plant_journal():
#     if session.get == 'logged_in':
#         if request.method == 'POST':
#             journalTextPath = request.form['journal_text_entry']
#
#     return render_template('plant_journal.html')


@views.route('/under_construction')
def under_construction():
    return render_template('under_construction.html')
