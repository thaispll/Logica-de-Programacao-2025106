Algoritmo "semnome"
// Disciplina   : Lógica de Programação 
// Professor   : Thais Leal 

Var
// Crie um programa que leia a idade de uma pessoa
// e classifique como criança, adolescente, adulto
//ou idoso
idade: inteiro

Inicio
      escreval("Digite sua idade: ")
      leia(idade)
      
      se (idade>=0) e (idade<=12) entao
         escreval("Criança")
      senao
           se (idade>=13) e (idade<18) entao
              escreval("Adolescente")
           senao
              se (idade>=18) e (idade <= 59) entao
                 escreval("Adulto")
              senao
                   se idade >= 60 entao
                      escreval("Idoso")
                   senao
                        escreval("Idade inválida")
                   fimse
              fimse
           fimse
      fimse

Fimalgoritmo