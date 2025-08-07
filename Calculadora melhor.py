def soma(x, y):
    print(f'O resultado é: {x+y}')

def sub(x, y):
    print(f'O resultado é: {x-y}')

def mult(x, y):
    print(f'O resultado é: {x*y}')

def div(x, y):
    print(f'O resultado é: {x/y}')

while True:
    print(f'=========calculadora=========')
    print(f'Escolha uma opção: ')
    print(f'[1] Soma')
    print(f'[2] Subtração')
    print(f'[3] Multiplicação')
    print(f'[4] Divisão')
    print(f'=============================')

    escolha = (int(input('Escolha: ')))

    num1 = (float(input('Escolha o primeiro numero: ')))
    num2 = (float(input('Escolha o segundo numero: ')))
    if (num2 == 0 and escolha == 4):
        print("Impossível dividir por 0. Encerrando o programa.")
        break

    if escolha == 1:
        soma(num1, num2)
    
    if escolha == 2:
        sub(num1, num2)

    if escolha == 3:
        mult(num1, num2)
    
    if escolha == 4:
        div(num1, num2)
    
    escolha2 = (str(input('Deseja fazer mais operações? S/N')))

    if escolha2.lower() == 's':
        print('Retornando ao inicio.')

    elif escolha2.lower() == 'n':
        print('Encerrando...')
        break
    else:
        print('Escolha inválida. Retornando para o inicio do programa.')