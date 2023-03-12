'''
1. Nós usamos o modificador de acesso private a fim de:

d) B e C estão corretas
'''

'''
Crie uma propriedade na classe Usuario chamada primeiroNome e evite que qualquer código
de fora da classe altere o seu valor, usando o modificador de acesso apropriado.
'''

class Usuario:
    def __init__(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getPrimeiroNome(self):
        return self.__primeiroNome

'''
Crie um método para definir o valor da propriedade primeiroNome. Use o modificador de
acesso correto para ele.
'''

class Usuario:
    def __init__(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getPrimeiroNome(self):
        return self.__primeiroNome

    def setPrimeiroNome(self, novoPrimeiroNome):
        self.__primeiroNome = novoPrimeiroNome

usuario = Usuario("Bea")
usuario.setPrimeiroNome("Beatriz")
print(usuario.getPrimeiroNome()) 



'''
Agora, crie um método para retornar o valor primeiroNome.
'''

class Usuario:
    def __init__(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getPrimeiroNome(self):
        return self.__primeiroNome

    def setPrimeiroNome(self, novoPrimeiroNome):
        self.__primeiroNome = novoPrimeiroNome


usuario = Usuario("Bea")
print(usuario.getPrimeiroNome()) 


'''
Crie um objeto chamado usuario1. Depois defina seu primeiro nome como "Joe" e faça com
que ele retorne este nome.
'''

class Usuario:
    def __init__(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getPrimeiroNome(self):
        return self.__primeiroNome

    def setPrimeiroNome(self, novoPrimeiroNome):
        self.__primeiroNome = novoPrimeiroNome

usuario1 = Usuario("")

usuario1.setPrimeiroNome("Joe")
print(usuario1.getPrimeiroNome()) 

'''
Crie uma classe chamada Empregado(), com três propriedades: nome, salario (deve ser
privada) e projeto. Ela também possui um método chamado “trabalho()”, que deverá
imprimir o nome do funcionário e o projeto em que ele está trabalhando e um outro método
chamado “mostrar()” para exibir os detalhes desse empregado (i.e. nome e salário). Atente
para o modificador de acesso da propriedade “salario”. Use o método adequado para ter
acesso a ela. Crie um objeto desta classe (i.e. instância) e use os métodos para visualizar os
dados.
'''

class Empregado:
    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self.__salario = salario
        self.projeto = projeto
    
    def trabalho(self):
        print(f"{self.nome} está trabalhando no projeto {self.projeto}")
        
    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.__salario}")

empregado1 = Empregado("João", 5000, "Projeto A")

empregado1.trabalho() 
empregado1.mostrar() 

'''
Crie uma classe chamada Robo(). Ela deverá ter duas propriedades privadas: nome e
ano_construcao. Também deverá ter um método de nome “diga_alo()”, para mostrar na
tela o nome do robô e seu ano de construção. Crie os métodos “setters” e “getters”
necessários. Instancie a classe e use os métodos criados para visualizar / atualizar os dados.
'''
class Robo:
    def __init__(self, nome, ano_construcao):
        self.__nome = nome
        self.__ano_construcao = ano_construcao
    
    def diga_alo(self):
        print(f"Olá, eu sou o robô {self.__nome} e fui construído em {self.__ano_construcao}.")
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def get_ano_construcao(self):
        return self.__ano_construcao
    
    def set_ano_construcao(self, novo_ano_construcao):
        self.__ano_construcao = novo_ano_construcao

robo1 = Robo("R2-D2", 1977)

robo1.diga_alo() 
robo1.set_nome("C-3PO")
print(robo1.get_nome()) 
robo1.set_ano_construcao(1976)
print(robo1.get_ano_construcao()) 

'''
Implemente uma classe chamada Laptop que possua um atributo privado chamado “preco”
que armazena o preço do laptop (sem qualquer validação). Em seguida, implemente um método
para ler esse atributo chamado “get_preco()” e um método para modificar esse atributo
chamado “set_preco()” sem validação também. Em seguida, crie uma instância da classe
Laptop siga estas etapas:
• usando o método “get_preco()” imprima o valor do atributo “preco” na tela
• usando o método “set_preco()”, defina o valor do atributo “preco” para 3999”
'''

class Laptop:
    
    def __init__(self):
        self.__preco = 0
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        self.__preco = preco


'''
Implemente uma classe chamada Pessoa que tenha dois atributos privados chamados
“primeiroNome” e “ultimoNome”, respectivamente. Em seguida, implemente métodos
chamados “getPrimeiroNome()” e “getUltimoNome()”, para ler os atributos, e os
métodos “setPrimeiroNome()” e “setUltimoNome()” para atribuir valores a eles. Depois
crie uma instância da classe Pessoa definindo os seguintes valores:
primeiroNome = 'João'
ultimoNome = 'Carvalho'
Após, imprima os valores desses atributos no console.
'''

class Pessoa:
    
    def __init__(self):
        self.__primeiroNome = ''
        self.__ultimoNome = ''
    
    def getPrimeiroNome(self):
        return self.__primeiroNome
    
    def setPrimeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome
    
    def getUltimoNome(self):
        return self.__ultimoNome
    
    def setUltimoNome(self, ultimoNome):
        self.__ultimoNome = ultimoNome
