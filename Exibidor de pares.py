# Ler e exibir números inteiros em um vetor:

pares = []

while True:
    print('Escolha uma opção:')
    print('[1] Inserir número.')
    print('[2] Imprimir vetor e encerrar.')
    escolha = int(input('Escolha: '))

    if escolha == 1:
        numero = int(input('Insira um numero inteiro:'))
        if numero % 2 == 0:
            pares.append(numero)

    elif escolha == 2:
        print(pares)
        break

    else:
        print("Escolha inválida.")