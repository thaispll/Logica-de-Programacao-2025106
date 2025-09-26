Algoritmo "Positivo_negativo"

Var
//Escreva um algoritmo que leia um número e verifique
// se ele é positivo ou negativo
   numero: real

Inicio
      escreval("Digite um número: ")
      leia(numero)
      
      se numero > 0 entao
         escreval("Esse Número é positivo")

      senao
           se numero <0 entao
              escreval("Número negativo")
           senao
                escreval("Zero")
           fimse
      fimse

Fimalgoritmo