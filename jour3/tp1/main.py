from sqlite3 import *
#CRUD : create, read, update, delete

import modulebdd

#connexion
connection = connect("GestionFormation.db")
cursor = connection.cursor() 

#création des tables
modulebdd.creationTbales()

#remplir les tables

cursus = [(cursor.lastrowid, "Langage de programmation"), (cursor.lastrowid, "Big data"), (cursor.lastrowid, "Securité")]
for c in cursus:
	modulebdd.ajouterCursus(c)

etudiant = [(cursor.lastrowid, "etudiant1", "toto1", 20, 1),(cursor.lastrowid, "etudiant2", "toto2", 22, 2),(cursor.lastrowid, "etudiant3", "toto3", 21, 1)]
for e in etudiant:
	modulebdd.ajouterEtudiant(e)

matiere = [(cursor.lastrowid, "Java"),(cursor.lastrowid, "Python"),(cursor.lastrowid, "Docker"),(cursor.lastrowid, "Git")]
for m in matiere:
	modulebdd.ajouterMatiere(m)

matiere_cursus = [(1,2),(1,3)]
for mc in matiere_cursus:
	modulebdd.ajouterMatierCursus(mc)

#afficher le contenu des tables
modulebdd.listerMatiere()
modulebdd.listerCursus()
modulebdd.listerEtudiant()

#modifier un etudiant
set_etudiant = ("Etudiant1", "toto1", 25, 1, 0)
modulebdd.modifierEtudiant(set_etudiant)

#supprimer un cursus
del_cursus = (4,)
modulebdd.supprimerCursus(del_cursus)

afficheMatier = (1,)
modulebdd.afficherMatiereCursus(afficheMatier)

#fermeture
cursor.close()
connection.close()