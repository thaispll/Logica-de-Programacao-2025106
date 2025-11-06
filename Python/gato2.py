
class Gato:
    def __init__(self, raca, nome, peso, idade):
        self.raca = raca
        self.nome = nome
        self.peso = peso
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Raça: {self.raca}")
        print(f"Nome: {self.nome}")
        print(f"Peso: {self.peso}")
        print(f"Idade: {self.idade} anos")

#solicitar
raca = input("Digite a raça do gato:")
nome = input("Digite o nome do gato: ")
peso = float(input("Digite o peso do gato (em kg): "))
idade = int(input("Digite a idade do gato (em anos): " ))

gato = Gato(raca, nome, peso, idade)

gato.mostrar_dados()