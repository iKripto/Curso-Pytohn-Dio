# Em programação, herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos e caracteristicas de uma classe pai.

# Beneficios da herança:
# Representa bem os relacionamentos do mundo real.
# Fornece reaproveitamento de código, não precisa reescrever o mesmo código várias vezes. Além disso, permite adicionar mais recursos para uma classe sem a modificar.
# É de natureza transitiva, o que significa que, se B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

# Sintaxe da herança:

# Herança simples:
# Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples.
class A:
    pass

class B:
    pass

# Herança multipla:
# Quando uma clase filha herda de várias classes pai, ela é chamada de herança multipla.

class A:
    pass

class B:
    pass

class C(A, B):
    pass
