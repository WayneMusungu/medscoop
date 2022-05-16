from . import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    """
    User class that will help in creating users
    """
    __tablename__ = 'users'



class PhotoProfile(db.Model):
    __tablename__ = 'profile_photos'

