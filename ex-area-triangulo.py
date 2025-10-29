#Faça uma função que recebe base e altura e retorna a área do triângulo usando a fórmula
# área = (base x altura) /2
def area_triangulo(base,altura):
    area = base * altura/2
    return f'A área do triângulo é de {area} cm²'

print(area_triangulo(2,3))

