#Estruturas condicionais:
#A estrutura condicional permite o desvio do fluxo de controle quando determinadas expressões são atendidas.
#IF:
#O programa irá testar a expressão lógica e, caso positivo, as ações no bloco serão executadas.
saldo = 1000
saque = int(input("Digite o valor do saque: "))
if saldo >= saque:
    print('Realizando saque!')

if saldo <= saque:
    print('Saldo insuficiente!')

#IF/ELSE
#Podemos criar uma estrutura condicional com dois desvios. Se if não for verdadeiro, o bloco ELSE será executado automaticamente. 
if saldo >= saque:
    print('Realizando saque!')

else:
    print('Saldo insuficiente!')

#if	Sempre verificado primeiro
#elif	Só avaliado se os if e elif anteriores forem falsos
#else	Executado se nenhuma condição anterior for verdadeira