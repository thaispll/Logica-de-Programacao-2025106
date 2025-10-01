Algoritmo "real_dolar"
// Disciplina   : Lógica de Programação
// Professor   : Thais Leal 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/09/2025
Var
// Escreva um algoritmo que leia um valor em real e
//converta para dólar, considerando a taxa de câmbio
           moeda_dolar, moeda_real: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
     escreval("Digite o valor em real")
     leia(moeda_real)
     
     moeda_dolar := moeda_real / 5.33
     
     escreval("R$",moeda_real, " foi convertido em $",moeda_dolar:4:2)

Fimalgoritmo