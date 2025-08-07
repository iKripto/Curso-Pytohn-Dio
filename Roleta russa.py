import random

while True:
    print('[1] Roletar')
    print('[2] Sair')
    escolha = int(input('Escolha uma opção: '))

    if escolha == 1:
        print("Girando o tambor...")
        num = random.randint(1, 6)
        print(f"O número sorteado foi: {num}")

        if num == 6:
                print("Sobrecarregando memória.")
                lista = []
                try:
                    while True:
                        lista.append(bytearray(10**6))  
                except MemoryError:
                    print("Overflow.")
        else:
                print("Você sobreviveu.")
                
    else:
         break