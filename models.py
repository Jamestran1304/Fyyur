from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'venue'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.Text)
    artists = db.relationship("Artist", secondary="show", lazy="joined", cascade='all, delete')
        # ? CASCADE ALL, DELETE to delete the children (Shows) automatically before deleting the parent
    # DONE: implement any missing fields, as a database migration using Flask-Migrate ✅


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    genres = db.Column(db.ARRAY(db.String))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.Text)
    venue = db.relationship("Venue", secondary="show", lazy="joined", cascade='all, delete')
    
    # DONE: implement any missing fields, as a database migration using Flask-Migrate ✅


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    start_time = db.Column(db.DateTime)
    venue = db.relationship(Venue, backref=db.backref("shows", lazy=True))
    artist = db.relationship(Artist, backref=db.backref("shows", lazy=True))

#src: 
# https://michaelcho.me/article/many-to-many-relationships-in-sqlalchemy-models-flask/ 
# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#many-to-many