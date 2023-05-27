'''
2. Classe Quadrado: Crie uma classe que modele um quadrado:

a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:
    def __init__(self, tam_lado):
        self.tam_lado = tam_lado
        
    def mudar_tam(self, novo_tam):
        self.tam_lado = novo_tam

    def ret_tam(self):
        self.tam_lado

    def calc_tam(self):
        self.tam_lado*2
