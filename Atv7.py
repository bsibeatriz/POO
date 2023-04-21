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

