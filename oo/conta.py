

class Conta:

    def __init__(self, numero, titular,saldo, limite): #self - guarda o endereço de memória
        print("Construindo objeto ...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite