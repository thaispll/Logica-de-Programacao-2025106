class ContaBancaria:
    def __init__ (self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor >0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self,valor):
        if 0 < valor  <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado!")
        else:
            print("Saldo insuficiente ou valor inválido!")
    
    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: R$ {self.__saldo:.2f}")

conta1 = ContaBancaria("Caio Feliz", 2.50)
conta2 = ContaBancaria("Taylor Swift", 740000000)
conta3 = ContaBancaria("Kanye West")

conta1.consultar_saldo()
conta1.depositar(500)
conta1.sacar(200)
conta1.consultar_saldo()

conta2.consultar_saldo()
conta2.depositar(150)
conta2.sacar(20)
conta2.consultar_saldo()
conta3.consultar_saldo()
conta3.sacar(3)

    
