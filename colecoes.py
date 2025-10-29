#Listas: são coleções ordenadas, 
# mutáveis e definidas com colchetes []
# Podem conter elementos VARIADOS e permitem adicionar,remover ou alterar
programadores = ['CBUM', 'Ramon Dino', 'Jorlan', 'Michael Jackson']
programadores.append('Cariani') # adicionar ao final
programadores[1] = 'Mike Sommerfeld'
print(programadores)

#Tuplas: semelhantes a listas, MAS IMUTÁVEIS, criadas com parênteses
meses = ('Janeiro','Fevereiro', 'Março')
print(meses[0])

# Dicionáros: armazenam pares chave-valor
#são mutáveis e criados com chaves {}

clientes = {
    'cliente1': {'nome':'Crispim do milho', 'idade': 78, 'telefone': '33580650'},
    'cliente2': {'nome':'Xaolin matador de porco', 'idade': 14, 'telefone': '40028922'},
}
print(clientes['cliente2']['nome'])
