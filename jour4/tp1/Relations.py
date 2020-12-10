#Tp Relations
class Ville:
	"""Ville"""
	def __init__(self,nomVille):
		self._nomVille = nomVille
		self._batiments = []

	@property
	def nomVille(self):
		return self._nomVille

	@nomVille.setter
	def nomVille(self,v):
		self._nomVille = v
	#Methodes de gestion de la liste des bâtiments
	def get_batiments(self):
		return self._batiments

	def add_batiments(self,b):
		if b not in self._batiments:
			self._batiments.append(b)
	def remove_batiments(self,b):
		if b in self._batiments:
			self._batiments.remove(b)
	#methode demandée
	def liste_villes(self):
		return len(self._batiments)

	def afficher_nbr_bat(self):
		return len(self._batiments)

class Batiment:
	"""Batiments"""
	def __init__(self,nomBat):
		self._nomBat = nomBat
		self._employes = []
	@property
	def nomBat(self):
		return self._nomBat

	@nomBat.setter
	def nomBat(self,b):
		self._nomBat = b

	#Methodes de gestion des employes
	def get_employes(self):
		return self._employes

	def add_employes(self,e):
		if e not in self._employes:
			self._employes.append(e)
	def remove_employes(self,e):
		if e in self._employes:
			self._employes.remove(e)

class Employe:
	"""Employes"""
	def __init__(self,nom,prenom):
		self._nom = nom
		self._prenom = prenom

	@property
	def nom(self):
		return self._nom

	@nom.setter
	def nomBat(self,n):
		self._nom = n
	@property
	def prenom(self):
		return self._prenom

	@nomBat.setter
	def prenom(self,p):
		self._prenom = p

class Entreprise:
	"""Entreprises"""
	def __init__(self,nomEntr):
		self._nomEntr = nomEntr
		self._batiments =[]
		self._villes =[]
	@property
	def nomEntr(self):
		return self._nomEntr

	@nomEntr.setter
	def nomEntr(self,e):
		self._nomEntr = e

	#Methodes de gestion de la liste des bâtiments
	def get_batiments(self):
		return self._batiments

	def add_batiments(self,b):
		if b not in self._batiments:
			self._batiments.append(b)
	def remove_batiments(self,b):
		if b in self._batiments:
			self._batiments.remove(b)

	#Methodes de gestion de la liste des villes
	def get_villes(self):
		return self._villes

	def add_villes(self,v):
		if v not in self._villes:
			self._villes.append(v)
	def remove_villes(self,v):
		if v in self._villes:
			self._villes.remove(v)

	def afficher_nbr_bat(self):
		return len(self._batiments)

entreprise = Entreprise("Entreprise1")

ville1 = Ville("Paris")
ville2 = Ville("Evry")

bat1 = Batiment("bat1")
bat2 = Batiment("Bat2")
bat3 = Batiment("Bat3")

emp1 = Employe("nom1", "prenom1")
emp2 = Employe("nom2", "prenom2")
emp3 = Employe("nom3", "prenom3")
emp4 = Employe("nom4", "prenom4")
emp5 = Employe("nom5", "prenom5")
emp6 = Employe("nom6", "prenom6")

entreprise.add_villes([ville1,ville2])
print(entreprise.get_villes())

ville1.add_batiments([bat3, bat2])
ville2.add_batiments([bat1])
print(ville1.get_batiments())

bat1.add_employes([emp1, emp3])
bat2.add_employes([emp4, emp2])
bat3.add_employes([emp5, emp6])

entreprise.add_batiments([bat3, bat2])

print(bat1.get_employes())

entreprise.afficher_nbr_bat()
