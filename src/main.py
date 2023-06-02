# substituí 'Combustivel' por 'Comb'
# 'tipoComb' = tipoCombustivel
# 'qtdComb' = quantidadeCombustivel
# 'abastPorValor' = abastecerPorValor
# 'abastPorLitro' = abastecerPorLitro

class bombaCombustivel:

    def __init__(self, tipoComb, valorLitro, qtdComb):
        self.tipoComb = tipoComb
        self.valorLitro = valorLitro
        self.qtdComb = qtdComb
        
    def abastPorValor(self, valorAbast):
        abastecimentoValor = 0.0
        abastecimentoValor = valorAbast/self.valorLitro
        self.qtdComb = self.qtdComb + abastecimentoValor

    def abastPorLitro(self, qtdLitros, ):
        abastPreco = 0
        abastPreco = qtdLitros*self.valorLitro
        self.qtdComb = self.qtdComb + qtdLitros

    def alterarValor(self, novoPreco):
        self.valorLitro = novoPreco

    def alterarComb(self, tipo):
        self.tipoComb = tipo

    def alterarQtd(self, novaQtd):
        self.qtdComb = novaQtd

class Carro:

    def __init__(self, consumo, km, capacidade):
        self.consumo = consumo
        self.km = km
        self.capacidade = capacidade
        self.comb = 0

    def andar(self, km):
        self.km += km
        self.comb -= (km / self.consumo)    

    def obterGas(self):
        return self.comb

    def addGas(self, abastecer):
        self.comb += abastecer
