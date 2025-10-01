Algoritmo "valida_senha"
// Disciplina   : Lógica de Programação
// Professor   : Thais Leal 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 25/09/2025
Var
// Escreva um algoritmo que leia senhas e repita
//enquanto a senha não corresponder à senha correta
//"admin"

         senha: caractere

Inicio

      repita
            escreval("Digite a senha: ")
            leia(senha)
            
            se senha <> "admin" entao
               escreval("Senha incorreta, tente novamente.")
            fimse
      ate senha = "admin"
      
      escreval ("Senha correta! Acesso autorizado.")


Fimalgoritmo