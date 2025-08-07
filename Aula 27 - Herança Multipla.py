class Animal:
    def __init__(self, nro_patas, cor_pelo):
        self.nro_patas = nro_patas
        self.cor_pelo = cor_pelo

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrico(Mamifero, Ave):
    pass

gato = Gato(4, 'preto')
print(gato)

ornitorrinco = Ornitorrico(2, 'vermelho',)
print(ornitorrinco)
