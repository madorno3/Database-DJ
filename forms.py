"""Forms for playlist app."""

from wtforms import SelectField, StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    """Form for adding playlists."""
    username = StringField("username", validators=[InputRequired()])
    password = StringField("password", validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    first_name = StringField("firstname", validators=[InputRequired()])
    last_name = StringField("lastname", validators=[InputRequired()])
    email = StringField("email", validators=[InputRequired()])

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("name", validators=[InputRequired()])
    description = StringField("description", validators=[InputRequired()])

    # Add the necessary code to use this form

class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("title", validators=[InputRequired()])
    artist = StringField("artist", validators=[InputRequired()])
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add')
    
