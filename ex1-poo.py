#Crie uma classe Animal com os atributos nome e idade.
#Crie um método fazer_som() que imprime uma mensagem genérica.
#Crie duas classes filhas: Cachorro e Gato, que herdam de Animal.
#Sobrescreva o método fazer_som() nas classes filhas para imprimir 
# sons específicos ("Au Au" para cachorro e "Miau" para gato).

#Criar Classe Animal: nome e idade
class Animal:
    def __init__ (self, nome ,idade):
        self.nome = nome
        self.idade = idade

#Crie um método fazer_som() que imprime uma mensagem genérica.
    def fazer_som(self):
        print("Algum animal está fazendo barulho!")
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

#Crie Cachorro e Gato, que herdam de Animal.

class Cachorro(Animal):
#Sobrescreva o método fazer_som() nas classes filhas para imprimir 
# sons específicos ("Au Au" para cachorro e "Miau" para gato).
    def fazer_som(self):
        print("Au au!")
    
    def mostrar_dados(self):
        super().mostrar_dados()
        print("Tipo: Cachorro")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")

    def mostrar_dados(self):
        super().mostrar_dados()
        print("Tipo: Gato")

#gato1 = Gato("Paçoca", 0.5)
#cachorro1 = Cachorro("Luke", 5)
#animal = Animal("Capivara de BM", 2)

#gato1.fazer_som()
#cachorro1.fazer_som()
#animal.fazer_som()

#com input
nome = input("Digite o nome do animal: ")
idade = int(input("Digite a idade do animal (em anos): "))
tipo = input("Digite o tipo do animal: (cachorro, gato ou animal): ").strip().lower()

#Criar o objeto baseado no tipo
if tipo == "cachorro":
    animal = Cachorro(nome, idade)
elif tipo == "gato":
    animal = Gato(nome, idade)
else:
    animal = Animal(nome, idade)

#chamar método para mostrar som
animal.fazer_som()
animal.mostrar_dados()


    
