Algoritmo "Exemplo"
// Disciplina   : Lógica de Programação
// Professor   : Alexandre Pimentel
// Descrição   : Demonstra as variáveis e funções
// Autor(a)    : Alexandre Pimentel
// Data atual  : 11/02/2025
Var
// Seção de Declarações das variáveis 
    minimo, salario, quantidade: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
    escreval("Salário mínimo atual: ")
    leia(minimo)
    
    escreval("Salário funcionário: ")
    leia(salario)
    
    quantidade <- salario/minimo
    escreva("O func. recebe ", quantidade)
    escreval(" de salários mínimos")

Fimalgoritmo