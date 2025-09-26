Algoritmo "aumento_salario"
// Disciplina   : Lógica de Programação
// Professor   : Thais Leal 

Var
// Escreva um algoritmo que leia o salário de um
//funcionário e calcule o novo salário com 10%
// de aumento
   salario, salario_novo: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva("Digite o seu salário: R$")
   leia(salario)
   
   salario_novo := salario * 1.1
   
   escreva("O seu salário saiu de R$", salario, " para R$",salario_novo)

Fimalgoritmo