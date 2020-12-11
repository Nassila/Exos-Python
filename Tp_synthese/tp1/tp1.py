from sqlite3 import *

connection = connect("GestionCompte.db")
cursor = connection.cursor()


def creation_tables():
    cursor.execute("""CREATE TABLE "Client" (
        "idClient"	INTEGER UNIQUE,
        "civilite"	TEXT,
        "nom"	TEXT,
        "prenom"	TEXT,
        "adresse"	TEXT,
        PRIMARY KEY("idClient" AUTOINCREMENT)
    );""")

    cursor.execute("""CREATE TABLE "CompteBancaire" (
        "idCompte"	INTEGER UNIQUE,
        "solde"	REAL,
        "decouvert"	REAL,
        "idClient"	INTEGER,
        "idAgence"	INTEGER,
        UNIQUE("idClient","idAgence"),
        CONSTRAINT "fk_agence" FOREIGN KEY("idAgence") REFERENCES "Agence"("idAgence"),
        FOREIGN KEY("idClient") REFERENCES "Client"("idClient"),
        PRIMARY KEY("idCompte" AUTOINCREMENT)
    );""")

    cursor.execute("""CREATE TABLE "Agence" (
    "idAgence"	INTEGER UNIQUE,
    "nomAgence"	TEXT,
    PRIMARY KEY("idAgence" AUTOINCREMENT)
    );""")


def ajouter_client(client):
    cursor.execute('INSERT INTO Client (civilite, nom, prenom, adresse) VALUES(?,?,?,?)', client)
    connection.commit()
    print("client ajouté")


def ajouter_agence(agence):
    cursor.execute('INSERT INTO Agence (nomAgence) VALUES(?)', agence)
    connection.commit()
    print("Agence ajoutée")


def ajouter_compte(compte):
    cursor.execute('INSERT INTO CompteBancaire (solde, decouvert, idClient, idAgence) VALUES(?,?,?,?)', compte)
    connection.commit()
    print("compte ajouté")


def lister_client():
    cursor.execute('SELECT * FROM Client')
    print(cursor.fetchall())


def lister_compte():
    cursor.execute('SELECT * FROM CompteBancaire')
    print(cursor.fetchall())


def lister_agence():
    cursor.execute('SELECT * FROM Agence')
    print(cursor.fetchall())


def supprimer_client(client):
    cursor.execute('DELETE FROM Client WHERE idClient=?', client)
    connection.commit()
    print("client supprimé")


def supprimer_compte(compte):
    cursor.execute('DELETE FROM CompteBancaire WHERE idCompte=?', compte)
    connection.commit()
    print("compte supprimé")


def supprimer_agence(agence):
    cursor.execute('DELETE FROM Agence WHERE idAgence=?', agence)
    connection.commit()
    print("agence supprimée")


def modifier_client(client):
    cursor.execute('UPDATE Client SET civilite=?, nom=?, prenom=?, adresse=? WHERE idClient=?', client)
    connection.commit()
    print("client modifié")


def modifier_compte(compte):
    cursor.execute('UPDATE CompteBancaire SET solde=?, decouvert=?, idClient=?, idAgence=? WHERE idCompte=?', compte)
    connection.commit()
    print("compte modifié")


def modifier_Agence(agence):
    cursor.execute('UPDATE Agence SET nomAgence=? WHERE idAgence=?', agence)
    connection.commit()
    print("Agence modifiée")


def ajouter(client, compte, somme):
    cursor.execute('UPDATE CompteBancaire set solde = solde + ? WHERE idClient=? and idCompte=?',
                   (somme, client, compte))
    connection.commit()


def retirer(client, compte, somme):
    cursor.execute('UPDATE CompteBancaire set solde = solde - ? WHERE idClient=? and idCompte=?',
                   (somme, client, compte))
    connection.commit()


def listerCompteAgence(agence):
    cursor.execute('SELECT * FROM CompteBancaire WHERE idAgence=?', agence)
    print(cursor.fetchall())


def listerComptes(client):
    cursor.execute('SELECT * FROM CompteBancaire WHERE idClient=?', client)
    print(cursor.fetchall())


# création des tables
creation_tables()

# ajout clients
clients = [("m", "client1", "cl1", "1 rue rue"),
           ("F", "client2", "cl2", "2 rue rue"),
           ("F", "client3", "cl3", "3 rue rue")]
for client in clients:
    ajouter_client(client)

# ajout d'une agence
agences = [("BNP",), ("socité generale",)]
for agence in agences:
    ajouter_agence(agence)

# ajout d'un compte
comptes = [(200, 100, 2, 1), (200, 100, 1, 1)]
for compte in comptes:
    ajouter_compte(compte)

# modifier les infos d'un client
client = ("M", "client2", "cl2", "2 rue du lac", 1)
modifier_client(client)

# lister les clients
lister_client()

# lister les agences
lister_agence()

# lister les compte
lister_compte()

# supprimer le client 2
supprimer_client((2,))

# ajouter de l'argent a un compte donné
ajouter(1, 1, 100)

# retirer de l'argent a un compte donné
retirer(1, 1, 50)

# lister les copmtes de l'agence dont l'id = 1
listerCompteAgence((1,))

# lister les copmtes de client dont l'id = 1
listerComptes((1,))

# fermeture
cursor.close()
connection.close()
