#Operadores aritméticos:
#Os operadores aritméticos executam operações matemáticas como adição, subtração, etc.

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

soma = x+y
sub = x-y
mult = x*y
div = x/y
# Ou div = x//y para retornar inteiro.
resto = x%y

print(f"Soma = {soma}, subtração = {sub}, multiplicação = {mult}, divisão = {div}, resto = {resto}")
