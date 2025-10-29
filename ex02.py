'''1. Crie um programa no qual o usuário informe um número
inteiro positivo N e armazene-o em uma variável. Em seguida,
o usuário deve digitar N números. Ao fim, o programa deve 
imprimir a média aritmética dos N números digitados. '''

n = int(input("Digite um nº inteiro: "))

soma = 0

for i in range(n):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma/n
print(f"A média aritmética dos números digitados é : {media}") 