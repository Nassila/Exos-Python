#coding:utf-8
prenom = str(input("Quel est votre prenom ?"))
nom = str(input("Quel est votre nom ?"))
age = int(input("Quel est votre age ?"))

print("tu t'appelles {}, {} et tu as {} ans".format(prenom,nom, age))

age10 = age + 10
print("tu auras {} dans 10 ans".format(age10))