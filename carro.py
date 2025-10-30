carros_cadastrados = []

class Carro:
    def __init__ (self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        carros_cadastrados.append(self)

    def buzinar(self): 
        print(f"O {self.modelo} está buzinando: BEEP BEEP!")

    def mostrar_info(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}")

carro1 = Carro("Fusca", "Azul", 1980)

carro2 = Carro("Civic", "Prata",2020)
carro1.buzinar()
carro2.buzinar()

print("Carros cadastrados: ")
for carro in carros_cadastrados:
    carro.mostrar_info()