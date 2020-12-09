class Personnage:
	def __init__(self,position,vie,puissance,type1,endurance):
		self.position = position
		self.vie = vie
		self.puissance = puissance
		self.type1 = type1
		self.endurance = endurance
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.position,self.vie,self.puissance,self.type1,self.endurance)
		# definition des autres autres methodes
	def est_vivant(self):
		print("vivant ...")

	def se_deplacer(self,h, v):
		print("vivant ...")
		
	def attaquer(self, autre_personnage):
		print("vivant ...")
		
	def informations(self):
		print("vivant ...")
					
#Mère
class Item:
	#constructeur
	def __init__(self,prix,description):
		self.prix = prix
		self.description = description
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.prix,self.description)
	

#Classe Fille
class Mero(Personnage):
	def __init__(self,position,vie,puissance,type1,endurance,inventaire, arme,argent):
		Personnage.__init__(self,position,vie,puissance,type1,endurance)
		self.inventaire = inventaire
		self.arme = arme
		self.argent = argent 
	def ramasser_item(self, item):
		print("Item...")

	def vendre_item(self, item):
		print("Item...")

	def utiliser_item(self, item):
		print("Item...")

	def charger_arme(self, arme):
		print("arme...")

#Classe Fille
class Monstre(Personnage):
	def __init__(self,position,vie,puissance,type1,endurance, nombre_de_pattes, cri, dormir):
		Personnage.__init__(self,position,vie,puissance,type1,endurance)
		self.nombre_de_pattes = nombre_de_pattes
		self.cri = cri
		self.dormir = dormir
	def crier(self):
		print("crier...")

	def est_eveiller(self):
		print("est_eveiller...")

#Classe Fille
class Potion(Item):
	def __init__(self,prix,description,vie):
		Item.__init__(self,prix,description)
		self.vie = vie 
	
	def comnien_de_vie(self):
		print("vie...")

#Classe Fille
class Or(Item):
	def __init__(self,prix,description,valeur):
		Item.__init__(self,prix,description)
		self.valeur = valeur
	
	def combien_argent(self):
		print("argent...")


