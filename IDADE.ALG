Algoritmo "Idade"
// Disciplina   : Lógica de Programação
// Professor   : Alexandre Pimentel
// Descrição   : Calcula a idade de uma pessoa
// Autor(a)    : Alexandre
// Data atual  : 12/02/2025
Var
// Seção de Declarações das variáveis 
    nome: caracter
    idade, nascimento: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
    escreva("Digite o seu nome:")
    leia(nome)
    
    escreva("Sua data de nascimento: ")
    leia(nascimento)
    
    idade <- 2025 - nascimento
    
    escreval("Você completa ", idade, " nesse ano.")
    

Fimalgoritmo