#working with the class based models -orm that comes with sqlalchemy
#class is a collection of methods each methods do only one things
# example of methods .connect() .select() .execute() 

#import items except of Table and MetaData (no longer creating tables but classes)
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

# classes created will be a subclass of declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# create the variable db that point out to the database location using create_engine
db = create_engine("postgresql:///chinook")

# the following will grab the metadata produced by the database table schema
# and create a subclass to map everything back within the base variable
base = declarative_base()

#create the database subclass after base declaration but before session creation
# create a class based model for Album table
class Artist(base):
    __tablename__= "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# Create a class based module for Album table
class Album(base):
    __tablename__= "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class based module for track table
class Track(base):
    __tablename__= "Track"
    TrackId = Column(Integer, primary_key=True),
    Name = Column(String),
    AlbumId = Column(Integer, ForeignKey("album_table.AlbumId")),
    MediaTypeId = Column(Integer, primary_key=False),
    GenreId = Column(Integer, primary_key=False),
    Composer = Column(String),
    Millisecond = Column(Integer),
    Bytes = Column(Integer),
    UnitPrice = Column(Float)


# instead of connect to the database directly, we will ask for a session
# create a new instance of sessionmaker that point to the db (engine)
Session = sessionmaker(db)

#open an actual session by calling the Session() subclass defined above
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )