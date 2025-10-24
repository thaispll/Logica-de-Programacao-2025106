#Crie uma função chamada soma que receba
#dois números como parâmetros e retorne a 
# soma deles.Depois, peça para o usuário digitar dois
#numeros, utilize a função para somá-los e imprima o
#resultado
#def soma(n1,n2):
#    return n1 +n2

#print(soma(2,3))

def soma():
    n1 = float(input("Digite o 1º número: "))
    n2 = float(input("Digite o 2º número: "))
    return n1 + n2 #envia o dado para o resto do código
print(soma())
