#Crie um programa que inclua uma função chamada somaImposto.
# Essa função deve receber dois parâmetros: taxaImposto, 
# que representa a porcentagem do imposto sobre vendas, e custo,
#  que é o valor do item antes da aplicação do imposto. 
# A função deve calcular o valor do imposto a partir da taxa fornecida
#  e adicionar esse valor ao custo inicial, retornando o novo custo 
# já com o imposto incluído.
def somaImposto():
    taxaimposto = float(input("Digite a taxa do imposto: "))
    custo_imposto = float(input(" Digite o custo do item: "))
                          
    imposto = custo_imposto * (taxaimposto /100)
    custo_com_imposto = custo_imposto + imposto
    print(f"Custo com imposto: R$ {custo_com_imposto:.2f} ")

somaImposto()
