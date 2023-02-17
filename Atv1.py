'''
1. Qual das alternativas abaixo melhor define o termo “classe”?
R:  b) Define e obtém as propriedades e métodos dela.

2. Qual das alternativas abaixo melhor define o termo “objeto”?
R:  a) Um objeto nos dá a capacidade de trabalhar com a classe e ter várias instâncias desta mesma classe.

3. Qual das alternativas abaixo melhor explica o termo "propriedade"?
R:  b) Uma variável dentro de uma classe.

4. Qual das alternativas abaixo melhor explica o termo "método"?
R:  a) Uma função dentro de uma classe.

5. Escreva o que você acha que deveria ser o nome da classe, os nomes das propriedades para o
primeiro e último nome (sobrenome) e o nome do método que retorna “Olá”.
R:  Nome da classe: Usuário
    Propriedades: nome
                  sobrenome
    Método: saudacao
'''
''''
6. Escreva a classe Usuario e adicione as propriedades e o método (em Python):
7. Crie a primeira instância e chame-a de usuario1.
8. Defina os valores do primeiro e último nome para usuario1.
9. Obter o nome e sobrenome do usuário e imprima-os na tela com o comando print.
10. Use o método que retorna “Olá” com as variáveis primeiro nome e último nome para dizer Olá ao usuario
11. Crie (instancie) outro objeto. Chame-o de usuario2, dê a ele o primeiro nome de “Jane” e o
sobrenome de “Silva”, e depois diga “Olá” ao usuário.
'''


class Usuario:
    nome = ""
    sobrenome = ""

    def saudacao(self):
        return "Olá "

usuario1 = Usuario()
usuario1.nome = "Bea"
usuario1.sobrenome = "Marques"

saudacao = usuario1.saudacao()
print(saudacao + usuario1.nome + " " + usuario1.sobrenome)


usuario2 = Usuario()
usuario2.nome = "Diego"
usuario2.sobrenome = "Lima"

saudacao = usuario1.saudacao()
print(saudacao + usuario2.nome + " " + usuario2.sobrenome)

#fim