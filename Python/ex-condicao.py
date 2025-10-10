#Elabore um programa que receba o nome do dia da 
# semana e imprima:
#"Fim de semana" se for sábado ou domingo;
#"Início da semana" se for segunda-feira;
#"Dia útil" para os outros dias.

dia = input("Digite o dia da semana").strip().lower()

if dia == "sábado" or dia == "sabado" or dia =="domingo":
    print("Fim de semana!")
elif dia == "segunda-feira" or dia == "segunda":
    print("Início da semana.")
else:
    print("Dia útil")