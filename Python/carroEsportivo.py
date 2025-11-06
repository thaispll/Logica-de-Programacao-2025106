#classe pai
class Carro:
    def __init__(self, motor, rodas):
        self.motor = motor
        self.rodas = rodas
    
    def acelerar(self):
        print("O carro está acelerando.")
    
    def frear(self):
        print("O carro está freando")

#classe filha herda da classe Carro
class CarroEsportivo(Carro):
    def __init__ (self, motor, rodas, turbo):
        super().__init__(motor,rodas) # Herda motor e rodas da classe pai
        self.turbo = turbo

    def usar_turbo(self):
        if self.turbo:
            print("Turbo ativado! Aceleração máxima!")
        else:
            print("Turbo não disponível.")

meu_carro = CarroEsportivo("V8", 4, True)
print(f"Motor: {meu_carro.motor}")
print(f"Rodas: {meu_carro.rodas}")
meu_carro.acelerar()
meu_carro.usar_turbo()
meu_carro.frear()
meu_carro_sem_turbo = CarroEsportivo("V6",4,False)
meu_carro_sem_turbo.usar_turbo()