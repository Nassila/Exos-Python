#coding:utf-8

#qet 1
dico = {"ordinateur": "computer", "lit": "bed","oreiller": "pillow" , "chaise": "chair", "eau": "water"}

#qst 2
dico["livre"] = "book"

#qst 3
for cle, valeur in dico.items():
	print("l'élément {} correspand a la clé {}".format(valeur, cle))

#qst 4
new_dict = {key for key in dico if key.startswith('c')}
for key in new_dict: 
	del dico[key]

print(dico.values())