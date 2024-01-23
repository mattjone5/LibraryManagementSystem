# I am switching this to python as I feel like it will make more sense in the scope of it all
import mysql.connector
cnx = mysql.connector.connect(user="root", password='root', host='127.0.0.1', database="librarysystem")
c = cnx.cursor()
print(c.execute("SELECT * FROM users;"))
cnx.close()