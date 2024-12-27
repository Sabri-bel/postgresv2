
#import some classes from sql alchemy

from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# link python file with chinook / executing instruction from chinook database
# 3 slashes = database locally hosted
db = create_engine("postgresql:///chinook")

# use the metadata class that will contain a collection of our table object and associated data
#(this is a recursive data about data)
meta = MetaData(db)

# construct the data model so python know the schema
# 1. artist table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)
# 2. album table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# 3. track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# make the connection to the database
# this will save our connection to the database in a variable called connection
with db.connect() as connection:
    # select all records from the artist table:
    #select_query = artist_table.select()

    # select only the name column from the artist table:
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # select only queen from the artist table:
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # select only the artist id 51 from the artist table:
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # select only albums from artist id 51 on the album table:
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    #select all tracks where the composer is queen from the track table:
    select_query = track_table.select().where(track_table.c.Composer == "Queen")
    
    results = connection.execute(select_query)
    for result in results:
        print(result)
