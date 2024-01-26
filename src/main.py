# I am switching this to python as I feel like it will make more sense in the scope of it all

from tkinter import *
from tkinter import messagebox
import winsound
import threading 
import sys
import tools
import hashlib

class Menu(Frame):

    db = None
    username = None

    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack()
        Menu.db = tools.DBConnection()

    def makeMenu(self): # This is going to edit the root itself as we want that to always have the menu. I might change this later. The idea right now is that buttons will open toplevel Tk's
        sysLabel = Label(self, text="Library Management System")
        loginButton = Button(self, text="Log in or Create Account", command=Menu.login) #TODO add command
        checkinButton = Button(self, text="Check in") #TODO add command
        checkoutButton = Button(self, text="Check Out") #TODO add command
        checkbookscuroutButton = Button(self, text="Check what books you have out") #TODO add command
        checkaccountButton = Button(self, text="Check Account") #TODO add command
        quitappButton = Button(self, text="Quit App", command=lambda: (Menu.db.cnx.close(), sys.exit(0))) #TODO add command
        sysLabel.pack()
        loginButton.pack()
        checkinButton.pack()
        checkoutButton.pack()
        checkbookscuroutButton.pack()
        checkaccountButton.pack()
        quitappButton.pack()

    def checkSignin(username, password, window):
        passwordHash = hashlib.sha256(password.get().encode('utf-8')).hexdigest()
        data = Menu.db.getLogInData(username, passwordHash)
        if data != None:
            Menu.username = data[0][1]
            window.destroy()
        else:
            threading.Thread(target= lambda: winsound.PlaySound("SystemHand", winsound.SND_ALIAS)).start()
            messagebox.showerror("Unable to Log in","Error:\nUsername or Passwor is incorrect. Please try again!")

    def login():
        top = Toplevel()
        top.title("Account Set up/Sign in")
        username = StringVar()
        password = StringVar()
        usernameLabel = Label(top,text="Username: ")
        usernameEntry = Entry(top, textvariable=username)
        passwordLabel = Label(top, text="Password")
        passwordEntry = Entry(top, textvariable=password, show="*")
        signinButton = Button(top, text="Sign in", command=lambda: Menu.checkSignin(username, password, top))
        signupButton = Button(top, text="Sign up", command = Menu.signup)
        usernameLabel.pack()
        usernameEntry.pack()
        passwordLabel.pack()
        passwordEntry.pack()
        signinButton.pack()
        signupButton.pack()

    def signup():
        top = Toplevel()
        username = StringVar()
        password = StringVar()
        cpassword = StringVar()
        birthday = StringVar()
        email = StringVar()
        phoneNumber = StringVar()
        top.title("Create an account")
        usernameLabel = Label(top, text="Username: ")
        usernameEntry = Entry(top, textvariable=username)
        passwordLabel = Label(top, text="Password")
        passwordEntry = Entry(top, textvariable=password, show="*")
        confirmpasswordLabel = Label(top, text="Confirm Password")
        confirmpasswordEntry = Entry(top, textvariable=cpassword, show="*")
        birthdayLabel = Label(top, text="Birthday")
        birthdayEntry = Entry(top, textvariable=birthday)
        emailLabel = Label(top, text="Email: ")
        emailEntry = Entry(top, textvariable=email)
        phoneNumberLabel = Label(top, text="Phone Number:")
        phoneNumberEntry = Entry(top, textvariable=phoneNumber)
        vars = [usernameLabel,usernameEntry,passwordLabel,passwordEntry,confirmpasswordLabel,confirmpasswordEntry,birthdayLabel,birthdayEntry,emailLabel,emailEntry,phoneNumberLabel,phoneNumberEntry]
        for thing in vars:
            thing.pack()

if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    app.master.title("Library System")
    app.makeMenu()
    app.mainloop()