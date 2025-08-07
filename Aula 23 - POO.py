# Método __init__ e self:
# Imagine que você está construindo bonecos
# Cada boneco tem:
# uma cor,
# um nome,
# um tamanho.
# Então, você decide fazer uma fábrica de bonecos. Cada vez que alguém pedir um boneco, a fábrica vai montar um com as características que a pessoa pedir.
# __init__ é o que a fábrica faz logo que começa a montar o boneco. É como se fosse a primeira coisa que acontece quando você cria o boneco.
# Ou seja, o __init__ é o início da criação do boneco: ele pega as informações (como nome, cor, tamanho) e coloca no boneco que está sendo feito.
# Self é uma forma de dizer “esse boneco que estou criando agora”.
# Então, quando você diz:
# self.nome = nome
# Você está dizendo: “Pegue o nome que o cliente mandou e coloque nesse boneco aqui”.

class Boneco:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

# class Boneco: → Você criou uma fábrica de bonecos.

# def __init__... → Aqui começa o processo de montar um boneco.

# self.nome = nome → Guarda o nome no boneco.

# self.cor = cor → Guarda a cor no boneco.

# self.tamanho = tamanho → Guarda o tamanho no boneco.

meu_boneco = Boneco("Robozinho", "Azul", "Pequeno")
print(meu_boneco)
print(dir(meu_boneco)) # Quando quer entender um objeto, se utilizar dir()
print(vars(meu_boneco)) # Acessa o dicionário do objeto. Isto é, acessa suas informações.











# Primeiro programa em POO:
# João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. Crie um programa onde joão informe : Cor, Ano, Modelo e Valor da bicicleta vendida. Uma bicicleta pode: Buzinar, Parar e Correr. Adicione esses comportamentos!

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): 
        self.cor = cor                           
        self.modelo = modelo                     
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plim plim...')
    
    def parar(self):
        print('Parando...')
        print('Bicicleta parada.')

    def correr(self):
        print('Vrum...')

# O método construtor é um método especial de uma classe em Python chamado __init__. Ele é automaticamente executado quando você cria um novo objeto daquela classe.
# A função principal do construtor é inicializar os atributos do objeto com os valores que você passar na hora da criação.
# Esse __init__ é o construtor. Ele recebe argumentos, e armazena esses dados na instância (usando self).

# Podemos usar "pass" dentro de uma classe vazia para deixarmos ela sem informações sem o compilador reclamar.

b1 = Bicicleta('vermelha', 'caloi', '2025', '1900')
print(b1.cor)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)