# Métodos da classe dict:

# {}clear:
# Apaga todos os valores do dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}
}

contatos.clear()
print(contatos) # {}

# {}copy:
# Tira uma cópia do dicionário.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
cópia = contatos.copy()
print(cópia) # {'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}}

# {}fromkeys:
# Cria as chaves, mas não define valor para elas. Elas ficarão lá, vazias. 
dict.fromkeys(["nome", "telefone"]) # {"nome": none, "telefone": none} 
dict.fromkeys(["nome", "telefone"], "vazio")# {"nome": vazio, "telefone": vazio}

# {}get:
# é uma segunda forma de acessar informações dentro de um dicionário.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
# contatos["chave"] # KeyError: 'chave'
print(contatos.get("chave")) # None
print(contatos.get("chave", {'vazio'})) # É o mesmo que dizer para procurar "chaves", se não encontar, retornar "vazio".
print(contatos.get("guilherme@gmail.com", {'vazio'})) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# {}items:
# Retorna um objeto dict_items, que é iterável e pode ser convertido para lista ou tupla.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos.items()) # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

# {}keys:
# Retorna apenas as chaves.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos.keys()) # dict_keys(['guilherme@gmail.com'])

# {}pop:
# Em dicionários, ele retorna e depois remove.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}
}
(contatos.pop("guilherme@gmail.com")) # "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
(contatos.pop("giovanna@gmail.com")) # "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"}
print(contatos) # "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}

# {}popitem:
# Remove os itens na sequência.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    # ('pedro@gmail.com', {'nome': 'Pedro', 'telefone': '3333-2223'})
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    # ('giovanna@gmail.com', {'nome': 'Giovanna', 'telefone': '3333-2222'})
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}
    # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
}
print(contatos.popitem())
print(contatos.popitem())
print(contatos.popitem())

# {}setdefault:
# O método setdefault() em dicionários do Python é utilizado para obter o valor de uma chave e, caso essa chave não exista, ele a adiciona ao dicionário com um valor padrão.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.setdefault("idade", 28)
print(contatos) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, 'idade": 28}

# {}update: 
# Atualiza as informações de um dicionário, substituindo as informações anteriores naquela chave.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
contatos.update({"guilherme@gmail.com": {"nome": "gui"}})
print(contatos) # {'guilherme@gmail.com': {'nome': 'gui'}}
# Você também pode adicionar informações usando update. Basta passar outra chave.
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"}})
print(contatos)
# {'guilherme@gmail.com': {'nome': 'gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2222'}}

# {}values:
# Retorna todos os valores no dicionário, ignorando as chaves.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}
}
print(contatos.values())
# dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3333-2222'}, {'nome': 'Pedro', 'telefone': '3333-2223'}])

# {}in
# verifica se os dados existem naquele dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}
}
"guilherme@gmail.com" in contatos # True
"giovanna@gmail.com" in contatos # True
"Giovanna" in "giovanna@gmail.com" # False

# {}del
# Remove um objeto dentro do dicionário.
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-2223"}
}
del contatos["giovanna@gmail.com"]["nome"]
del contatos["pedro@gmail.com"]
print(contatos)
# {'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '3333-2221'}, 'giovanna@gmail.com': {'telefone': '3333-2222'}}
# Curiosidade: Se utilizar del contatos, apagará o dicionário inteiro.