#Estética:
#Identar o código é a forma de manter o código fonte mais manutentível e legível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

#As linguagens de programação costumam utilizar caracteres para terminar e iniciar o fim do bloco. Em Java e C por exemplo, utilizamos chaves.

#Bloco em c:
#Void sacar(x,y){
#   if (saque > saldo){
#       cout << "Inválido" << "\n";
#    }
#}

#Existe uma convenção em Python, que define as boas práticas para escrita e código da linguagem. Nesse documento, é recomendado utilizar 4 espaços em branco por nível de identação. 
def sacar(self, valor: float) -> None:
    if self.saldo >= valor:
    
     self.saldo -= valor
    