'''
1. Qual palavra-chave (keyword) você usaria para ter acesso às propriedades e métodos de uma classe
estando dentro dela?
R:  c) A palavra-chave self
'''
# Exercício de Codificação

class Usuario():
    primeiroNome = ""
    segundoNome = ""

    def hello(self):
        return "Olá" + self.primeiroNome + " " + self.segundoNome

usuario1 = Usuario()
usuario1.primeiroNome = "Jonnie"
usuario1.segundoNome = "Bravo"
print(usuario1.hello())
