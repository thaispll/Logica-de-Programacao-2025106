# condição o programa verificará 
# se a nota é menor que 5(reprovadpo). Se não, 
#verifica se a nota é menor que 7 (rec)
#Caso nenhuma dessas condições seja
#verdadeira, imprime "Aprovado"

nota = float(input("Digite a sua nota: "))
if nota >=0 and nota < 5:
    print("Reprovado")
elif nota >=0 and nota <7:
    print("Recuperação")
elif nota <= 10 and nota>=7:
   print("Aprovado") 
else:
    print("Resposta inválida!")
