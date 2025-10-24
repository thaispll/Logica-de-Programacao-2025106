linha1 = input().split()
cod1, quantidade1, valor1 = linha1

linha2 = input().split()
cod2, quantidade2, valor2 = linha2

total = (int(quantidade1) *float(valor1))+ (int(quantidade2) * float(valor2))

print(f"VALOR A PAGAR: R$ {total:.2f}")
