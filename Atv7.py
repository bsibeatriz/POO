"""
1. Acrescente na classe Usuario métodos para definir e obter o número de artigos:
a) setNumeroDeArtigos(self, nart)
b) getNumeroDeArtigos(self)
"""

class Usuario:
    pontos = 0
    numeroDeArtigos = 0

    def setNumeroDeArtigos(self, nart):
        if isinstance(nart, int):
            self.numeroDeArtigos = nart
        else:
            print("Erro: o número de artigos deve ser um inteiro.")

    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos

"""
2. Acrescente à classe o método chamado calcPontuacao(), que realiza os cálculos das pontuações
separadamente para cada classe.
"""

class Usuario:
    pontos = 0
    numeroDeArtigos = 0
    
    def setNumeroDeArtigos(self, nart):
        self.numeroDeArtigos = nart
        
    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos
    
    def calcPontuacao(self):
        pass  # método a ser implementado nas subclasses


class Autor(Usuario):
    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 10 + 20


class Editor(Usuario):
    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 15 + 30


"""
3. Crie uma classe chamada Autor que herda da classe de Usuario. Nesta classe (Autor) crie um
método chamado calcPontuacao() que retorna o número de pontuações usando o seguinte
cálculo:

numeroDeArtigos * 10 + 20
"""

class Autor(Usuario):
    
    def calcPontuacao(self):
        return self.numeroDeArtigos * 10 + 20

"""
Agora crie também uma classe chamada Editor que herda da classe Usuario. Nesta classe
(Editor), crie um método chamado calcPontuacao() que retorne o número de pontuações
usando o seguinte cálculo:

numeroDeArtigos * 6 + 15
"""

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.numeroDeArtigos = 0
    
    def setNumeroDeArtigos(self, nart):
        self.numeroDeArtigos = nart
    
    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos
    
    def calcPontuacao(self):
        pass

class Autor(Usuario):
    def calcPontuacao(self):
        return self.numeroDeArtigos * 10 + 20

class Editor(Usuario):
    def calcPontuacao(self):
        return self.numeroDeArtigos * 6 + 15


"""
Crie um objeto chamado autor1, a partir da classe Autor. Agora defina o número de artigos como
8 e imprima as pontuações obtidas pelo autor.
"""

from abc import ABC, abstractmethod

class Usuario:
    pontos = 0
    numeroDeArtigos = 0

    def setNumeroDeArtigos(self, nart):
        self.numeroDeArtigos = nart

    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos

    def calcPontuacao(self):
        pass

class Autor(Usuario):
    def calcPontuacao(self):
        return self.numeroDeArtigos * 10 + 20


autor1 = Autor()
autor1.setNumeroDeArtigos(8)


print("Pontuação do autor1:", autor1.calcPontuacao())


"""
Crie outro objeto chamado editor1, a partir da classe Editor. Agora defina o número de artigos
para 15 e imprima as pontuações que o editor ganhou.
"""

class Usuario:
    pontos = 0
    numeroDeArtigos = 0
    
    def setNumeroDeArtigos(self, nart):
        self.numeroDeArtigos = nart
        
    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos
    
    def calcPontuacao(self):
        pass

class Autor(Usuario):
    def calcPontuacao(self):
        return self.numeroDeArtigos * 10 + 20

class Editor(Usuario):
    def calcPontuacao(self):
        return self.numeroDeArtigos * 6 + 15

# criando o objeto autor1 da classe Autor
autor1 = Autor()
autor1.setNumeroDeArtigos(8)
print(f"A pontuação do autor é: {autor1.calcPontuacao()}")

# criando o objeto editor1 da classe Editor
editor1 = Editor()
editor1.setNumeroDeArtigos(15)
print(f"A pontuação do editor é: {editor1.calcPontuacao()}")

#------------------------------------------------------------------------------------------------------------

"""
Crie uma hierarquia de classes para animais, com uma classe mãe Animal e subclasses Cachorro,
Gato e Peixe. Cada subclasse deve ter um método falar() que retorne uma string
representando o som que o animal faz. Demonstre o polimorfismo chamando falar() nas
instâncias de cada subclasse.
"""
class Animal:
    def falar(self):
        pass
    
class Cachorro(Animal):
    def falar(self):
        return "Au au"
    
class Gato(Animal):
    def falar(self):
        return "Miau"
    
class Peixe(Animal):
    def falar(self):
        return "blub"
    
