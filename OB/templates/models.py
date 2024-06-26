import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myPlantDB.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class bloomerUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(10), db.ForeignKey('user.id'))
    userEmail = db.Column(db.String(20), index=True, unique=True)
    usePassword = db.Column(db.String(10), index=False, unique=True)

    poster = db.relationship('userCommunityPost', backref='originalPoster', lazy=True)
    journal = db.relationship('journalEntry', backref='obUser', lazy=True)
    bloomerPlant = db.relationship('Plant', backref='obPlant', lazy=True)


class journalEntry(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True)
    journal_id = db.Column(db.Integer, db.ForeignKey('journal_entry.id'))
    plant_journal_id = db.Column(db.Integer, db.ForeignKey('plant_journal_entry.id'))
    journalEntry = db.Column(db.String(200), index=False, unique=False)


#The reason we choose the charater limit of 280 for postText is becasue on X they use that value as theirs
class userCommunityPost(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    userPost_id = db.Column(db.Integer, db.ForeignKey('post_creator.id'))
    comPostTitle = db.Column(db.String(15), index=False, unique=False)
    postText = db.Column(db.String(280), index=False, unique=False)

    comments = db.relationship('userComment', backref='userPost', lazy=True)

    #post date still needs to be added in


#We specifically chose 39 characters for the plantType_id is becasue the longest plant name is 39 letters
class Plant(db.Model):
    plant_id = db.Column(db.Integer, primary_key=True)
    userPlant_id = db.Column(db.Integer, db.ForeignKey('plant_user.id'))
    plantName = db.Column(db.String(15), index=False, unique=False)
    plantType = db.Column(db.String(39), index=False, unique=False)

    plantJournalEntry = db.relationship('journalEntry', backref='plantEntry', lazy=True)
    plantSchedule = db.relationship('wateringSchedule', backref='scheduling', lazy=True)


#With regards to waterDate we will be also looking into how implement it as a calendar not add it in manually
class wateringSchedule(db.Model):
    waterSchedule_id = db.Column(db.Integer, primary_key=True)
    userWaterSchedule_id = db.Column(db.Integer, db.ForeignKey('userWaterSchedule.id'))
    plantWaterSchedule_id = db.Column(db.Integer, db.ForeignKey('plantWaterSchedule.id'))
    waterDate = db.Column(db.DateTime, nullable=False, default=datetime.UTC)


class userComment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    commentPost_id = db.Column(db.Integer, db.ForeignKey('commentPost.id'))
    userComment_id = db.Column(db.Integer, db.ForeignKey('userComment.id'))
    commentText = db.Column(db.String(280), index=False, unique=True)


class plantType(db.Model):
    plantType_id = db.Column(db.Integer, primary_key=True)
    plantSpecies = db.Column(db.String(39), index=False, unique=True)
    plantDescription = db.Column(db.String(280), index=False, unique=True)

    characteristics = db.relationship('Plant', backref='plantTypeToPlant', lazy=True)

# ###NOTES#### unique: When set to True, the values in the column has to be unique index: When True, the column is

# journal_entries = db.relationship('Class name - Referring to the 'many' side',backref='attribute name to dynamically allocate',lazy='dynamic')
# 'One' side of the relationship syntax

#    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic')
# searchable by its values primary key: when True, the column acts as the primary key What is a primary key: Each
# value is unique across the whole table, primary key cannot contain a null value and is automatically indexed by the
# database