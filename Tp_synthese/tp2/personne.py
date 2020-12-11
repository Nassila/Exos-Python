class Personne:
    def __init__(self, nom, sexe, adresses):
        self._nom = nom
        self._sexe = sexe
        self._adresses = adresses

    def __str__(self):
        return "nom : {}, sexe : {}".format(self._nom, self._sexe)


    @property
    def nom(self):
        return self._nom

    @property
    def sexe(self):
        return self._sexe

    @property
    def adresses(self):
        return self._adresses

    @nom.setter
    def nom(self, n):
        self._nom = n

    @sexe.setter
    def sexe(self, s):
        self._sexe = s

    @adresses.setter
    def adresses(self, a):
        self._adresses = a