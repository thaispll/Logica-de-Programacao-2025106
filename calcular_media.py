#Crie uma função chamada calcular_media(nota_a, nota_b) 
# que recebe as duas notas, calcula a média ponderada e
#  retorna o resultado. A função principal leria as 
# entradas e chamaria calcular_media
def calcular_media(n1,n2):
    resultado_media = (n1 * 2 + n2 *3)/5
    print(f'A média do aluno é {resultado_media}')

#calcular_media(7,8)

def calcular_media_input():
    num1 = float(input("Digite a 1ª nota: "))
    num2 = float(input("Digite a 2ª nota:"))
    resultado_media_input = (num1 * 2 + num2 *3)/5
    return f'A média do aluno é {resultado_media_input}'
print(calcular_media_input())