# never call this file psycopg2.py since it is the name of the default file used
#by the package and it will end with a failure

# 1. import the package to the python file
import psycopg2


#2. connect with chinook database using the connect() method
# assign to a variable called connection
# assigned only the name of the variable for now but other can be assigned (password, username, host etc)
connection = psycopg2.connect(database="chinook")


#3. build a cursor object of the database --> similar to a list or array
# anything we will query will become part of this cursor object
cursor = connection.cursor()


# 4. fetch the results (multiple):
results = cursor.fetchall()
# results = cursor.fetchone() ==> in case of single result


# 5. close the connection with the database
connection.close()


#6. print results 
for result in results:
    print(result)