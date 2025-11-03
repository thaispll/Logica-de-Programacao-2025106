#Desenvolva um programa em Python que implemente um sistema simples 
# de cadastro de alunos utilizando somente funções (def). O programa 
# deve incluir:
#Uma função para cadastrar um aluno, que receba uma lista e os dados 
# do aluno (nome, idade e curso) e adicione essas informações como 
# um dicionário à lista.
#Uma função para listar todos os alunos cadastrados, exibindo seus 
# dados de forma organizada.
#Não utilize classes; todas as operações devem ser feitas apenas 
# com funções e estruturas básicas do Python.
#Teste o sistema cadastrando alguns alunos e exibindo a lista ao final.

def cadastrar_alunos(lista, nome, idade, curso):
    aluno = {"nome": nome, "idade":idade, "curso": curso}
    lista.append(aluno)

def listar_alunos(lista):
    for i in range(len(lista)):
        aluno = lista[i]
        print(f" {i + 1}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']} ")

alunos = []

while True:
    print("Cadastro de Aluno")
    nome = input("Nome (ou digite sair para encerrar): ")
    if nome.lower() == "sair":
        break
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    cadastrar_alunos(alunos, nome, idade, curso)
    print("Aluno cadastrado com sucesso! \n")

print("\n Lista de alunos cadastrados:")
listar_alunos(alunos)
