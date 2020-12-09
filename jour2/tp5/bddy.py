from sqlite3 import *
#CRUD : create, read, update, delete

#connexion
connection = connect("base.db")
cursor = connection.cursor()

#requetes
"""
ajout d'un etudiant
new_etudiant = (cursor.lastrowid, "toto2", "tata1", 20)
cursor.execute('INSERT INTO etudiant VALUES(?,?,?,?)', new_etudiant)
connection.commit()
print("ok")
"""
"""
€affiche toute les lignes
cursor.execute('SELECT * FROM etudiant')
print(cursor.fetchall())
"""
"""
#affiche une ligne
my_etudiant= (1,)
cursor.execute('SELECT * FROM etudiant WHERE id=?', my_etudiant)
print(cursor.fetchone())
"""

#modifier une ligne
"""
set_etudiant= ('TestModif', 'TEST1', 20, 1)
cursor.execute('UPDATE etudiant SET nom=?, prenom=?, age=? WHERE id=?', set_etudiant)
connection.commit()
print("ok")
"""

#supprimer une ligne
del_etudiant= (1,)
cursor.execute('DELETE FROM etudiant WHERE id=?', del_etudiant)
connection.commit()
print("ok")

#fermeture
cursor.close()
connection.close()