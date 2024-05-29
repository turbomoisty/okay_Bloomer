from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myPlantDB.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class bloomerUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(10), db.foreignKey('user.id'), index=True, unique=True)
    userEmail = db.Column(db.String(20), index=True, unique=True)
    usePassword = db.Column(db.String(10), index=False, uniqe=True)


class plantPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_text = db.Column(db.String(100), index=False, unique=False)


# ###NOTES#### unique: When set to True, the values in the column has to be unique index: Wen True, the column is

# journal_entries = db.relationship('Class name - Referring to the 'many' side',backref='attribute name to dynamically allocate',lazy='dynamic')
# 'One' side of the relationship syntax

#
# searchable by its values primary key: when True, the column acts as the primary key What is a primary key: Each
# value is unique across the whole table, primary key cannot contain a null value and is automatically indexed by the
# database
class userPlant(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key column will generate unique key?
    plant_name = db.Column(db.String(21), index=True, unique=False)
    plant_species = db.Column(db.String(30), index=True, unique=False)
    user_notes = db.Column(db.String(100), index=False, Unique=False)

