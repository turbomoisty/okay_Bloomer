from flask import Flask
import secrets


def create_site():
    token_key = secrets.token_hex(16)
    app = Flask(__name__)
    app.secret_key = token_key
    return app
