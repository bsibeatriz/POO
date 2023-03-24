image.png

"""
Descrição da Imagem caso não abra:
Método protected pode ser acessado pelas classes Mãe e Filha e não pode ser acessado pelo escopo globlal.
Método private só podem ser acessados dentro da própria classe em que foram declarados. 
Eles não podem ser acessados nem mesmo por classes filhas.
"""

"""
1. Crie uma classe chamada Usuario.
"""

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos.")

"""
2. Adicione à classe acima uma propriedade privada com o nome nomeUsuario.
"""

class Usuario:
    def __init__(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario
    
    def getNomeUsuario(self):
        return self.__nomeUsuario


"""
3. Crie um método setter que possa definir o valor do nomeUsuario.
"""
class Usuario:
    def __init__(self):
        self.__nomeUsuario = ""

    def setNomeUsuario(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario


"""
4. Crie uma classe Admin que herde a classe Usuario.
"""

class Admin(Usuario):
    def __init__(self, username, password, nomeUsuario):
        super().__init__(username, password)
        self.__nomeUsuario = nomeUsuario

"""
5. Agora, vamos acrescentar à classe Admin algum código. Primeiro, adicione um método público
chamado de escrevaNome() e faça com que ele retorne a string: "Admin".
"""

class Admin(Usuario):
    def escrevaNome(self):
        return "Admin"


"""
6. Adicione à classe Admin outro método público, digaOla(), que retorne a string "Olá Admin,
XXX" onde XXX é o nome do usuário (nomeUsuario).
"""

class Admin(Usuario):
    def escrevaNome(self):
        return "Admin"
    
    def digaOla(self):
        return f"Olá Admin, {self.nomeUsuario}"


"""
7. Crie um objeto chamado admin1 fora da classe Admin. Defina seu nome para "Baltazar" e diga
olá ao usuário. Você vê algum problema?

R: Sim, há um problema porque a propriedade nomeUsuario da classe Usuario é privada e não temos um método 
getter para acessá-la fora da classe.
Portanto, não podemos definir o nome do usuário fora da classe Usuario ou Admin.
"""

class Usuario:
    def __init__(self):
        self.__nomeUsuario = ""

    def setNomeUsuario(self, nome):
        self.__nomeUsuario = nome

    def getNomeUsuario(self):
        return self.__nomeUsuario

class Admin(Usuario):
    def escrevaNome(self):
        return "Admin"

    def digaOla(self):
        return f"Olá {self.getNomeUsuario()}, {self.escrevaNome()}"


admin1 = Admin()
admin1.setNomeUsuario("Beatriz")


print(admin1.digaOla()) 


"""
8. Qual é a causa do problema?

R:O problema ocorre porque a propriedade nomeUsuario da classe Usuario é privada e, portanto, não pode ser acessada diretamente por objetos fora da classe.
Para acessar essa propriedade, deve-se usar um método público de acesso, como o setter
"""

"""
9. Altere o código para corrigir o problema.

R Implemnetação já ajustada na atividade 7
"""

"""
10. Tente escrever a solução com um método getter dentro da classe mãe que pode ser usado a partir da
classe filha.
"""

class Usuario:
    def __init__(self):
        self.__nomeUsuario = ""

    def setNomeUsuario(self, nome):
        self.__nomeUsuario = nome

    def getNomeUsuario(self):
        return self.__nomeUsuario

class Admin(Usuario):
    def escrevaNome(self):
        return "Admin"

    def digaOla(self):
        return f"Olá {self.getNomeUsuario()}"


admin1 = Admin()
admin1.setNomeUsuario("Beatriz")


print(admin1.digaOla()) 
