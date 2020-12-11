from tkinter import *
import sqlite3
from tkinter import messagebox

"""
pour le test:
la base de données contient:
----------1---------
login : toto
password : toto
----------2---------
login : admin
password : admin
"""

def connect():
    conn = sqlite3.connect('tt_users.db')
    curs = conn.cursor()
    curs.execute('SELECT * FROM personne WHERE login=? and  password=?', (loginVar.get(), passwordVar.get()))
    if curs.fetchone():
        messagebox.showinfo("connected", "utilisateur connecté")
        loginVar.set("")
        passwordVar.set("")
    else:
        messagebox.showwarning("error", "erreur de connexion")

window= Tk()
window.title("TP4: tkinter et BDD (optionnel)")
window.geometry("%dx%d+0+0" % (400, 400))

loginLabel = Label(window, text="Login")

loginVar = StringVar()
loginEntry = Entry(window,textvariable=loginVar)

passwordlabel = Label(window, text="Password")

passwordVar = StringVar()
passwordEntry = Entry(window,textvariable=passwordVar)

connexionBtn = Button(window, text="connexion", command=connect)


loginLabel.pack()
loginEntry.pack()
passwordlabel.pack()
passwordEntry.pack()
connexionBtn.pack()
window.mainloop()