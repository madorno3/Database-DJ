from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):


    db.app = app
    db.init_app(app)

class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    username = db.Column(
        db.String(20),
        nullable=False,
        unique=True,
    )
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    playlists = relationship('Playlists', back_populates='user')
    # songs = relationship('Songs', back_populates='user')


    @classmethod
    def register(cls,username, password, first_name, last_name, email):
        """Register a user, hashing their password."""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False


class Playlists(db.Model):
    __tablename__ = "playlists"
    playlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=False, nullable=False)  # Corrected usage
    description = db.Column(db.Text, unique=False, nullable=True)  # Corrected usage
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  
    user = relationship('User', back_populates='playlists')
    
    

class Playlists_songs(db.Model):
    __tablename__="playlists_songs"
    pl_songs_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'), nullable=False)
    playlist = relationship('Playlists', backref=db.backref('playlist_songs', lazy='dynamic'))
    song = relationship('Songs', backref=db.backref('playlist_songs', lazy='dynamic'))

class Songs(db.Model):
    __tablename__="songs"
    song_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)
    title = db.Column(db.String,
                     unique=False,
                     nullable=False)
    artist = db.Column(db.String,
                     unique=False,
                     nullable=False)


