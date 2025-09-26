Algoritmo "verifica_idade"

Var
// Desenvolva um programa que leia a idade de uma pessoa
//e informe se ela é maior de idade Adicione um intervalo
// de adolescente

   idade: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
      escreval("Digite a sua idade: ")
      leia(idade)
      
      se idade>=18 entao
         escreval("Você é maior de idade!")
      senao
           escreval("Você é menor de idade!")
           se (idade>=12) e (idade<18) entao
              escreval("Você é adolescente")
           fimse
      fimse

Fimalgoritmo