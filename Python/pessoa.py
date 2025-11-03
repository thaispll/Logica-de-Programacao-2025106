class Pessoa:
    def __init__ (self, nome,idade):
    #construtor: Inicializar atributos ao criar o objeto
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


#Criando objetos(instâncias) da classe Pessoa
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("The Weekend", 19)

#Usando os objetos
pessoa1.apresentar()
pessoa2.apresentar()

