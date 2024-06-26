from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db
from datetime import datetime


#####GO THROUGH THE MODEL TO DOUBLE CHECK#######
class bloomerUser(db.Model, UserMixin):
    __tablename__ = 'bloomer_user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(10), index=True, unique=True)
    userEmail = db.Column(db.String(20), index=True, unique=True)
    userPassword = db.Column(db.String(15), index=False, unique=False)

    poster = db.relationship('userPost', backref='originalPoster', lazy=True)
    journal = db.relationship('journalEntry', backref='obUser', lazy=True)
    plants = db.relationship('Plant', backref='obPlant', lazy=True)
    comments = db.relationship('userComment', backref='obComments', lazy=True)

    @property
    def password(self):
        raise AttributeError("error in pw")

    @password.setter
    def password(self, password):
        self.userPassword = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.userPassword, password)

    def __init__(self, userName, userEmail):
        self.userName = userName
        self.userEmail = userEmail


class journalEntry(db.Model):
    __tablename__ = 'journal_entry'
    id = db.Column(db.Integer, primary_key=True)
    journal_title = db.Column(db.String(20), nullable=False)
    journalEntry = db.Column(db.String(200), nullable=False, unique=False)

    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'))
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))


# The reason we choose the character limit of 280 for postText is because on X they use that value as theirs


# post date still needs to be added in


# We specifically chose 39 characters for the plantType_id is because the longest plant name is 39 letters
class Plant(db.Model):
    __tablename__ = 'plant'
    id = db.Column(db.Integer, primary_key=True)
    plantName = db.Column(db.String(15), nullable=False)
    waterDate = db.Column(db.Integer, nullable=False)
    last_watered = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'), nullable=False)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant_type.id'), nullable=False)
    plantJournalEntry = db.relationship('journalEntry', backref='plantEntry', lazy=True)



# In regard to waterDate we will be also looking into how implement it as a calendar not add it in manually
class userPost(db.Model):
    __tablename__ = 'user_community_post'
    id = db.Column(db.Integer, primary_key=True)
    PostTitle = db.Column(db.String(15), nullable=False)
    PostText = db.Column(db.String(280), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'))
    comments = db.relationship('userComment', backref='userPost', lazy=True)


class userComment(db.Model):
    __tablename__ = 'user_comment'
    id = db.Column(db.Integer, primary_key=True)
    commentText = db.Column(db.String(280), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    post_id = db.Column(db.Integer, db.ForeignKey('user_community_post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'))


class plantType(db.Model):
    __tablename__ = 'plant_type'
    id = db.Column(db.Integer, primary_key=True)
    typeName = db.Column(db.String(39), nullable=False)

    plants = db.relationship('Plant', backref='plantTypeToPlant', lazy=True)
