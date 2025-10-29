'''Construa um programa para fazer uma pequena entrevista com
os alunos de uma turma. Na entrevista, são informados o sexo e
a idade de cada aluno. Considere que o usuário não sabe quantos 
alunos existem na turma. O programa deve exibir a quantidade de 
homens acima de 18 anos e a quantidade de mulheres de
qualquer idade. Para encerrar o programa, o usuário deve informar 
uma idade negativa.'''

homens_18 = 0
mulheres = 0
outros= 0
while True:
    #receber o gênero e a idade de cada aluno (dentro do loop)
    genero = input("Informe o gênero do aluno (M/F/Outro)").strip().upper()
    idade = int(input("Informe a idade do aluno (nº negativo para encerrar o programa):"))
    
    #interromper a entrada quando a idade informada for negativa
    if idade < 0:
        break
    match genero:
        case 'M':
            #contar a quantidade de homens com idade acima 18 anos.
            if idade >18:
                homens_18 +=1
        case 'F':
            #contar a quantidade de mulheres(qualquer idade)
            mulheres +=1

        case "OUTRO":
            outros += 1
        case _:
            print("Gênero inválido. Digite M ou F")    

print(f"Quantidade de homens acima de 18 anos: {homens_18}")
print(f"Quantidade de mulheres de qualquer idade: {mulheres}")
print(f"Quantidade de alunos com outro gênero: {outros}")



