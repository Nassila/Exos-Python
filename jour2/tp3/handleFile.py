try:
	with open("depart.txt",'r') as fic:
		# récupération du contenu
		content = fic.read()
		# affichage
		print(content)
# Gestion de l'erreur
except FileNotFoundError:
	print("fichier introuvable")

try:
	with open("arrivee.txt",'w') as fic:
		#ecrit le contenu du fichier depart dans le fichier arriee
		fic.write(content)
	
# Gestion de l'erreur
except FileNotFoundError:
	print("fichier introuvable")
