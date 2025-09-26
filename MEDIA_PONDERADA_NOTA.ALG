Algoritmo "Media_ponderada_nota"

Var
   nota_um, nota_dois, media,nota_rec: real

Inicio
//Pedir as informações para o usuário
        escreval("Digite a primeira nota: ")
        leia(nota_um)

        escreval("Digite a segunda nota: ")
        leia(nota_dois)


//calcular a média
        media := (nota_um *2 + nota_dois*3)/5

//Verificar se o aluno está aprovado ou não
        se media >= 7 entao
           escreval("Você foi aprovado com nota ",media)
        senao
           escreval("Você está de recuperação! Sua nota foi ",media)
           escreval("Digite a nota da recuperação: ")
           leia(nota_rec)

           se nota_rec >= 7 entao
              escreval("Você foi aprovado com nota ",nota_rec)
           senao
                escreval("Você está Reprovado! Sua nota foi ",nota_rec)
           fimse
       fimse

Fimalgoritmo