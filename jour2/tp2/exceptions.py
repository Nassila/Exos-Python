def div(a,b):
	return a/b

while True:
	try:
		a = int(input("Entre le primer number "))
		b = int(input("Entre le primer number "))
		assert a, b == int
		assert b != 0
		assert (a % 2) == 0
		print(div(a,b))
	except ValueError:
		print("Valeur Erreur")
	




   

