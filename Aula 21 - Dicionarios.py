# Dicionarios / dict:
# É um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separado por vírgulas.

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome = "Guilherme", idade=28)

pessoa["telefone"] = "3333-1234"

# Acessar dados:

dados = {"nome": "guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"]
dados["idade"]
dados["telefone"]

# Sobrescrever dados:

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)
# {'nome': 'Maria', 'idade': 18, 'telefone': '9988-1781'}

# Dicionários aninhados:
# Dicionários podem armazenar qualquer tipo de objeto em Python, descomo valor, desde que a chave para esse valor seja um objeto imutável como strings e números.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}
}

extra = contatos["guilherme@gmail.com"]
print(extra)
# {'nome': 'Guilherme', 'telefone': '3333-2221'}

# A forma mais comum para percorrer dados de um dicionário é utilizando o comando for.

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)
