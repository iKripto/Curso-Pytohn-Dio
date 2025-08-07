#Estudo aprofundado sobre funções: 
#Uma função é um bloco de código, identificado por um nome e pode receber uma lista de parâmetro, esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e permite reutilizar o código na forma de blocos. Programas em funções é o mesmo que dizer que estamos programando de maneira estruturada.

#Em Python, diferente de c++, somos OBRIGADOS a definir um valor para as variáveis declaradas na estrutura. 

def exibirmensagem():
    print('olá, mundo!')

def exibirmensagem2(nome = 'pedro'):
    print(f'Olá, {nome}, seja bem vindo!')

#Em Python, não precisamos declarar explicitamente o tipo de retorno de uma função, ao contrário de C++, onde é necessário especificar o tipo de retorno (como int, float, etc.).
#Além disso, em Python, se não houver uma instrução return dentro da função, a função retorna automaticamente None, que é o valor padrão de retorno para funções sem um valor explícito de retorno.

def somar(a, b):
    resultado = a + b
    print(resultado)

