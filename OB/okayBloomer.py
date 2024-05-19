from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/login_page')
def login_page():
    return render_template('login_page.html')


##########REMEMBER TO LINK THIS IN THE HTML FILE AT LINE 17: main_page.html########

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


# just templates


if __name__ == "__main__":
    app.run(debug=True)
