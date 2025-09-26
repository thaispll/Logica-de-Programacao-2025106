Algoritmo "celsius_farenheint"

Var
// Desenvolva um programa que converta uma temperatura
//em Celsius para Fahrenheint
temp_f, temp_c: real

Inicio
   escreval("Digite a temperatura em Celsius: ")
   leia(temp_c)
   temp_f := (temp_c * 9/5) + 32
   escreval("Temperatura em Fahrenheint: ",temp_f:4:2,"F")

Fimalgoritmo