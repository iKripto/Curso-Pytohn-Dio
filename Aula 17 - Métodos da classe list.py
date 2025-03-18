# Lista.append - Adiciona na lista.

lista = []
lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista)

# Lista.clear - Limpa lista.

lista = [1, 'Python', [40, 30, 20]]
print(lista)
lista.clear()
print(lista)

# Lista.copy - Copia a lista e mostra seu endereço na memória.

lista = [1, 'Python', [40, 30, 20]]
l2 = lista.copy
print(l2)
print(lista)

# Lista.count - Conta quantas vezes aquele objeto aparece na lista.

cores = ['branco', 'preto', 'azul', 'branco', 'amarelo', 'azul', 'vermelho', 'branco', 'vermelho', 'azul']
print(cores.count('branco'))    # 3
print(cores.count('azul'))      # 3
print(cores.count('vermelho'))  # 2

# Lista.extend - Junta elementos de outra lista em uma lista.

linguagens = ['python','java','c++']
print(linguagens)
linguagens.extend(['c#', 'javascript'])
print(linguagens)

# Lista.index - Encontra a posição que o item está na lista, começando do zero. 0 - 1 - 2 - 3 - 4 - 5 - 6.

linguagens = ['python', 'java', 'c++', 'c#', 'javascript']
linguagens.index('java')    # 1
linguagens.index('python')  # 0 

# Lista.pop - O método lista.pop() em Python remove e retorna o último elemento de uma lista.

numeros = [10, 20, 30, 40]
numeros.pop()   # 40
numeros.pop()   # 30
numeros.pop()   # 20

# Lista.remove - Remove um elemento da lista.

linguagens = ['python', 'java', 'c++', 'c#', 'javascript']
linguagens.remove('c++')
print(linguagens)

# Lista.reverse - Inverte os elementos da lista.

linguagens = ['python', 'java', 'c++', 'c#', 'javascript']
linguagens.reverse()
print(linguagens)

# Lista.sort - Organiza os elementos da lista.

linguagens = ['python', 'java', 'c++', 'c#', 'javascript']
linguagens.sort()
print(linguagens)   # ['c#', 'c++', 'java', 'javascript', 'python']

linguagens.sort(reverse=True)
print(linguagens)   # ['python', 'javascript', 'java', 'c++', 'c#']

linguagens.sort(key = lambda x:len(x))  # Organiza pelo tamanho das palavras.
print(linguagens)   # ['c#', 'c++', 'java', 'python', 'javascript']

linguagens.sort(key = lambda x:len(x), reverse=True)    # Organiza pelo tamanho das palavras, mas ao contrário.
print(linguagens)   # ['javascript', 'python', 'java', 'c++', 'c#']

# Lista.len - Serve apenas para ver o tamanho da lista.

linguagens = ['python', 'java', 'c++', 'c#', 'javascript']
print(len(linguagens)) # 5
