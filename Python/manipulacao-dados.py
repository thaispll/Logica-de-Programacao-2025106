nome_completo = input("Digite nome e sobrenome")

#versão original
print(nome_completo)

# Maiúsculas 
print(nome_completo.upper())

#Minúsculas
print(nome_completo.lower())

#Retirar espaços no início e no final
print(nome_completo.strip())

#Primeiro nome
nomes = nome_completo.split()
print(nomes[0])
print(len(nomes))

#Deixa a primeira letra de cada palavra maiúscula
print(nome_completo.title())

#Substituir um texto por outro
print(nome_completo.replace("Leal","FIRJAN"))

