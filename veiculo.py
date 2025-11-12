class Veiculo:
    def __init__(self, marca, modelo, velocidade_maxima):
        self.marca = marca
        self.modelo = modelo
        self._velocidade_maxima = velocidade_maxima #protegido
        self.__codigo_interno = 'ABC123' #privado

    def _calcular_desempenho(self):
        #método protegido, complexidade oculta
        return f"O veículo pode atingir {self._velocidade_maxima} km/h"

    def mostrar_informacoes(self):
        #interface pública que abstrai os detalhes internos
        desempenho = self._calcular_desempenho()
        return f"Marca {self.marca}, Modelo: {self.modelo}. {desempenho}"
    
    def __metodo_privado(self):
        return "Esse método é privado"

#leitura dos dados pelo usuário
marca = input("Digite a marca do veiculo: ")
modelo = input("Digite o modelo do veículo: ")
velocidade_maxima = float(input("Digite a velocidade máxima do veículo (km/h): "))
veiculo = Veiculo(marca, modelo, velocidade_maxima)
print(veiculo.mostrar_informacoes())
#veiculo = Veiculo("Toyota", "Corolla", 180)
print(veiculo._calcular_desempenho())
#print(veiculo.__metodo_privado) -ERRO NAO FUNCIONA

#Método protegido (1 _):método destinado ao uso interno da classe ou sbclasses
#Método privado (2 __): dificulta o acesso acidental ou externo direto ao método




