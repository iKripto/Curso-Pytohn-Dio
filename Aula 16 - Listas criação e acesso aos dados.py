# Em Python, listas são uma estrutura de dados que armazena uma sequência de elementos de diferentes tipos (como inteiros, strings, objetos etc.). Elas são mutáveis, ou seja, seus elementos podem ser alterados, adicionados ou removidos após a criação.

# Lista vazia
lista_vazia = []

# Lista com números inteiros
numeros = [1, 2, 3, 4, 5]

# Lista com diferentes tipos de dados
mista = [1, 'Python', 3.14, True]

# Lista aninhada (listas dentro de listas)
aninhada = [[1, 2], [3, 4]]

numeros = list(range(10))
print(numeros)

letras = list('python')
print(letras)

# Acesso direto:
# A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice a partir do zero.

print (numeros[0])
# Imprime o primeiro numero.

print (numeros[8])
# Imprime o oitavo numero a partir do zero. Como o (range(10)) também começa do zero, vai imprimir oito.

print (letras[5])
# Imprime a quinta letra a partir do zero. Ou seja, o N.

frutas = ['maça', 'uva', 'pera', 'mexerica']
print (frutas[0])
#maça
print (frutas[2])
#pera

# Indices negativos:
# Sequências suportam indexação negativa. A sequência começa do -1, de trás para frente do último item da lista.

frutas = ['maça', 'uva', 'pera', 'mexerica']
print (frutas[-1])
#mexerica
print (frutas[-2])
#pera

# Listas aninhadas:
# Listas também são objetos em Python. Com isso, podemos criar listas dentro de listas, que recebem o nome de listas aninhadas. Com isso, podemos criar estruturas bidimensionais (matrizes) que podemos acessar informando linhas e colunas.

matriz = [
    [1, 'a', 'b'],
    [3, 5, 'c'],
    ['d', 'e', 6]
]

print(matriz[0][0])
# 1
print(matriz[1][1])
# 5
print(matriz[2][2])
# 6

print(matriz[0][-1])
# b
print(matriz[-1][-1])
# 6

# Fatiamento: 
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso, basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

lista = ['p','y','t','h','o','n']
print(lista[::])
# python
print(lista[0:])
# python
print(lista[::-1])
# nohtyp
print(lista[0:3:2]) # O último representa o "steps", os números que irão pular. Então, vai pular dois números.
# pt


# Iteração de listas:
# A forma mais comum de percorrer listas é utilizando o comando FOR.

carros = ['gol', 'celta', 'corsa']
for carro in carros:
    print(carros)

# Enumerate: 
# Às vezes é necessário saber qual o índice do objeto dentro do laço for.
# Para isso, podemos usar a função enumerate. 
carros = ['gol', 'celta', 'corsa', 'palio', 'fusca', 'opala']
for indice, carro in enumerate(carros):
    print(f'{indice}:{carro}')


# Compreensão de listas:
# Uma compreensão de listas em Python é uma maneira concisa e eficiente de criar listas. Ela permite gerar uma nova lista aplicando uma expressão a cada item de uma sequência, como uma lista, ou aplicando condições para filtrar elementos. A sintaxe básica é: [expressão for item in sequência if condição]. Isso resulta em uma forma compacta de escrever loops e operações de filtragem em uma única linha.

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
pares = []

# Filtros versão 1:

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# Filtros versão 2:

pares = [numero for numero in numeros if numero % 2 == 0]