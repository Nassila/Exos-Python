import adresse
import personne
import pickle


class ListPersonnes:
    def __init__(self, personnes):
        self._personnes = personnes

    def __str__(self):
        personnes = ""
        for personne in self._personnes:
            personnes = personnes + "nom : {}, sexe : {}".format(personne.nom, personne.sexe) + " \n"
        return personnes

    @property
    def personnes(self):
        return self._personnes

    @personnes.setter
    def personnes(self, p):
        self._personnes = p

    def find_by_nom(self, s: str):
        for personne in self._personnes:
            if personne.nom == s:
                return personne
            else:
                return None

    def exists_code_postal(self, cp: str):
        for personne in self._personnes:
            if len(personne.adresses) > 0:
                for adresse in personne.adresses:
                    if adresse.codePostal == cp:
                        return True
        return False

    def count_personne_ville(self, ville: str):
        count = 0
        for personne in self._personnes:
            if len(personne.adresses) > 0:
                for adresse in personne.adresses:
                    if adresse.ville == ville:
                        count = count + 1
                        break
        return count

    def edit_personne_nom(self, oldNom: str, newNom: str):
        for personne in self._personnes:
            if personne.nom == oldNom:
                personne.nom = newNom
                print("nom modifié en {}".format(personne.nom))

    def edit_personne_ville(self, nom: str, newVille: str):
        for personne in self._personnes:
            if personne.nom == nom:
                personne.adresses[0].ville = newVille
                print("ville modifiée en {}".format(personne.adresses[0].ville))

    def write_to_file(self, fichier: str):
        with open(fichier, "wb") as fic:
            record = pickle.Pickler(fic)
            record.dump(self._personnes)

    def read_from_file(self, fichier: str):
        with open(fichier, "rb") as fic:
            get_record = pickle.Unpickler(fic)
            return get_record.load()

a1 = adresse.Adresse("rue de champs", "Paris", "75003")
a2 = adresse.Adresse("rue de jacque prevert", "Evry", "91000")
a3 = adresse.Adresse("rue de julles valles", "Evry", "91000")

personne1 = personne.Personne("nom1", "M", [a1])
personne2 = personne.Personne("nom2", "F", [a2])
personne3 = personne.Personne("nom3", "F", [a3])

listPersonne = ListPersonnes([personne1, personne2, personne3])
print(listPersonne.find_by_nom("nom1"))

print(listPersonne.exists_code_postal("75003")) #return true
print(listPersonne.exists_code_postal("75013")) #return false

print(listPersonne.count_personne_ville("Evry"))
listPersonne.edit_personne_nom("nom1", "sila")

listPersonne.edit_personne_ville("sila", "Creteil")
listPersonne.write_to_file("personnes.txt")

print(listPersonne.read_from_file("personnes.txt"))