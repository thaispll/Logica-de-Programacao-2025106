notas = [9.5, 7.0, 8.5, 5.5, 10.0]

primeira_nota = notas[0]
print(f"A primeira nota foi: {primeira_nota}")

notas[1] = 7.5
print(f"Lista de notas atualizadas: {notas}")

notas.append(6.0)
print(f"Lista de notas atualizadas: {notas}")

notas.sort()
print(notas)

lista = [4,1,2,3]
nova_lista = sorted(lista, reverse=True)
print(nova_lista)
print(lista)

