"""
Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor
"""

class Bola:
    
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        
    def mostraCor(self):
        return self.cor

"""
Classe Quadrado: Crie uma classe que modele um quadrado:
a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def mudarLado(self, novoLado):
        self.lado = novoLado
        
    def retornarLado(self):
        return self.lado
    
    def calcularArea(self):
        return self.lado ** 2

"""
Classe Retangulo: Crie uma classe que modele um retangulo:
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e
de rodapés necessárias para o local.
"""

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        
    def set_lado_a(self, novo_lado_a):
        self.__lado_a = novo_lado_a
        
    def set_lado_b(self, novo_lado_b):
        self.__lado_b = novo_lado_b
        
    def get_lado_a(self):
        return self.__lado_a
    
    def get_lado_b(self):
        return self.__lado_b
    
    def calcular_area(self):
        return self.__lado_a * self.__lado_b
    
    def calcular_perimetro(self):
        return 2 * (self.__lado_a + self.__lado_b)

"""
Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos,
ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso


    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

"""
• Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os
demais atributos são obrigatórios.
"""

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")


"""
• Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve
ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o
número do canal e o nível do volume permanecem dentro de faixas válidas.
"""

class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def mudar_canal(self, canal):
        if 1 <= canal <= 100:
            self.canal = canal
        else:
            print("Canal inválido")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def mostrar_info(self):
        print("Canal:", self.canal)
        print("Volume:", self.volume)


"""
• Classe Bichinho Virtual: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar
em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os
atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo
para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""

class BichinhoVirtual:
    def __init__(self, nome):
        self.__nome = nome
        self.__fome = 0
        self.__saude = 100
        self.__idade = 0
    
    def alterar_nome(self, novo_nome):
        self.__nome = novo_nome
        
    def alterar_fome(self, valor):
        self.__fome += valor
        if self.__fome < 0:
            self.__fome = 0
        elif self.__fome > 100:
            self.__fome = 100
        
    def alterar_saude(self, valor):
        self.__saude += valor
        if self.__saude < 0:
            self.__saude = 0
        elif self.__saude > 100:
            self.__saude = 100
        
    def alterar_idade(self, valor):
        self.__idade += valor
        
    def retornar_nome(self):
        return self.__nome
        
    def retornar_fome(self):
        return self.__fome
        
    def retornar_saude(self):
        return self.__saude
        
    def retornar_idade(self):
        return self.__idade
    
    def retornar_humor(self):
        return (self.__fome + self.__saude) // 2


"""
• Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o
outro. É possível criar um macaco canibal?
"""

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        if self.bucho:
            print(f"{self.nome} tem no bucho: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está de barriga vazia")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo: {', '.join(self.bucho)}")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada para digerir")

# Teste interativo
macaco1 = Macaco("João")
macaco2 = Macaco("Maria")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.verBucho()

macaco2.comer("Pêssego")
macaco2.verBucho()

macaco1.digerir()
macaco1.verBucho()

macaco2.digerir()
macaco2.verBucho()


"""
Não é possível criar macaco canibal
"""

"""
• Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
a. Possua uma classe chamada Ponto, com os atributos x e y.
b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
c. Possua uma função para imprimir os valores da classe Ponto
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
retângulo, que deve ser um objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
ponto que indique os valores de x e y para o centro do objeto.
h. O valor do centro do objeto deve ser mostrado na tela
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto ({self.x},{self.y})")


class Retangulo:
    def __init__(self, largura, altura, ponto):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto

    def centro(self):
        centro_x = self.ponto.x + self.largura/2
        centro_y = self.ponto.y + self.altura/2
        return Ponto(centro_x, centro_y)


#menu

opcao = 0
while opcao != 3:
    print("1 - Alterar valores do retângulo")
    print("2 - Imprimir centro do retângulo")
    print("3 - Sair")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        x = float(input("Digite a coordenada x do ponto inferior esquerdo: "))
        y = float(input("Digite a coordenada y do ponto inferior esquerdo: "))
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        p = Ponto(x, y)
        r = Retangulo(largura, altura, p)

    elif opcao == 2:
        r_centro = r.centro()
        r_centro.imprimir()


