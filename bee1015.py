from math import sqrt

#Leitura dos valores dos pontos
x1 , y1 = map(float, input("").split()) 
#map: aplica uma função a cada item
x2, y2 = map(float, input("").split())

#calcular a distância usando a formula do enunciado
distancia = sqrt((x2 - x1)**2 + (y2-y1)**2)

print(f"{distancia:.4f}")