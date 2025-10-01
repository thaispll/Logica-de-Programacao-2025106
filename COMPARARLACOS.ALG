Algoritmo "CompararLacos"
// Disciplina   : Lógica de Programação

Var

   i, contador, numero: inteiro


Inicio

      escreval("Laço PARA - contar de 1 a 5")
      para i de 1 ate 5 faca
           escreval(i)
      fimpara
      
      escreval("Laço ENQUANTO - repetir enquanto o numero for menor que 5")

      contador <- 1
      enquanto contador < 5 faca
               escreval(contador)
               contador <- contador + 1
      fimenquanto
      
      escreval("Laço REPITA - repetir até que numero maior ou igual a 5")
      contador <- 1
      
      repita
            escreval(contador)
            contador <- contador + 1
      ate contador >= 5

Fimalgoritmo