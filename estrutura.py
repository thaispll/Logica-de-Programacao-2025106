#def nome_da_funcao(parametro1,parametro2):
    #corpo da função
    #código que será executado 
#    return valor 

#parametros padrão
#quando um argumento não é fornecido

def saudacao(nome, mensagem="Olá"):
    return f'{mensagem}, {nome}!'

print(saudacao("Maria"))
print(saudacao("João", "Oi"))
