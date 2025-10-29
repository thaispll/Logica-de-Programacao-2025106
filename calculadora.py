"""Crie um programa em Python que funcione como uma calculadora básica, 
usando funções para cada operação matemática (soma, subtração,
 multiplicação e divisão). 
O programa deve exibir um menu com as opções de operação para o usuário 
escolher. Após a seleção, o programa solicitará dois números e, 
em seguida, chamará a função correspondente para calcular o resultado. 
O resultado deve ser exibido ao usuário. 
O programa deve continuar executando até que o usuário escolha sair.
"""
# criar funções soma, subtração,  multiplicação e divisão 
#criar menu
# selecionei a opção, preciso solicitar 2 números para cálculo
def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Não pode fazer a divisão por zero!"
    return a / b

def menu():
    print("\nCalculadora \n")
    print("Selecione uma das opções: \n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

while True:
    menu()
    escolha = input(" Escolha a operação (de 1 a 5): ")

    match escolha:
        case "1" | "2" | "3" | "4":
            try:
                numero1 = float(input("Digite o 1º número: "))
                numero2 = float(input("Digite o 2º número: "))
            except ValueError:
                print("Erro: Digite um número válido.")
                continue 
            match escolha:
                case "1":
                    resultado = soma(numero1,numero2)
                case "2":
                    resultado = subtracao(numero1,numero2)
                case "3":
                    resultado = multiplicacao(numero1, numero2)
                case "4":
                    resultado = divisao(numero1,numero2)
            print(f"Resultado: {resultado}")
        case "5":
            print("Programa Encerrado.")
            break
        case _:
            print("Opção inválida. Por favor, digite um número entre 1 e 5.")
     
                    
               


