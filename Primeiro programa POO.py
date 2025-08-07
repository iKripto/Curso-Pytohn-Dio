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
print(vars(b1))

b2 = Bicicleta('verde', 'shimano', '1990', '7000')
print(b2.ano)
b2.buzinar()
b2.correr()
b2.parar()
print(vars(b2))
