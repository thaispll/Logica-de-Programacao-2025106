aluno = input("Digite o seu nome completo: ")
ano = int(input("Digite o ano atual: "))
curso = input("Digite o nome do curso: ")
matriculado_input = input("Você está matriculado? (sim/não) ")

#Converter resposta para Bool
# if: se
#else: senão
#matriculado =  True if matriculado_input.lower() == "sim" else False

if matriculado_input.lower()  =="sim":
    matriculado = True
elif  matriculado_input.lower() =="não" or matriculado_input.lower() == "nao":
    matriculado = False
else:
    matriculado = False
    print("Resposta inválida para matrícula, não matriculado")

if matriculado:
    print(f"{aluno} está matriculado(a) no curso")
else:
    print(f" {aluno} não está matriculado(a) no curso.")

