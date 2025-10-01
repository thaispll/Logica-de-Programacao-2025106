Algoritmo "CondicionalAninhada"

Var
   idade: inteiro

Inicio
      escreval("Digite a sua idade: ")
      leia(idade)
      
      se idade <18 entao
         escreval("Menor de idade")
      senao
           se idade <= 65 entao
              escreval("Adulto")
           senao
                escreval("Idoso")
           fimse
      fimse
Fimalgoritmo