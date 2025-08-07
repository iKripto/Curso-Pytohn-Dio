class Veiculo:
    def __init__(self, cor, placa, rodas):
        self.cor = cor
        self.placa = placa
        self.rodas = rodas
    
    def Ligar_Motor(self):
        print("Vrum, vrum... ")
    

class Motocicleta(Veiculo): # Não cria seu próprio __init__ 
    pass

class Carro(Veiculo):
    pass

# Por que Motocicleta e Carro funcionam mesmo sem super()?
# Porque você usou o pass, ou seja, não sobrescreveu o construtor.
# Logo, o Python usa automaticamente o __init__ da classe pai (Veiculo).

#  Neste caso, como nada foi sobrescrito, o construtor do Veiculo é chamado automaticamente.

class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado,):
        super().__init__(cor, placa, rodas) # Chama o __init__ da classe pai
        self.carregado = True # Adiciona atributo novo da subclasse
        

    def Esta_Carregado(self):    
        print(f"{'sim' if self.carregado else 'não'} estou carregado.")

# Você sobrescreveu o __init__ com novos parâmetros (inclusive adicionou carregado). Isso 
# interrompe a herança automática do construtor, então você precisa chamar o super() 
# manualmente, senão os atributos cor, placa e rodas não são definidos.


moto = Motocicleta('preta', 'abc-123', 2)
print(moto)
moto.Ligar_Motor()

carro = Carro('branco', 'abc-124', 4)
print(carro)
carro.Ligar_Motor()

caminhao = Caminhao('amarelo', 'abc-125', 6, True)
print(caminhao)
caminhao.Ligar_Motor()
caminhao.Esta_Carregado()
