# Método construtor: 
# O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da nossa classe, criamos um método com o nome __init__.

# __init__
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


# Método destrutor:
# O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores Python não são tão necessários quanto em c++ pois o Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__.

# __del__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Iniciando a classe.')
        self.nome = nome
        self.cor = cor 
        self.acordado = acordado
    
    def __del__(self):
        print('Excluindo instância da classe.')

    def falar(self):
        print('Auau')

    # Quando o objeto c deixa de existir, o Python automaticamente chamará __del__.
    # Geralmente, isso acontece no final da execução do programa, do mesmo jeito que o __init__ é inicializado no processo de instâncialização do objeto.
    

c = Cachorro('Chappie', 'Amarelo')
c.falar()