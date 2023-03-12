'''
1. Acrescente à classe Usuario um método construtor para definir um valor para a propriedade
primeiroNome assim que o objeto for criado.
'''

class Usuario:
    
    def __init__(self, primeiroNome):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ""

usuario1 = Usuario("Diego")


'''
Acrescente ao construtor a capacidade de definir o valor da propriedade ultimoNome, bem como a
propriedade primeiroNome.
'''

class Usuario:
    
    def __init__(self, primeiroNome, ultimoNome):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

usuario1 = Usuario("Diego", "Lima")

'''
Adicione à classe Usuario um método público chamado getNomeCompleto() que retorna o
nome completo do usuário.
'''

class Usuario():
    def __init__(self, primeiroNome, ultimoNome):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

    def getNomeCompleto(self):
        return f"{self.__primeiroNome} {self.__ultimoNome}"


'''
Crie um novo objeto, usuario1, e passe para o construtor os valores do primeiro e último nome. O
primeiro nome é "Johnny" e o sobrenome é "Bravo" (você pode escolher sua combinação preferida
de primeiro e último nome).
'''


usuario1 = Usuario("Johnny", "Bravo")


'''
Obtenha o nome completo e imprima-o na tela.
'''

print(usuario1.getNomeCompleto())
