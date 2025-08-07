# Um set é uma coleção de objetos e tem elementos únicos, usamos set para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
# NÃO CONFIE NA ORDEM, ELA É ALEATÓRIA!

print (set([1, 2, 3, 3, 2, 1]))
# [1, 2, 3, 3, 2, 1]

print (set(['corsa', 'fusca', 'corsa', 'opala']))
# {fusca, opala, corsa}

print (set('abacaxi'))
# {'a', 'i', 'c', 'b', 'x'}

# Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o conjunto para lista.

numeros = {1, 2, 3, 2}
numeros = list(numeros)
print (numeros[0])
# Funciona.
# Se não convertessemos, o Python retornaria um TypeError: 'set' is not substriptable.


# Iterar conjuntos: 
# A forma mais comum para percorrer dados de um conjunto é utilizando o comando for.
carros = {'gol', 'celta', 'palio'}
for carro in carros:
    print(carro) # palio celta gol


# Função Enumerate:
# Às vezes é necessário saber o indíce do objeto dentro do laço for. Para isso, usamos enumerate.
carros = {'gol', 'celta', 'palio'}
for indice, carro in enumerate(carros):
    print(f"{indice} {carro}")
# 0 gol
# 1 celta
# 2 palio