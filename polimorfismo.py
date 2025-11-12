class Carro:
    def acelerar(self):
        print("O carro está acelerando de forma padrão.")

class CarroEsportivo(Carro):
    def acelerar(self):
        print("O carro esportivo acelera muito rápido!")
#criando objetos
carro_comum = Carro()
carro_esportivo = CarroEsportivo()

#chamando método acelerar
carro_comum.acelerar()
carro_esportivo.acelerar()