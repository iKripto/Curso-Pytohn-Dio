#Os operadores de associação em Python são usados para verificar se um valor está presente dentro de uma sequência (como listas, tuplas, strings, conjuntos ou dicionários).

#Operadores:
#in → Retorna True se o valor estiver presente na sequência.
#not in → Retorna True se o valor não estiver presente na sequência.

frutas = ["maçã", "banana", "laranja"]

print("banana" in frutas)   # True → "banana" está na lista
print("uva" in frutas)      # False → "uva" não está na lista
print("uva" not in frutas)  # True → "uva" realmente não está na lista

texto = "Aprendendo Python!"

print("Python" in texto)    # True → "Python" está na string
print("Java" in texto)      # False → "Java" não está na string

dados = {"nome": "Alice", "idade": 25}

print("nome" in dados)      # True → "nome" é uma chave no dicionário
print("Alice" in dados)     # False → "Alice" é um valor, não uma chave
print("Alice" in dados.values())  # True → Verifica se "Alice" está entre os valores