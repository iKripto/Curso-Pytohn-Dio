import tkinter as tk

# Função para atualizar a entrada
def adicionar_caractere(caractere):
    entrada_texto.set(entrada_texto.get() + caractere)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada_texto.get())  # Avalia a expressão matemática
        entrada_texto.set(str(resultado))
    except:
        entrada_texto.set("Erro")

# Função para limpar a entrada
def limpar():
    entrada_texto.set("")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Variável para armazenar a entrada
entrada_texto = tk.StringVar()

# Campo de entrada
entrada = tk.Entry(janela, textvariable=entrada_texto, font=("Arial", 20), justify="right", bd=10, relief="ridge")
entrada.grid(row=0, column=0, columnspan=4)

# Layout dos botões
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Criando botões na interface
for (texto, linha, coluna) in botoes:
    if texto == "=":
        btn = tk.Button(janela, text=texto, font=("Arial", 20), command=calcular)
    else:
        btn = tk.Button(janela, text=texto, font=("Arial", 20), command=lambda t=texto: adicionar_caractere(t))
    
    btn.grid(row=linha, column=coluna, ipadx=20, ipady=20, sticky="nsew")

# Botão de limpar
btn_limpar = tk.Button(janela, text="C", font=("Arial", 20), command=limpar)
btn_limpar.grid(row=5, column=0, columnspan=4, ipadx=20, ipady=20, sticky="nsew")

# Ajustando tamanho das colunas
for i in range(4):
    janela.columnconfigure(i, weight=1)
for i in range(6):
    janela.rowconfigure(i, weight=1)

# Executando o loop da interface gráfica
janela.mainloop()
