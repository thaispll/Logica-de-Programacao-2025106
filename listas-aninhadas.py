#lista que existe como elemento de outra lista
familia = ["Willyan e Márcia",["Deniel", "Thais"]]
print(familia)

matriz = [
    [2, 1, -5],
    [3, 7, 0],
    [6, 4, 8]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
