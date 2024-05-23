from flask import Flask
import secrets


def create_site():
    token_key = secrets.token_hex(16)
    app = Flask(__name__)
    app.secret_key = token_key

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/views')
    app.register_blueprint(auth,url_prefix='/auth')
    return app
