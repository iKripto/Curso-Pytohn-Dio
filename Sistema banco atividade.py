contador = 0
saldo = 3000

while True:
    print(f'Escolha uma opção:')
    print(f'[1] Saque')
    print(f'[2] Depósito')
    print(f'[3] Extrato')
    escolha1 = (int(input('Escolha uma opção: ')))

    if escolha1 == 1:
        saque1 = (int(input('Digite a quantia a ser sacada:')))
        if contador < 3 and saque1 <= saldo and saque1 <= 500:
            saldo -= saque1
            contador += 1
            print('Sacado com sucesso!')
        else:
            print('Erro. Verifique se sacou mais de três vezes hoje ou se excedeu o limite de R$500,00.')
    
    if escolha1 == 2:
        deposito1 = (int(input('Digite a quantia a ser depositada:')))
        saldo += deposito1
        print('Depositado com sucesso!')
    
    if escolha1 == 3:
        print(f'Saldo: {saldo}')


