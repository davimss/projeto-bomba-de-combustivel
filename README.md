# Estudos sobre Classes e Orientação a Objeto

Este é um repositório dedicado a um projeto/exercício de Classes, Orientação a Objetos e exercícios complementares.

# Bomba de Combustível

Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

1. Possua uma classe chamada bombaCombustível,
com no mínimo esses atributos:

        1. tipoCombustivel.
        2. valorLitro
        3. quantidadeCombustivel                    

2. Possua no mínimo esses métodos:

        I. abastecerPorValor( ) – método onde é informado o valor a ser
       abastecido e mostra a quantidade de litros que foi colocada no veículo.

        II. abastecerPorLitro( ) – método onde é informado a quantidade em litros
        de combustível e mostra o valor a ser pago pelo cliente.

        III. alterarValor( ) – altera o valor do litro do combustível.

        IV. alterarCombustivel( ) – altera o tipo do combustível.

        V. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    
_OBS: Sempre que acontecer um abastecimento, é necessário atualizar
a quantidade de combustível total na bomba._

# Classe Carro

Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

1. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
2. O consumo é especificado no construtor e o nível de combustível inicial é 0.
3. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
4. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
5. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

```
meuFusca = Carro(15);

15 quilômetros por litro de combustível.
```

```
meuFusca.adicionarGasolina(20);

Abastece com 20 litros de combustível.
```

```
meuFusca.andar(100);     

Anda 100 quilômetros.    
```

```
meuFusca.obterGasolina()     

Imprime o combustível que resta no tanque.
```

* [Projeto Bomba de Combustível e Classe Carro](src/main.py)


<!-- EXERCÍCIOS COMPLEMENTARES -->

# Exercícios Complementares

São exercícios de Classes retirados do site https://wiki.python.org.br/ExerciciosClasses.


1. Classe Bola: Crie uma classe que modele uma bola:

        I. Atributos: Cor, circunferência, material
        
        II. Métodos: trocaCor e mostraCor

* [Exercício 1](exercicios/ex1.py)

2. Classe Quadrado: Crie uma classe que modele um quadrado:

        I. Atributos: Tamanho do lado

        II. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

* [Exercício 2](exercicios/ex2.py)

# Licença

<img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361?color=rgb(89,101,224)">

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

# Contato

Me acompanhe nas redes sociais.

<p align="center">


  <a href="https://www.instagram.com/ddavimig/" target="_blank" >
    <img alt="Instagram" src="https://img.shields.io/badge/-Instagram-ff2b8e?logo=Instagram&logoColor=white"></a>

  <a href="https://www.linkedin.com/in/davimss/" target="_blank" >
    <img alt="Linkedin" src="https://img.shields.io/badge/-Linkedin-blue?logo=Linkedin&logoColor=white"></a>

  <a href="mailto:davi00msantos@gmail.com" target="_blank" >
    <img alt="Email" src="https://img.shields.io/badge/-Email-c14438?logo=Gmail&logoColor=white"></a>

</p>