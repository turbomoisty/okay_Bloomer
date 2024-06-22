import re

from flask import Blueprint, request, redirect, url_for, flash, session, render_template, current_app
from werkzeug.security import check_password_hash
from .models import bloomerUser, db
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        form_type = request.form.get('form_type')
        if form_type == 'login':
            username = request.form.get('userName')
            password = request.form.get('userPassword')

            if not username or not password:
                flash("Please fill the required fields", 'error')
            else:
                user = bloomerUser.query.filter_by(userName=username).first()
                if user and check_password_hash(user.userPassword, password):
                    login_user(user)
                    flash("Login successful", 'success')

                    return redirect(url_for('views.main_page'))
                else:
                    flash("Invalid username or password", 'error')

        elif form_type == 'signup':
            username = request.form.get('userName')
            password = request.form.get('userPassword')
            email = request.form.get('userEmail')

            if not username or not password or not email:
                flash("Please ensure all fields are filled", 'error')
            else:
                # email_validation = 'r[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}'
                # if re.match(email_validation):

                existing_mail = bloomerUser.query.filter_by(userEmail=email).first()
                existing_name = bloomerUser.query.filter_by(userName=username).first()
                if existing_mail:
                    flash("This email has already been registered!", 'error')
                elif existing_name:
                    flash("This username already exists!", "error")
                else:
                    # I dont know why it says unexpected argument, but removing them breaks the code, so dont.
                    new_user = bloomerUser(userName=username, userEmail=email)
                    new_user.password = password
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Sign up successful! Please log in.', 'success')
                    return redirect(url_for('auth.login_page'))
                #else:

    return render_template('login_page.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are now logged out!.', 'success')
    return redirect(url_for('auth.login_page'))
