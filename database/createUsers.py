import sqlite3

myConnection = sqlite3.connect('./users.sqlite')

myCursor = myConnection.cursor()
myCursor.execute("""CREATE TABLE users (
            username text,
            password text
            )""")

myConnection.commit()
myConnection.close()