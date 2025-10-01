Algoritmo "Desafio"
// Disciplina   : Desenvolvimento de Projeto
// Professor   : Alexandre Pimentel
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Alexandre Pimentel
// Data atual  : 17/09/2024
Var
// Seção de Declarações das variáveis 
n, par, impar, contador: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
repita
leia(n)
se n % 2 = 0 entao
par <- par + 1
senao
impar <- impar + 1
fimse
contador <- contador + 1
ate contador = 10

escreval("numeros pares:", par)
escreval("numeros impares:", impar)

Fimalgoritmo