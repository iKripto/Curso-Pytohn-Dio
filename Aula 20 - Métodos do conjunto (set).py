# Conjuntos numéricos:

# {}union:
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print (conjunto_a.union(conjunto_b)) # {1, 2, 3, 4}

# {}intersection:
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print (conjunto_a.intersection(conjunto_b)) # {2, 3}

# {}diference 
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print (conjunto_a.difference(conjunto_b)) # {1}
print (conjunto_b.difference(conjunto_a)) # {4}

# {}symmetric_diference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print (conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

# {}issubset - Verifica se é um subconjunto e se verdadeiro retorna true.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 3, 5, 2, 6, 1}
print (conjunto_a.issubset(conjunto_b)) # true
print (conjunto_b.issubset(conjunto_a)) # false

# {}issuperset - O contrário de issubset.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 3, 5, 2, 6, 1}
print (conjunto_a.issuperset(conjunto_b)) # false
print (conjunto_b.issuperset(conjunto_a)) # true

# isdisjoint() - Verifica se está em estado de disjunta e se verdadeiro retorna true.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}
conjunto_c = {1, 0}
print (conjunto_a.isdisjoint(conjunto_b)) # true
print (conjunto_a.isdisjoint(conjunto_c)) # false


# Outros métodos de conjunto:

# {}add
sorteio = {1, 23}
sorteio.add(25) # {1, 25, 23}
sorteio.add(42) # {1, 42, 25, 23}
sorteio.add(25) # {1, 42, 25, 23}
# Conjuntos não podem ter elementos repetidos, então 25 é ignorado.
print(sorteio) # {1, 42, 25, 23}

# {}clear
sorteio = {1, 23}
sorteio.clear()
print (sorteio) 
# Vazio.

# {}copy
sorteio = {1, 23}
print (sorteio.copy)

# {}discard
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
numeros.discard(1)
numeros.discard(4)
numeros.discard(90)
print (numeros) # 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

# {}pop
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print (numeros.pop()) # 1
print (numeros.pop()) # 2 
print (numeros.pop()) # 3 
print (numeros.pop()) # 4

# {}remove
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
numeros.remove(1)
numeros.remove(4)
# numeros.remove(90) < Retornaria um ERRO. Funciona igual o discard, mas quando não foi possível remover, retorna erro.
print (numeros) # 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

# {}len
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print (len(numeros)) # 15

# {}in
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
1 in numeros # true
90 in numeros # false

