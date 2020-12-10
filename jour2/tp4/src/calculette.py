class Calculette:
    def add(self,a, b):
        """Méthode pour l'addition"""
        return a + b
    def sous(self, a, b):
        """Méthode pour la soustraction"""
        return  a - b
    def mult(self, a, b):
         """Méthode pour la multiplication"""
         return a * b
    def div(self,a, b):
        """Méthode pour la division"""
        try:
            return a/b
        except ZeroDivisionError:
            print("Veuillez saisir une valeur différente de 0 pour la division")