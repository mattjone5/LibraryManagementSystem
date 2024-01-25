import mysql.connector
class DBConnection():
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user="remoteUser", password='root', host='192.168.1.193',  database="librarySystem")
            print ("Connection successful!")
        except:
            print("Error, connection failed!")

    def testStuff(self):
        cursor = self.cnx.cursor()
        print(cursor.execute("SELECT * FROM users;"))