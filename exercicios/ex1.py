class Bola:
    def __init__(self, cor, circunf, material):
        self.cor = cor
        self.circunf = circunf
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)  