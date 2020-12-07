#coding:utf-8
devise = str(input("Entre la devise "))
print("ta devise de depart {} est".format(devise))
if (devise == "€"):
	print("converti en $")
else:
	print("converti en €")