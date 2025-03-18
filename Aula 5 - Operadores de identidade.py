#Operadores de identidade:
#São operadores utilizados para comparar se os objetos testados ocupam a mesma posição na memória.

curso = 'curso de python'
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)
#true

print(curso is not nome_curso)
#false

print(saldo is limite)
#false

a = [1, 2, 3]
b = a  # 'b' aponta para o mesmo objeto que 'a'
c = [1, 2, 3]  # 'c' é um novo objeto com o mesmo conteúdo

print(a is b)   # True → 'b' é o mesmo objeto que 'a'
print(a is c)   # False → 'c' tem o mesmo conteúdo, mas é um objeto diferente
print(a is not c)  # True → 'a' e 'c' não são o mesmo objeto

x = 10
y = 10
print(x == y)   # True → os valores são iguais
print(x is y)   # True → apontam para o mesmo objeto (por otimização do Python)

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(lst1 == lst2)  # True → os conteúdos são iguais
print(lst1 is lst2)  # False → são objetos diferentes na memória