cachorro = Cachorro()
gato = Gato()
peixe = Peixe()

print(cachorro.falar())
print(gato.falar()) 
print(peixe.falar()) 

"""
Crie uma classe Animal com um método falar(). Em seguida, crie duas classes filhas,
Cachorro e Gato, que herdam da classe Animal. Cada uma destas classes filhas deve ter seu
próprio método falar() que retorne um som diferente (e.g. latidos para o cachorro e miados para
o gato). Em seguida, crie uma lista de animais que inclua um cachorro e um gato. Por fim, itere
sobre a lista e chame o método falar() de cada animal.
"""

class Animal:
    def falar(self):
        return "..."
    
class Cachorro(Animal):
    def falar(self):
        return "Au au"
    
class Gato(Animal):
    def falar(self):
        return "Miau"
    
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())

"""
Crie uma classe chamada Carro com um método dirigir(). Em seguida, crie duas subclasses,
CarroGasolina e CarroEletrico, cada uma com sua própria implementação de dirigir().
Demonstre o polimorfismo passando instâncias de ambas as subclasses para uma função que recebe
um objeto Carro.
"""

class Carro:
    def dirigir(self):
        print("Dirigindo carro")

class CarroGasolina(Carro):
    def dirigir(self):
        print("Dirigindo carro a gasolina")

class CarroEletrico(Carro):
    def dirigir(self):
        print("Dirigindo carro elétrico")

def test_drive(carro):
    carro.dirigir()

carro1 = Carro()
carro2 = CarroGasolina()
carro3 = CarroEletrico()

test_drive(carro1)  
test_drive(carro2)  
test_drive(carro3)  

"""
Crie uma classe Forma com um método area(). Em seguida, crie duas classes filhas, Circulo e
Quadrado, que herdam da classe Forma. Cada uma destas classes filhas deve ter seu próprio
método area() que calcula a área do círculo ou do quadrado, respectivamente. Em seguida, crie
uma lista de formas que inclua um círculo e um quadrado. Por fim, itere sobre a lista e chame o
método area() de cada forma.
"""
import math

class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio**2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2

formas = [Circulo(5), Quadrado(3)]
for forma in formas:
    print(f"A área da forma é {forma.area()}")


"""
Crie uma classe Empregado com um método pagar_salario(). Em seguida, crie duas classes
filhas, EmpregadoHora e EmpregadoMes, que herdam da classe Empregado. Cada uma das
classes filhas deve ter seu próprio método pagar_salario() que calcula o salário com base no
número de horas trabalhadas ou no salário mensal, respectivamente. Em seguida, crie uma lista de
funcionários que inclua um funcionário horista e um funcionário mensalista. Por fim, itere sobre a
lista e chame o método pagar_salario() de cada funcionário.
"""

class Empregado:
    def __init__(self, nome):
        self.nome = nome
        
    def pagar_salario(self):
        pass

class EmpregadoHora(Empregado):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
        
    def pagar_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        return salario

class EmpregadoMes(Empregado):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal
        
    def pagar_salario(self):
        return self.salario_mensal


"""
Crie uma classe chamada ContaBancaria com os métodos deposito() e retirada(). Crie
duas subclasses: ContaPoupanca e ContaCorrente. Cada uma dessas subclasses deve ter sua
própria taxa de juros (a taxa de juros da Conta Poupança é maior que a da Conta Corrente).
"""

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def deposito(self, valor):
        self.saldo += valor
    
    def retirada(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
        self.taxa_juros = 0.05
    
    def calcular_juros(self):
        self.saldo += self.saldo * self.taxa_juros

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo):
        super().__init__(saldo)
        self.taxa_juros = 0.01

    def calcular_juros(self):
        self.saldo += self.saldo * self.taxa_juros


poupanca = ContaPoupanca(1000)
corrente = ContaCorrente(2000)

print("Saldo inicial da conta poupança:", poupanca.saldo)
poupanca.deposito(500)
print("Saldo após depósito na conta poupança:", poupanca.saldo)
poupanca.calcular_juros()
print("Saldo após cálculo de juros na conta poupança:", poupanca.saldo)

print("\nSaldo inicial da conta corrente:", corrente.saldo)
corrente.retirada(1500)
print("Saldo após retirada na conta corrente:", corrente.saldo)
corrente.calcular_juros()
print("Saldo após cálculo de juros na conta corrente:", corrente.saldo)
