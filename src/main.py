# I am switching this to python as I feel like it will make more sense in the scope of it all
import mysql.connector
cnx = mysql.connector.connect(user="remoteUser", password='root', host='192.168.1.193',  database="librarySystem")
c = cnx.cursor()
print(c.execute("SELECT * FROM users;"))
cnx.close()

# Remove above code when needed
from tkinter import *
import winsound
import threading 
import sys

class Menu(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()

    def makeMenu(self): # This is going to edit the root itself as we want that to always have the menu. I might change this later. The idea right now is that buttons will open toplevel Tk's
        sysLabel = Label(self, text="Library Management System")
        loginButton = Button(self, text="Log in or Create Account", command=Menu.login) #TODO add command
        checkinButton = Button(self, text="Check in") #TODO add command
        checkoutButton = Button(self, text="Check Out") #TODO add command
        checkbookscuroutButton = Button(self, text="Check what books you have out") #TODO add command
        checkaccountButton = Button(self, text="Check Account") #TODO add command
        quitappButton = Button(self, text="Quit App", command=lambda:sys.exit(0)) #TODO add command
        sysLabel.pack()
        loginButton.pack()
        checkinButton.pack()
        checkoutButton.pack()
        checkbookscuroutButton.pack()
        checkaccountButton.pack()
        quitappButton.pack()

    def login():
        top = Toplevel()
        top.title("Account Set up/Sign in")
        #threading.Thread(target= lambda: winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)).start() 
        # ABove is me just testing some code since I haven't touched the above in a while
    

class EventHandler():
    pass
        


if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    app.master.title("Testing")
    app.makeMenu()
    app.mainloop() 