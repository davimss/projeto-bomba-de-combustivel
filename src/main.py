''' Classe Bomba de Combustível: Faça um programa completo
utilizando classes e métodos que:

a. Possua uma classe chamada bombaCombustível,
com no mínimo esses atributos:

    i. tipoCombustivel.
   ii. valorLitro
  iii. quantidadeCombustivel

b. Possua no mínimo esses métodos:

    i. abastecerPorValor( ) – método onde é informado o valor a ser
       abastecido e mostra a quantidade de litros que foi colocada no veículo
   ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros
       de combustível e mostra o valor a ser pago pelo cliente.
  iii. alterarValor( ) – altera o valor do litro do combustível.
   iv. alterarCombustivel( ) – altera o tipo do combustível.
    v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    
OBS: Sempre que acontecer um abastecimento é necessário atualizar
 a quantidade de combustível total na bomba.
'''

# substituirei 'Combustivel' por 'Comb'
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

    def abastPorLitro(self, qtdLitros):
        abastPreco = 0
        abastPreco = qtdLitros*self.valorLitro
        self.qtdComb = self.qtdComb + qtdLitros

    def alterarValor(self, novoPreco):
        self.valorLitro = novoPreco

    def alterarComb(self, tipo):
        self.tipoComb = tipo

    def alterarQtd(self, novaQtd):
        self.qtdComb = novaQtd