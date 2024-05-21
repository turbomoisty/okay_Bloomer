from flask import Flask, render_template

app = Flask(__name__)


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
