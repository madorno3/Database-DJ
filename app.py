from flask import Flask, render_template, redirect, session, flash, request
from models import connect_db, db, Playlists, Songs, Playlists_songs, User
from forms import RegisterForm, LoginForm, PlaylistForm, SongForm, NewSongForPlaylistForm
from flask_bcrypt import Bcrypt
from wtforms import Form, SelectField



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///playlist_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"


app.app_context().push()
connect_db(app)

db.create_all()

@app.route("/", methods=["GET", "POST"] )
def home():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:
            session['id'] = user.id
            return redirect(f"/{user.id}")

    else:
        return render_template('home.html', form=form)
    
@app.route("/register", methods=["GET", "POST"])
def register():
    
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        user = User.register(username,password,first_name,last_name,email)
        session["id"] = user.id
        db.session.add(user)
        db.session.commit()
        return redirect(f"/{user.id}")

    return render_template("register_form.html", form=form)

@app.route("/<int:id>")
def profile(id):
    
    user = User.query.get_or_404(id)
    return render_template("profile.html", user=user)

@app.route("/playlists/new_plform", methods=["GET", "POST"])
def new_playlist_form():
   
    form = PlaylistForm()
    if form.validate_on_submit():
        
        name = form.name.data
        description = form.description.data
        playlist = Playlists(name=name, description=description, user_id=session['id'])
        db.session.add(playlist)
        db.session.commit()
        return redirect("/playlists")
    return render_template("create_new_playlist.html", form=form)

@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""
    # user_id = session.get('user_id')
    # user = User.query.get_or_404(id)
    # session["id"] = user.id
    playlists = Playlists.query.filter_by(user_id=session['id']).all()
    # playlists = Playlists.query.all()
    return render_template("playlists.html", playlists=playlists)

@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    playlist = Playlists.query.get(playlist_id)
    songs = Songs.query.join(Playlists_songs).filter(Playlists_songs.playlist_id == playlist_id).all()

    return render_template("playlist.html", playlist=playlist, songs=songs)

    
@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_playlist(playlist_id):
    
    playlist = Playlists.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()
    all_songs = Songs.query.all()
    form.song.choices = [(song.song_id, song.title) for song in all_songs]
                     
    if form.validate_on_submit():
    
        playlist_song = Playlists_songs(song_id=form.song.data,playlist_id=playlist_id)
        db.session.add(playlist_song)
        db.session.commit()
        
        return redirect(f"/playlists/{playlist_id}")
    return render_template('add_song_to_playlist.html', playlist=playlist, form=form)



# ##############################################################################
# # Song routes


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    form = SongForm()
    if form.validate_on_submit():
        
        title = form.title.data
        artist = form.artist.data
        song = Songs(title=title, artist=artist)
        db.session.add(song)
        db.session.commit()
        return redirect("/songs")
    else:
        return render_template("new_song.html", form=form)


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""
    
    songs = Songs.query.all()
    return render_template("songs.html", songs=songs)

@app.route("/songs/<int:song_id>")
def show_song(song_id):
    song = Songs.query.get(song_id)
    
    return render_template("song.html",song=song)

