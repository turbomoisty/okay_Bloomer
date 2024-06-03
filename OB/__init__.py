from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy
from .models import db, bloomerUser, userCommunityPost, journalEntry, plantType, userComment, wateringSchedule, Plant


def create_site():
    # Create unique token per user instance.
    token_key = secrets.token_hex(16)

    app = Flask(__name__)
    app.secret_key = token_key

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myPlantDB.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()
    return app
