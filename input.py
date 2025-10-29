nome = input("Digite o seu nome: ") 
#input guarda as informações como se fossem strings(caracteres)
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura: "))

#print("Nome: " + nome + ", Idade: "+ str(idade)+", altura: "+str(altura))
#print("Nome: ", nome, ", Idade: ", idade,", altura: ",altura)

print(f"Nome: {nome}, Idade: {idade}, altura: {altura} ")
