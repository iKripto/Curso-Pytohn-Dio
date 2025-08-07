#Parametros especiais: 
#Por padrão, argumentos podem ser passados para uma função em Python tanto por posição quanto por nome. Para uma melhor legibilidade de desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados. Assim, um desenvolvedor precisa apenas olhar para a função para determinar se os itens são passados por posição, por posição e nome ou nome. 


#Positional only:
#Em Python, parâmetros positional-only são aqueles que só podem ser passados por posição ao chamar uma função. Ou seja, eles não podem ser passados por nome (keyword arguments).
#A partir do Python 3.8, é possível definir esses parâmetros usando a barra (/) na assinatura da função. Tudo que vier antes da barra deve ser passado apenas por posição.

def criarcarro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criarcarro('fiat', '2015','ABC123', marca='fiat', motor='1.0', combustivel='gasolina' )
#Válido.

criarcarro(modelo='fiat', ano='2015', placa='ABC123', marca='fiat', motor='1.0', combustivel='gasolina' )
#Inválido.

#Keyword only:
#Os parâmetros keyword-only em Python são aqueles que só podem ser passados por nome, e não por posição.
#Para definir esses parâmetros, usamos o asterisco (*) na assinatura da função. Tudo o que vier depois do * deve ser passado por nome.

def criarcarro(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criarcarro(modelo='fiat', ano='2015', placa='ABC123', marca='fiat', motor='1.0', combustivel='gasolina' )
#Válido.

criarcarro('fiat', '2015','ABC123', 'fiat', '1.0', 'gasolina' )
#Inválido.

#É possível dividir, usando o / e * na posição que quer.