"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro
iii. quantidadeCombustivel
b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
quantidade de litros que foi colocada no veículo
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
combustível e mostra o valor a ser pago pelo cliente.
iii. alterarValor( ) – altera o valor do litro do combustível.
iv. alterarCombustivel( ) – altera o tipo do combustível.
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na
bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
combustível total na bomba.
"""

class BombaDeCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            litros_abastecidos = self.quantidade_combustivel
            valor_abastecido = litros_abastecidos * self.valor_litro
            self.quantidade_combustivel = 0
        else:
            self.quantidade_combustivel -= litros_abastecidos
        print(f"Abastecidos {litros_abastecidos:.2f} litros, valor total R$ {valor_abastecido:.2f}")
    
    def abastecer_por_litro(self, litros_abastecidos):
        valor_abastecido = litros_abastecidos * self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            litros_abastecidos = self.quantidade_combustivel
            valor_abastecido = litros_abastecidos * self.valor_litro
            self.quantidade_combustivel = 0
        else:
            self.quantidade_combustivel -= litros_abastecidos
        print(f"Abastecidos {litros_abastecidos:.2f} litros, valor total R$ {valor_abastecido:.2f}")
    
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
    
    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade


"""
Classe Carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
quantidade de combustível no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
reduzindo o nível de combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
meuFusca = Carro(15) # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20) # abastece com 20 litros de combustível.
meuFusca.andar(100) # anda 100 quilômetros.
meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.
"""

class BombaCombustivel:
    
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        
    def abastecer_por_valor(self, valor):
        quantidade = valor / self.valor_litro
        if quantidade > self.quantidade_combustivel:
            quantidade = self.quantidade_combustivel
        valor_total = quantidade * self.valor_litro
        self.quantidade_combustivel -= quantidade
        return quantidade, valor_total
    
    def abastecer_por_litro(self, quantidade):
        if quantidade > self.quantidade_combustivel:
            quantidade = self.quantidade_combustivel
        valor_total = quantidade * self.valor_litro
        self.quantidade_combustivel -= quantidade
        return quantidade, valor_total
    
    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro
        
    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel
        
    def alterar_quantidade_combustivel(self, quantidade_combustivel):
        self.quantidade_combustivel = quantidade_combustivel


"""
Classe Conta de Investimento: Faça uma classe chamada contaInvestimento que seja semelhante à
classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um
construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros
(sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma
poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método
adicioneJuros() cinco vezes e imprime o saldo resultante.
"""

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100

    def adicione_juros(self):
        self.saldo += self.saldo * self.taxa_juros

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


"""
• Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e
um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para
devolver nome e salário. Escreva um pequeno programa que teste sua classe.
• Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
(porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
• Exemplo de uso:
harry=funcionário("Harry",25000)
harry.aumentarSalario(10)
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def aumentar_salario(self, porcentual):
        aumento = self.salario * porcentual / 100
        self.salario += aumento


"""
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário
especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
• Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores
exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada
no menu, for informada na escolha do usuário. Dica: acrescente um método especial str() à classe
Bichinho.
• Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles
através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário
tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu
deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os
bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa
mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
"""

import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)
        self.saude = random.randint(0, 10)

    def __str__(self):
        return f"Bichinho: {self.nome}\nFome: {self.fome}\nTédio: {self.tedio}\nSaúde: {self.saude}"

    def alimentar(self, quantidade):
        self.fome = max(0, self.fome - quantidade)

    def brincar(self, tempo):
        self.tedio = max(0, self.tedio - tempo)

    def curar(self):
        self.saude = 10

    def mostrar_atributos(self):
        print(self.__str__())

class FazendaBichinhos:
    def __init__(self, nomes):
        self.bichinhos = [Bichinho(nome) for nome in nomes]

    def alimentar_bichinhos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade)

    def brincar_bichinhos(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)

    def curar_bichinhos(self):
        for bichinho in self.bichinhos:
            bichinho.curar()

    def mostrar_atributos_bichinhos(self):
        for bichinho in self.bichinhos:
            print(bichinho.__str__())

# Programa principal
fazenda = FazendaBichinhos(['Bichinho1', 'Bichinho2', 'Bichinho3'])

while True:
    print("""
    1 - Alimentar bichinhos
    2 - Brincar com bichinhos
    3 - Curar bichinhos
    4 - Mostrar atributos dos bichinhos
    0 - Sair
    """)

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        quantidade = int(input("Quantidade de comida: "))
        fazenda.alimentar_bichinhos(quantidade)
    elif escolha == 2:
        tempo = int(input("Tempo de brincadeira: "))
        fazenda.brincar_bichinhos(tempo)
    elif escolha == 3:
        fazenda.curar_bichinhos()
    elif escolha == 4:
        fazenda.mostrar_atributos_bichinhos()
    elif escolha == 0:
        break
    else:
        print("Opção inválida!")
