Algoritmo "e_par"
// Disciplina   : Lógica de Programação 
// Professor   : Thais Leal 

Var
// Faça um algoritmo que leia 10 números inteiros
//e mostre quantos deles são pares
  contadora, numero, contadorPares: inteiro

Inicio

      para contadora de 1 ate 10 faca:
           escreval("Digite o",contadora,"º número inteiro: ")
           leia(numero)
           
           se (numero % 2 =0) entao
              contadorPares <- contadorPares + 1
           fimse
      fimpara
      escreval("Quantidade de números pares: ", contadorPares)
      

Fimalgoritmo