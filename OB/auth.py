from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from .models import bloomerUser, db

auth = Blueprint('auth', __name__)


@auth.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        form_type = request.form.get('form_type')

        if form_type == 'login':
            email = request.form.get('userEmail')
            password = request.form.get('userPassword')

            if not email or password:
                flash("Invalid email or password", 'error')
            else:
                user = bloomerUser.query.filter_by(userEmail=email).first()
                if user and check_password_hash(user.password_hash, password):
                    session['user_id'] = user.id
                    session['user_name'] = user.userName
                if user and user.check_password(password):
                    flash("Login successful")

                    return redirect(url_for('views.main_page'))
                else:
                    flash("Invalid email or password", 'error')

        elif form_type == 'signup':
            username = request.form.get('userName')
            password = request.form.get('userPassword')
            email = request.form.get('userEmail')

            if not username or password or email:
                flash("Please ensure all fields are filled", 'error')
            else:
                existing_user = bloomerUser.query.filter_by(userEmail=email).first()
                if existing_user:
                    flash("This email has already been registered!", 'error')
                else:
                    new_user = bloomerUser(userName=username, userPassword=password)
                    new_user.password = password
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Sign up successful! Please log in.', 'success')
                    return redirect(url_for('login_page'))

    return render_template('login_page.html')


@auth.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login_page'))
