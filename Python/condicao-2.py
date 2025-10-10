idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("Criança")
elif idade <20:
    print("Adolescente")
elif idade <60:
    print("Adulto")
else:
    print("Idoso")