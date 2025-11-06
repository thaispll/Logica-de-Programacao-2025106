"""Implemente a classe Aluno com atributos nome, matricula e notas (lista), 
métodos para adicionar nota validando entre 0 e 10, calcular média, 
retornar situação ("Aprovado", "Recuperação" ou "Reprovado") 
conforme média, e listar todas as notas."""
class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self,nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
    
    def calcular_media(self):
        return sum(self.notas)/len(self.notas) if self.notas else 0
    
    def mostrar_resultado(self):
        media = self.calcular_media()

    def listar_notas(self):
        return self.notas

nome = input("Nome: ")
matricula = input("Matrícula: ")
aluno = Aluno(nome, matricula)

while True:
    nota = input("Nota (ou enter para sair): ")
    if nota == "":
        break
    try:
        aluno.adicionar_nota(float(nota))
    except:
        print("Insira um número válido!")

print(f"Notas: {aluno.listar_notas()}")
print(f"Média: {aluno.calcular_media():.2f}")
print(f"Resultado: {aluno.mostrar_resultado()}")
