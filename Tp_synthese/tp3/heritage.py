class Alphabet:
    def __init__(self, mot):
        self._mot = mot

    @property
    def mot(self):
        return self._mot

    @mot.setter
    def mot(self, m):
        self._mot = m

    def info(self):
        print("info sur la classe Alphabet")

    def test1(self):
        print("run test1 de la classe Alphabet")

    def test2(self):
        print("run test2 de la classe Alphabet")


class A(Alphabet):
    def __init__(self, mot):
        Alphabet.__init__(self, mot)

    def info(self):
        print("info sur la classe A")

    def test1(self):
        print("run test1 de la classe A")

class Accent:
    pass

    def info(self):
        print("info sur la classe Accent")

    def test2(self):
        print("run test2 de la classe Accent")

    def test3(self):
        print("run test3 de la classe Accent")


class Mot:

    def info(self):
        print("info sur la classe Mot")

    def test1(self):
        print("run test1 de la classe Mot")

    def test3(self):
        print("run test3 de la classe Mot")


class Abracadabra(Mot):
    pass

    def test1(self):
        print("run test1 de la classe Abracadabra")


class AGrave(A, Accent, Abracadabra):

    def test4(self):
        print("run test4 de la classe AGrave")


aAccentGrave = AGrave("à")
print(aAccentGrave.mot)
aAccentGrave.test1()
aAccentGrave.test2()
aAccentGrave.test3()
aAccentGrave.test4()

"""
*********** une conclusion concernant l’appel des méthodes dans le cadre d’un héritage multiple*********

1 : une classe fille peut appeler les methodes de ses classes méres et les méthodes des classes méres des ses classes méres
===> autrement dit :
les methodes d'une classe mére peuvent être appelées par toutes les classes descendantes de cette classe mére

2 : une methode de classe mére peut être redefini dans sa classe fille

3 : l'ordre des classes (de gauche a droite) dans l'héritage multiple est important car c'est selon cette 
ordre que les méthodes de classes sont appelées; les méthodes de la classe la plus à gauche sont prioritaire par rapprot
aux méthodes des classes de droite

"""
