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

gato1 = Gato("Siamês","Luna", 4.5, 3)
gato2 = Gato("Gato Caramelo", "Frederico", 7.5, 0.6)
gato3 = Gato("Gato Caramelo", "Frajola", 4, 3)

#exibir gatos
gato1.mostrar_dados()
print("")
gato2.mostrar_dados()
print("")
gato3.mostrar_dados()

