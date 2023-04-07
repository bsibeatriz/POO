"""
Crie uma classe Pessoa com os atributos nome e idade. Crie uma classe Aluno que herda de
Pessoa e adicione o atributo nota. Crie um método para imprimir as informações da Pessoa e um
método para imprimir as informações do Aluno.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def imprimir_info(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)


class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
        
    def imprimir_info(self):
        super().imprimir_info()
        print("Nota:", self.nota)


"""
Crie uma classe Veiculo com os atributos marca, modelo e ano. Crie classes filhas Carro e
Moto que adicionam o atributo quantidade_de_portas e cilindradas, respectivamente. Crie
um método para imprimir as informações do Veiculo e um método para imprimir as informações
do Carro e da Moto.
"""
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def imprimir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_de_portas):
        super().__init__(marca, modelo, ano)
        self.quantidade_de_portas = quantidade_de_portas

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f"Quantidade de portas: {self.quantidade_de_portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f"Cilindradas: {self.cilindradas}")


"""
Crie uma classe Animal com os atributos nome e peso, e um método comer(). Em seguida, crie
duas subclasses, Cachorro e Gato, que herdam da classe Animal. Adicione um método
latir() na classe Cachorro e um método miar() na classe Gato.
"""
class Animal:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def comer(self):
        print(f"{self.nome} está comendo.")


class Cachorro(Animal):
    def latir(self):
        print("Au au!")


class Gato(Animal):
    def miar(self):
        print("Miau!")

"""
Crie uma classe Pessoa com os atributos nome e idade. Em seguida, crie uma classe
Funcionario que herda da classe Pessoa e adicione o atributo salario. Crie um método
aumento() na classe Funcionario que aumenta o salário em uma porcentagem específica.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
        
    def aumento(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)


"""
Crie uma classe Forma com o método area(). Em seguida, crie duas subclasses: Retangulo e
Circulo, que herdam da classe Forma. Adicione os atributos comprimento e largura na
classe Retangulo e o atributo raio na classe Circulo. Agora calcula a área de cada polígono.
"""
import math

class Forma:
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def area(self):
        return self.comprimento * self.largura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2


"""
crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor()
"""

class Ingresso:
    def __init__(self, valor):
        self.valor = valor
        
    def imprimeValor(self):
        print("Valor do ingresso: R$ {:.2f}".format(self.valor))


"""
crie uma classe VIP que herda de Ingresso e possui um valor adicional. Crie também um método
que retorne o valor do ingresso VIP (como o adicional incluído).
"""
class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print("Valor do ingresso: R$", self.valor)

class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional


"""
crie uma classe Normal, que herda Ingresso e possui um método que imprime: "Ingresso Normal".
"""

class Normal(Ingresso):
    def imprimeTipo(self):
        print("Ingresso Normal")


"""
crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos para acessar e
imprimir esta localização) e uma classe CamaroteSuperior, que é mais cara (possui valor
adicional). Esta última possui um método para retornar o valor do ingresso. Ambas as classes herdam
a classe VIP.
"""
class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor:.2f}")

class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional

class Normal(Ingresso):
    def imprimeTipo(self):
        print("Ingresso Normal")

class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao

    def imprimeLocalizacao(self):
        print(f"Localização: {self.localizacao}")

class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional, valorAdicional):
        super().__init__(valor, adicional)
        self.valorAdicional = valorAdicional

    def valorCamaroteSuperior(self):
        return self.valor + self.adicional + self.valorAdicional

"""
uma classe Funcionario com os atributos (nome, endereço, telefone, email) e com os
métodos (construtor, exibeDados())
"""

class Funcionario:
    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def exibeDados(self):
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)
        print("Telefone:", self.telefone)
        print("E-mail:", self.email)


"""
crie a classe Assistente, que também é Funcionário, e que possui um número de
matrícula (use o método get).
"""

class Funcionario:
    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        
    def exibeDados(self):
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)
        print("Telefone:", self.telefone)
        print("Email:", self.email)
        

class Assistente(Funcionario):
    def __init__(self, nome, endereco, telefone, email, matricula):
        super().__init__(nome, endereco, telefone, email)
        self.matricula = matricula
        
    def getMatricula(self):
        return self.matricula


"""
sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes Administrativos
possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e
Administrativo. Para cada um destas classes, imprima o número de matrícula e o nome de cada
um deles.
"""

class Funcionario:
    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def exibeDados(self):
        print("Nome:", self.nome)
        print("Endereço:", self.endereco)
        print("Telefone:", self.telefone)
        print("Email:", self.email)

class Assistente(Funcionario):
    def __init__(self, nome, endereco, telefone, email, matricula):
        super().__init__(nome, endereco, telefone, email)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

class Tecnico(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, bonus):
        super().__init__(nome, endereco, telefone, email, matricula)
        self.bonus = bonus

    def exibeDados(self):
        super().exibeDados()
        print("Matrícula:", self.matricula)
        print("Bônus salarial:", self.bonus)

class Administrativo(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, turno, adicional_noturno):
        super().__init__(nome, endereco, telefone, email, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    def exibeDados(self):
        super().exibeDados()
        print("Matrícula:", self.matricula)
        print("Turno:", self.turno)
        print("Adicional noturno:", self.adicional_noturno)
