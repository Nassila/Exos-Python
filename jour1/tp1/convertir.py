#coding:utf-8
montant = int(input("Entre le montant de la somme à convertir "))
devise = str(input("Entre la devise "))
if (devise == "€"):
	print("montant en € en {}".format(montant*0.83))
else:
	print("montant en $ en {}".format(montant/0.83))