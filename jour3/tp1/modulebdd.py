from sqlite3 import *

def creationTbales():
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()

	cursor.execute("""CREATE TABLE Matiere (
		Matiere	INTEGER,
		nomMatiere	TEXT,
		PRIMARY KEY(Matiere AUTOINCREMENT)
	);""")

	cursor.execute("""CREATE TABLE Cursus (
		idCursus	INTEGER,
		nomCursus	TEXT,
		PRIMARY KEY(idCursus AUTOINCREMENT)
	);""")

	cursor.execute("""CREATE TABLE Etudiant (
		idEtudiant	INTEGER,
		nomEtudiant	TEXT,
		prenomEtudiant	TEXT,
		age	INTEGER,
		idCursus	INTEGER,
		FOREIGN KEY(idCursus) REFERENCES Cursus(idCursus),
		PRIMARY KEY(idEtudiant AUTOINCREMENT)
	);""")

	cursor.execute("""CREATE TABLE "MatiereCursus" (
		"idMatiere"	INTEGER NOT NULL,
		"idCursus"	INTEGER NOT NULL,
		PRIMARY KEY("idMatiere","idCursus"),
		FOREIGN KEY("idCursus") REFERENCES "Cursus"("idCursus"),
		FOREIGN KEY("idMatiere") REFERENCES "Matiere"("idMatiere")
	);""")

	cursor.close()
	connection.close()
	

def ajouterMatiere(matiere):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('INSERT INTO Matiere VALUES(?,?)', matiere)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def ajouterCursus(cursus):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('INSERT INTO Cursus VALUES(?,?)', cursus)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def ajouterEtudiant(etudiant):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('INSERT INTO Etudiant VALUES(?,?,?,?,?)', etudiant)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def ajouterMatierCursus(matier_cursus):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('INSERT INTO MatiereCursus VALUES(?,?)', matier_cursus)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def listerMatiere():
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM Matiere')
	print(cursor.fetchall())
	cursor.close()
	connection.close()

def listerCursus():
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM Cursus')
	print(cursor.fetchall())
	cursor.close()
	connection.close()

def listerEtudiant():
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM Etudiant')
	print(cursor.fetchall())
	cursor.close()
	connection.close()

def modifierMatiere(matiere):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('UPDATE Matiere SET nomMatiere=? WHERE idMatiere=?', matiere)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def modifierCursus(cursus):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('UPDATE Cursus SET nomCursus=? WHERE idCursus=?', cursus)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def modifierEtudiant(etudiant):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('UPDATE Etudiant SET nomEtudiant=?, prenomEtudiant=?, age=?, idCursus=? WHERE idEtudiant=?', etudiant)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def supprimerMatiere(matiere):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('DELETE FROM Matiere WHERE idMatiere=?', matiere)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def supprimerCursus(cursus):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('DELETE FROM Cursus WHERE idCursus=?', cursus)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def supprimerEtudiant(etudiant):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('DELETE FROM Etudiant WHERE idEtudiant=?', etudiant)
	connection.commit()
	print("ok")
	cursor.close()
	connection.close()

def afficherEtudiantDeCursus(cursus):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('SELECT idEtudiant, nomEtudiant FROM Etudiant WHERE idCursus=?', cursus)
	print(cursor.fetchall())
	cursor.close()
	connection.close()

def afficherMatiereCursus(cursus):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('SELECT idMatiere FROM MatiereCursus WHERE idCursus=?', cursus)
	print(cursor.fetchall())
	cursor.close()
	connection.close()

def afficherCursurs(matiere):
	connection = connect("GestionFormation.db")
	cursor = connection.cursor()
	cursor.execute('SELECT idCursus FROM MatiereCursus WHERE idMatiere=?', matiere)
	print(cursor.fetchall())
	cursor.close()
	connection.close()

