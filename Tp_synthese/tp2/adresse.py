class Adresse:
    def __init__(self, rue, ville, codePostal):
        self._rue = rue
        self._ville = ville
        self._codePostal = codePostal

    @property
    def rue(self):
        return self._rue

    @property
    def ville(self):
        return self._ville

    @property
    def codePostal(self):
        return self._codePostal

    @rue.setter
    def rue(self, r):
        self._rue = r

    @ville.setter
    def ville(self, v):
        self._ville = v

    @codePostal.setter
    def codePostal(self, c):
        self._codePostal = c
