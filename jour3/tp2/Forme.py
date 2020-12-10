class Forme:
	def __init__(self,point,origine):
		self.point = point
		self.origine = origine
		
	#redefinition de la méthode d'affichage
	def __str__(self):
		return "{} \n{}\n{}\n{}".format(self.point,self.origine)
		# definition des autres autres methodes
	def calculer_distance(self):
		print("calculer_distance ...")

	def calculer_preimetre(self):
		print("calculer_preimetre ...")

	def afficher(self):
		print("afficher ...")

class Rectangle(Forme):
	def __init__(self,point,origine):
		Forme.__init__(self,point,origine)
	
	def calculer_distance(self):
		print("argent...")

	def calculer_preimetre(self):
		print("calculer_preimetre ...")

class Cercle(Forme):
	def __init__(self,point,origine):
		Forme.__init__(self,point,origine)
	
	def calculer_distance(self):
		print("argent...")

	def calculer_preimetre(self):
		print("calculer_preimetre ...")