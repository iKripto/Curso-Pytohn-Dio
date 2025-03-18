#Em Python, temos 3 formas de interpolar váriaveis em Python, conforme abaixo.

#A primeira é usando %, mas não é recomendada hoje em dia.
nome = 'Guilherme'
idade = 28
profissão = 'programador'
linguagem = 'python'

print('olá, meu nome é %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.' %(nome, idade, profissão, linguagem))
#olá, meu nome é Guilherme. Eu tenho 28 anos de idade, trabalho como programador e estou matriculado no curso de python.

#A terceira é usando f strings.
nome = 'Guilherme'
idade = 28
profissão = 'programador'
linguagem = 'python'

print(f'olá, meu nome é {nome} . Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculado no curso de {linguagem}.')
