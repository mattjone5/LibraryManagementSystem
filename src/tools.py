import mysql.connector
import sys
class DBConnection():
    def __init__(self):
        cnx = None
        try:
            DBConnection.cnx = mysql.connector.connect(user="remoteUser", password='root', host='192.168.1.193',  database="librarySystem")
            print ("Connection successful!")
        except:
            print("Error, connection failed!")
            sys.exit(0)
            
    def getLogInData(self, username, password):
        data = []
        cursor = DBConnection.cnx.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s;", (username.get(), password))
        for dataPoint in cursor:
            data.append(dataPoint)
        if len(data) == 0:
            return None
        return data

