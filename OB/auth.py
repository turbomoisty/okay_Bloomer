from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash

from .models import bloomerUser, db

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
                    session['logged_in'] = True
                    session['user_id'] = user.id
                    session['bloomerUser'] = user.userName
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
                existing_mail = bloomerUser.query.filter_by(userEmail=email).first()
                existing_name = bloomerUser.query.filter_by(userName=username).first()
                if existing_mail:
                    flash("This email has already been registered!", 'error')
                elif existing_name:
                    flash("This username already exists!", "error")
                else:
                    new_user = bloomerUser(userName=username, userEmail=email)
                    new_user.password = password
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Sign up successful! Please log in.', 'success')
                    return redirect(url_for('auth.login_page'))

    return render_template('login_page.html')


@auth.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out!.', 'success')
    return redirect(url_for('auth.login_page'))
