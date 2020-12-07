#coding:utf-8
nbr = int(input("Entre un nombre"))
if (nbr % 2 == 0):
	print("Ce nombre est pair")
elif (nbr % 3 == 0):
	print("Ce nombre est impair, mais est multiple de 3")
else:
	print("Ce nombre n’est ni pair ni multiple de 3")
