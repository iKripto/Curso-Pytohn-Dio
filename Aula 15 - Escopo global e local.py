#Em Python, escopo se refere ao contexto onde uma variável é reconhecida e pode ser usada. Existem dois principais tipos de escopo:

# Escopo Global – A variável pode ser acessada de qualquer parte do código.
# Escopo Local – A variável é criada dentro de uma função e só pode ser acessada dentro dela.

x = 10  # Variável global

def minha_funcao():
    print(x)  # Pode acessar 'x' porque está no escopo global

minha_funcao()
print(x)  # Funciona normalmente



#Escopo local
def minha_funcao():
    y = 5  # Variável local
    print(y)

minha_funcao()
print(y)  # ❌ Erro! 'y' só existe dentro da função



#Podemos usar a palavra-chave global para modificar variáveis globais dentro de funções:
x = 10

def alterar():
    global x  # Indica que queremos usar a variável global
    x = x + 5
    print(x)

alterar()  # ✅ Modifica 'x' globalmente
print(x)  # ✅ Agora 'x' tem o novo valor