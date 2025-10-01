Algoritmo "Aumento e imposto"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 

Var
   dia, mes, DPassados:inteiro

Inicio
      escreval("Digite o número do mês: ")
      leia( mes)
      escreval ("Digite o dia do mês")
      leia (dia)
      
      //calculo
      DPassados <-(mes-1)*30 + dia
      
      escreval("Dias passados desde o inicio do ano", DPassados, " dias")
      

Fimalgoritmo