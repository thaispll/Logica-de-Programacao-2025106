class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade #atributos públicos
        self.__cpf = cpf # atributo privado

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        print(f"CPF (privado): {self.__cpf}")

    def alterar_cpf(self, novo_cpf):
        self.__cpf = novo_cpf  #método para alterar o modo privado

pessoa1 = Pessoa("Iracema", 74, "123456789-00")
pessoa1.mostrar_dados()

#Acessando diretamente ao atributo privado
#print(pessoa1.__cpf) #gera erro pois não é possível acessar diretamente
pessoa1.alterar_cpf("987654321-00")
pessoa1.mostrar_dados()


    
