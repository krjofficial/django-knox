import mysql.connector

dataBase = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
)

# superuser username = admin
# superuser password = 123

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE knoxblog")

print("Database created")


