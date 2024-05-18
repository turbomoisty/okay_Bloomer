from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


if __name__ == "__main__":
    app.run(debug=True)
