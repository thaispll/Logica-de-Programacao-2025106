#Imprima números pares de 1 a 30 que 
# são divisíveis por 3
def funcao_divisivel():
    for numero in range(1,31):
        if numero % 2 == 0 and numero %3 ==0:
            print(numero)

funcao_divisivel()
