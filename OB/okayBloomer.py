from flask import Flask, render_template, jsonify

# import

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/login_page')
def login_page():
    # with open("userCredentials.txt", "r") as userFile:
    #
    # def singleton(cls):
    #     instance = None
    #
    #     def get_instance():
    #         nonlocal instance
    #
    #         if instance is None:
    #             instance = cls()
    #
    #             return get_instance
    #
    #         return get_instance
    #
    # @singleton
    # def user_creds():
    #     class login_cred:
    #         def __init__(self):
    #             self.userName = "@userName"
    #             self.email = "@email"
    #             self.password = "@password"

    ##########REMEMBER TO LINK THIS IN THE HTML FILE AT LINE 17: main_page.html########
    return render_template('login_page.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/plant_profiles')
def plant_profiles():
    return render_template('plant_profiles.html')


# just templates


if __name__ == "__main__":
    app.run(debug=True)
