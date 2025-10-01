Algoritmo "validarNota_repita"

Var
// Seção de Declarações das variáveis
   nota: real


Inicio
      repita
            escreval("Digite a nota (0 a 10): ")
            leia(nota)
            
            se (nota < 0) ou (nota > 10) entao
               escreval("Nota inválida! Tente novamente.")
            fimse
            
      ate (nota >=0) e (nota <=10)
      escreval("Nota registrada: ", nota)

Fimalgoritmo