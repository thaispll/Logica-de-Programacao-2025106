Algoritmo "area_triangulo"

Var
// Escreva um algoritmo que leia a base e a altura
//de um triângulo e calcule sua área. A = (b x a)/2
   base,altura,area: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreval("Olá, esse software calcula a área do triângulo.")
   escreval("Digite a base do triângulo: ")
   leia(base)
   
   escreval("Digite a altura do triângulo: ")
   leia(altura)

   area := (base * altura)/2
   
   escreval("A área do triângulo é: ", area,"cm²")

Fimalgoritmo