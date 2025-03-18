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

# {}items
# Retorna um objeto dict_items, que é iterável e pode ser convertido para lista ou tupla.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos.items()) # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])

# {}keys
# Retorna apenas as chaves.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}
print(contatos.keys()) # dict_keys(['guilherme@gmail.com'])