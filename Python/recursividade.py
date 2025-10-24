#Função recursiva é uma função que chama si mesma dentro
#de sua definição

def fatorial(n):
    #calcular o fatorial de n recursivamente
    if n <= 1:
        return 1
    return n* fatorial(n - 1)
print(fatorial(5))