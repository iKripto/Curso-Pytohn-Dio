#Objetos de primeira classe:
#Em Python, tudo são objetos. Dessa forma, funções também são objetos o que as tornam objetos de primeira classe. 

def somar (a,b):
    return a + b

def exibir_resultado (a, b, funcao):
    resultado = funcao(a, b)

def saudacao():
    return "Olá, mundo!"
msg = saudacao  # Atribuímos a função a uma variável
print(msg())  # ✅ Chamamos a função através da variável


#Se quisermos confirmar que saudacao e msg referenciam o mesmo objeto, podemos usar id() ou is:
print(id(saudacao))  # Exibe um identificador único do objeto
print(id(msg))  # Mesmo identificador, pois é a mesma função

print(saudacao is msg)  # ✅ True - Ambos referenciam o mesmo objeto