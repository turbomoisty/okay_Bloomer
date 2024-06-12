from flask import Flask
import secrets

from .models import db, bloomerUser, userCommunityPost, journalEntry, plantType, userComment, Plant
from flask_login import LoginManager


def create_site():
    # Create unique token per user instance.


    app = Flask(__name__)
    app.secret_key = 'test_key' #secrets.token_hex(16)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myPlantDB.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_mange = LoginManager()
    login_mange.login_view = 'auth.login_page'
    login_mange.init_app(app)

    from .views import views
    from .auth import auth

    @login_mange.user_loader
    def start_user(user_id):
        return bloomerUser.query.get(int(user_id))

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app
