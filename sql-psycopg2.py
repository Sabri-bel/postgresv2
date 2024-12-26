# never call this file psycopg2.py since it is the name of the default file used
#by the package and it will end with a failure

import psycopg2

#connect with chinook database (more variable can be defined other than database)
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database (this is something similar to an array)
cursor = connection.cursor()

#QUERY 1 - select all the records from the "artist" table:
#cursor.execute('SELECT * FROM "Artist"')

#QUERY 2 - select only the name column from the Artist table:
#cursor.execute('SELECT "Name" FROM "Artist"')

# QUERY 3 - select only queen from the artist table:
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
#the query above is SELECT * FROM "Artist" WHERE "Name" = 'Queen' but there is a problem with
#the single quote, so they cannot be used in psycopg2

# QUERY 4 - select only the artistId #51 from the Artist table:
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# QUERY 5 - select only the album with "ArtistId" 51 from the Album table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#QUERY 6- select all tracks where the composer is queen from the rtack table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# fetch the results (multiple)
results = cursor.fetchall()
#results = cursor.fetchone() # ==> if single result will be returned

# close the connection 
connection.close()

#print the results 
for result in results:
    print(result)
