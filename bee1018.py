valor = float(input(""))
print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = valor // nota
    valor = valor % nota
    print(f"{float(quantidade).replace('.',',')} nota(s) de R$ {float(nota).replace('.',','):.2f}")