import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


#####GO THROUGH THE MODEL TO DOUBLE CHECK#######
class bloomerUser(db.Model):
    __tableName__ = 'bloomer_user'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(10), index=True, unique=True)
    userEmail = db.Column(db.String(20), index=True, unique=True)
    userPassword = db.Column(db.String(15), index=False, unique=False)

    poster = db.relationship('userCommunityPost', backref='originalPoster', lazy=True)
    journal = db.relationship('journalEntry', backref='obUser', lazy=True)
    plants = db.relationship('Plant', backref='obPlant', lazy=True)

    @property
    def password(self):
        raise AttributeError("error in pw")

    @password.setter
    def password(self, password):
        self.userPassword = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.userPassword, password)


class journalEntry(db.Model):
    __tablename__ = 'journal_entry'
    id = db.Column(db.Integer, primary_key=True)
    journal_title = db.Column(db.String(20),nullable=False)
    journalEntry = db.Column(db.String(200), nullable=False, unique=False)

    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'))
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))


# The reason we choose the character limit of 280 for postText is because on X they use that value as theirs
class userCommunityPost(db.Model):
    __tablename__ = 'user_community_post'
    id = db.Column(db.Integer, primary_key=True)
    PostTitle = db.Column(db.String(15), nullable=False)
    postText = db.Column(db.String(280), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'))
    comments = db.relationship('userComment', backref='userPost', lazy=True)

    # post date still needs to be added in


# We specifically chose 39 characters for the plantType_id is because the longest plant name is 39 letters
class Plant(db.Model):
    __tablename__ = 'plant'
    id = db.Column(db.Integer, primary_key=True)
    plantName = db.Column(db.String(15), nullable=False)
    plantType = db.Column(db.String(39), index=False, unique=False)

    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'))
    plant_id = db.Column(db.Integer, db.ForeignKey('plant_type.id'))
    plantJournalEntry = db.relationship('journalEntry', backref='plantEntry', lazy=True)
    plantSchedule = db.relationship('wateringSchedule', backref='scheduling', lazy=True)


# In regard to waterDate we will be also looking into how implement it as a calendar not add it in manually
class wateringSchedule(db.Model):
    __tablename__ = 'watering_schedule'
    id = db.Column(db.Integer, primary_key=True)
    waterDate = db.Column(db.DateTime, nullable=False, default=datetime.UTC)

    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'))


class userComment(db.Model):
    __tablename__ = 'user_comment'
    id = db.Column(db.Integer, primary_key=True)
    commentText = db.Column(db.String(280), nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey('user_community_post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('bloomer_user.id'))


class plantType(db.Model):
    __tablename__ = 'plant_type'
    id = db.Column(db.Integer, primary_key=True)
    plantSpecies = db.Column(db.String(39), unique=True, nullable=False)
    plantDescription = db.Column(db.String(280), nullable=False)

    plants = db.relationship('Plant', backref='plantTypeToPlant', lazy=True)
