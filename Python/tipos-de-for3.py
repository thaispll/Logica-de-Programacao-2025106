frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    if fruta == 'banana' :
        break
    print(fruta)

# iterar sobre strings
mensagem = "Olá"
for caractere in mensagem:
    print(caractere)

#enumerate
for indice, fruta in enumerate(frutas):
    print(f"índice {indice}: {fruta}")