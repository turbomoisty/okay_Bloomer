import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


#####GO THROUGH THE MODEL TO DOUBLE CHECK#######
class bloomerUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(10), index=True, unique=True)
    userEmail = db.Column(db.String(20), index=True, unique=True)
    userPassword = db.Column(db.String(10), index=False, unique=True)

    poster = db.relationship('userCommunityPost', backref='originalPoster', lazy=True)
    journal = db.relationship('journalEntry', backref='obUser', lazy=True)
    bloomerPlant = db.relationship('Plant', backref='obPlant', lazy=True)

    @property
    def password(self):
        raise AttributeError("error in pw")

    @password.setter
    def password(self, password):
        self.userPassword = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.userPassword, password)


class journalEntry(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True)
    journalEntry = db.Column(db.String(200), index=False, unique=False)

    journal_id = db.Column(db.Integer, db.ForeignKey('journal_entry.id'))
    plant_journal_id = db.Column(db.Integer, db.ForeignKey('plant_journal_entry.id'))


# The reason we choose the character limit of 280 for postText is because on X they use that value as theirs
class userCommunityPost(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    userPost_id = db.Column(db.Integer, db.ForeignKey('post_creator.id'))
    comPostTitle = db.Column(db.String(15), index=False, unique=False)
    postText = db.Column(db.String(280), index=False, unique=False)

    comments = db.relationship('userComment', backref='userPost', lazy=True)

    # post date still needs to be added in


# We specifically chose 39 characters for the plantType_id is because the longest plant name is 39 letters
class Plant(db.Model):
    plant_id = db.Column(db.Integer, primary_key=True)
    userPlant_id = db.Column(db.Integer, db.ForeignKey('plant_user.id'))
    plantName = db.Column(db.String(15), index=False, unique=False)
    plantType = db.Column(db.String(39), index=False, unique=False)

    plantJournalEntry = db.relationship('journalEntry', backref='plantEntry', lazy=True)
    plantSchedule = db.relationship('wateringSchedule', backref='scheduling', lazy=True)


# In regard to waterDate we will be also looking into how implement it as a calendar not add it in manually
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
