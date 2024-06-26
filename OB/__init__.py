from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manger = LoginManager()


def create_site():
    # Create unique token per user instance.

    app = Flask(__name__)
    app.secret_key = 'test_key'  # secrets.token_hex(16)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myPlantDB.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manger.login_view = 'auth.login_page'
    login_manger.init_app(app)

    @login_manger.user_loader
    def start_user(user_id):
        return bloomerUser.query.get(int(user_id))

    with app.app_context():
        from .models import bloomerUser
        db.create_all()

    from .views import views as views_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(views_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/')

    return app
