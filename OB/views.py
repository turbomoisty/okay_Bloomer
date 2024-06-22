from flask import Blueprint, render_template, request, url_for, session, redirect
from flask_login import login_user, login_required, current_user
from .models import Plant, userComment, plantType
from . import db

views = Blueprint('views', __name__)


@views.route('/')  # Same routing for displaying the main page
@views.route('/main_page')
# app decorator for index route so the browser doesn't shit itself when trying to access files
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
    plants = Plant.query.filter_by(user_id=current_user.id).all()
    comments = userComment.query.filter_by(user_id=current_user.id).all()
    plant_types = plantType.query.all()
    return render_template('watering_schedules.html', plants=plants, comments=comments, plant_types=plant_types,
                           username=current_user.userName)


# forms: add-plant, add-schedule, comment-form, image-upload(I still don't know how to add images)

@views.route('/add-plant', methods=['POST'])
@login_required
def add_plant():
    plant_name = request.form.get('plant_name')
    plant_type = request.form.get('plant_type')
    if plant_name and plant_type:
        new_plant = Plant(plantName=plant_name, waterDate=2, plant_id=plant_type, user_id=current_user.id)
        db.session.add(new_plant)
        db.session.commit()
    return redirect(url_for('views.watering_schedules'))


##double check to see if all objects are named consistently.
@views.route('/add-schedule', methods=['POST'])
@login_required
def add_schedule():
    plant_name = request.form.get('plant_name')
    schedule = int(request.form.get('add_schedule'))
    plant = Plant.query.filter_by(plantName=plant_name, user_id=current_user.id).first()
    if plant:
        plant.waterDate = schedule
        db.session.commit()
        return redirect(url_for('views.watering_schedules'))


@views.route('/comment-form', methods=['POST'])
@login_required
def add_comments():
    comment_text = request.form.get('comment')
    if comment_text:
        adding_comment = userComment(commentText=comment_text, user_id=current_user.id)
        db.session.add(adding_comment)
        db.session.commit()
    return redirect(url_for('views.watering_schedules'))


@views.route('/under_construction')
def under_construction():
    return render_template('under_construction.html')
