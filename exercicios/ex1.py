'''
1. Classe Bola: Crie uma classe que modele uma bola:

a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor
'''

class Bola:
    def __init__(self, cor, circunf, material):
        self.cor = cor
        self.circunf = circunf
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)  